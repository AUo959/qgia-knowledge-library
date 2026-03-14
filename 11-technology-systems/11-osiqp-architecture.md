# OSIQP Technical Architecture Documentation

**Document ID**: QGIA-KL-TS-11-OSIQP-ARCH  
**Classification**: UNCLASSIFIED  
**Version**: 1.0  
**Last Updated**: 2026-03-13  
**Authority**: QGIA OSIQP Development Team

---

## Purpose

This document is the technical reference for the **Open-Source Intelligence Quantitative Platform (OSIQP) v4.2.1** — the primary data ingestion, processing, sentiment analysis, and query substrate supporting all QGIA analytical operations. It is intended for systems engineers, platform administrators, and senior analysts who require authoritative knowledge of OSIQP internals. Analytical users who do not require system-level knowledge should consult the Analyst Orientation Guide (`07_ANALYST_ORIENTATION.md`).

OSIQP is not a standalone product. It is the **data substrate layer** for QGIA's full analytical stack — providing normalized, indexed, and sentiment-scored intelligence records that feed QSFE, EDM, ABCP, RPRN, and TCA. Every probabilistic forecast Aurora orchestrates at the QGIA node begins with data that passed through OSIQP.

---

## System Specifications Summary

| Parameter | Value |
|---|---|
| **Platform Version** | OSIQP v4.2.1 |
| **Processing Capacity** | 156 qubit-equivalent (hybrid classical-quantum) |
| **Daily Data Ingestion** | 500 TB |
| **Sentiment Analysis Accuracy** | 94.7% |
| **Query Latency** | <50ms (p95) |
| **Uptime SLA** | 99.97% (monthly) |
| **Data Retention (hot)** | 90 days |
| **Data Retention (warm)** | 3 years |
| **Data Retention (cold archive)** | Indefinite (Harmion-compressed) |
| **API Version** | REST v3, gRPC v2 |
| **Symbolic Tag** | `s.tag::system.osiqp.v4` |
| **Node** | L1_QGIA |

---

## 1. System Architecture Overview

### 1.1 Component Architecture (ASCII Diagram)

```
═══════════════════════════════════════════════════════════════════════════
                        OSIQP v4.2.1 — SYSTEM ARCHITECTURE
═══════════════════════════════════════════════════════════════════════════

  ┌─────────────────────────────────────────────────────────────────────┐
  │                      SOURCE INGESTION LAYER                         │
  │  RSS Feeds │ Social APIs │ News Aggregators │ Gov Publications │ DB  │
  └───────────────────────────────┬─────────────────────────────────────┘
                                  │  (raw multi-format streams)
                                  ▼
  ┌─────────────────────────────────────────────────────────────────────┐
  │                    INGESTION BROKER (Kafka Cluster)                 │
  │  Topic partitioning by source_type, region, priority_tier           │
  └───────────────────────────────┬─────────────────────────────────────┘
                                  │
          ┌───────────────────────┼───────────────────────┐
          ▼                       ▼                       ▼
  ┌───────────────┐     ┌─────────────────┐     ┌───────────────────┐
  │  NORMALIZATION│     │  DEDUPLICATION  │     │   TRIAGE ENGINE   │
  │  SERVICE      │     │  SERVICE (LSH)  │     │  (Priority Scorer)│
  └───────┬───────┘     └────────┬────────┘     └────────┬──────────┘
          └───────────────────────┼───────────────────────┘
                                  ▼
  ┌─────────────────────────────────────────────────────────────────────┐
  │                     NLP PROCESSING PIPELINE                         │
  │  Tokenization → Entity Extraction → Sentiment → Classification      │
  └───────────────────────────────┬─────────────────────────────────────┘
                                  │
                    ┌─────────────┴──────────────┐
                    ▼                            ▼
  ┌─────────────────────────┐       ┌────────────────────────────┐
  │  CLASSICAL COMPUTE TIER │       │  QUANTUM-HYBRID COMPUTE    │
  │  (High-volume NLP)      │◄─────►│  (156 qubit-equiv)         │
  │  Llama-4 / XLM-RoBERTa │       │  Amplitude-weighted scoring│
  └─────────────────────────┘       └────────────────────────────┘
                                  │
                                  ▼
  ┌─────────────────────────────────────────────────────────────────────┐
  │                      INDEXING & STORAGE LAYER                       │
  │  Hot Store (NVMe SSD) │ Warm Store (NAS) │ Cold Archive (Harmion)   │
  │  OpenSearch Index     │ Entity Graph (Neo4j) │ Vector Store (Milvus)│
  └───────────────────────────────┬─────────────────────────────────────┘
                                  │
                    ┌─────────────┴──────────────┐
                    ▼                            ▼
  ┌─────────────────────────┐       ┌────────────────────────────┐
  │  QUERY ENGINE (<50ms)   │       │  OSIQP EXPORT API          │
  │  Cache L1: Redis (mem)  │       │  REST v3 / gRPC v2         │
  │  Cache L2: Redis (NVMe) │       │  Feeds: QSFE, EDM, ABCP    │
  │  Cache L3: Materialized │       │  Aurora orchestration layer│
  └─────────────────────────┘       └────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────────┐
  │                  CROSS-CUTTING SERVICES                             │
  │  Security (ZKP + mTLS) │ Monitoring (Prometheus/Grafana)            │
  │  DLP Audit (Caelion)   │ Harmion Compression │ HALO Sync Anchor     │
  └─────────────────────────────────────────────────────────────────────┘
═══════════════════════════════════════════════════════════════════════════
```

### 1.2 Data Flow Summary

Records traverse OSIQP in five sequential stages:

1. **Ingestion** — Raw streams arrive from ~4,200 active source connectors across 14 source categories. The Kafka ingestion broker partitions by `source_type`, `region_tag`, and `priority_tier` (P1–P4).
2. **Normalization and Deduplication** — Each record is converted to the OSIQP Canonical Record Schema (CRS v3). Locality-sensitive hashing (LSH) eliminates near-duplicate content (Jaccard similarity ≥ 0.87).
3. **NLP Processing** — Tokenization, named entity recognition (NER), sentiment scoring, and topic classification. Compute is distributed across classical and quantum-hybrid tiers based on record complexity and priority.
4. **Indexing and Storage** — Processed records are written to the three-tier storage stack (hot/warm/cold) and indexed across OpenSearch, Neo4j entity graph, and Milvus vector store.
5. **Query and Export** — Analysts and downstream systems query through the query engine (p95 <50ms) or receive push exports via the OSIQP API.

---

## 2. Source Ingestion Pipeline

### 2.1 Source Inventory

| Source Category | Count | Daily Volume | Update Frequency |
|---|---|---|---|
| RSS / Atom feeds (news, government) | 1,847 | ~120 TB | Continuous / 5 min |
| Social media APIs (X/Twitter, Telegram, Weibo, VKontakte) | 412 | ~95 TB | Real-time stream |
| News aggregators (Factiva, LexisNexis, aggregated RSS) | 89 | ~40 TB | Batch (15 min) |
| Government publications (official press, legislative records, diplomatic cables — open) | 234 | ~18 TB | Batch (1 hr) |
| Academic and think-tank databases (JSTOR, SSRN, CSIS, IISS, RAND) | 108 | ~8 TB | Batch (daily) |
| Financial and market data (Bloomberg terminal feeds, SEC/EDGAR, SWIFT indicators) | 67 | ~35 TB | Real-time |
| Satellite-derived public data (Sentinel, Landsat, commercial AIS/ADS-B) | 53 | ~112 TB | Batch (6 hr) |
| Radio / broadcast transcript feeds | 178 | ~22 TB | Batch (1 hr) |
| Open-web crawl (targeted domain list — 9,400 domains) | 1,212 | ~50 TB | Batch (24 hr) |
| **TOTAL** | **~4,200** | **~500 TB** | — |

### 2.2 Ingestion Broker Architecture

OSIQP uses a 48-node **Apache Kafka** cluster (3 availability zones × 16 brokers) as the ingestion backbone. Key design decisions:

- **Topic hierarchy**: `osiqp.raw.{source_type}.{region}.{priority}` — e.g., `osiqp.raw.social.middle_east.p1`
- **Priority tiers**: P1 (crisis signals, real-time), P2 (diplomatic / government), P3 (news / analysis), P4 (academic / archival)
- **Throughput capacity**: Sustained 6 GB/s ingest; burst-tested to 14 GB/s
- **Retention**: Raw topics retained 72 hours before offset expiration; processed records persist per storage tier policy

### 2.3 Normalization Service

Every record is converted to the **Canonical Record Schema (CRS v3)** before entering the NLP pipeline:

```json
{
  "record_id": "OSIQP-{YYYYMMDD}-{UUID}",
  "source_id": "string (source connector ID)",
  "source_category": "enum (social|news|gov|academic|financial|satellite|broadcast|web)",
  "source_reliability": "float [0.0–1.0] (Admiralty scale mapping)",
  "region_tags": ["ISO 3166 codes or QGIA region labels"],
  "actor_tags": ["named entities — states, organizations, persons"],
  "language_original": "ISO 639-1",
  "language_normalized": "en",
  "raw_text": "string",
  "normalized_text": "string (cleaned, transliterated, entity-normalized)",
  "publication_timestamp": "ISO 8601",
  "ingestion_timestamp": "ISO 8601",
  "priority_tier": "int [1–4]",
  "dedup_hash": "SHA-256 of normalized_text",
  "lsh_signature": "MinHash signature (128-band)",
  "caelion_anchor": "string (L3 provenance anchor — injected at ingestion)"
}
```

**Admiralty Source Reliability Mapping** — source connectors are pre-scored and reviewed quarterly:

| Admiralty Grade | OSIQP Score Range | Example Source Categories |
|---|---|---|
| A — Completely Reliable | 0.90–1.00 | UN official records, national government primary releases |
| B — Usually Reliable | 0.75–0.89 | Established wire services (AP, Reuters, AFP), IAEA publications |
| C — Fairly Reliable | 0.55–0.74 | Major regional newspapers, credentialed think tanks |
| D — Not Usually Reliable | 0.35–0.54 | Social media verified accounts, anonymous aggregators |
| E — Unreliable | 0.10–0.34 | Unverified social media, fringe platforms |
| F — Cannot Be Judged | 0.00–0.09 | Novel sources, first-time connectors (provisional) |

### 2.4 Deduplication Engine

Near-duplicate elimination uses **MinHash LSH** (128 hash functions, 8 bands of 16 rows each) targeting a Jaccard similarity threshold of 0.87. Performance characteristics:

- False positive rate: <0.3%
- False negative rate: <1.1%
- Processing latency: <2ms per record
- Daily deduplication rate: 23–29% of raw volume (translated content and syndicated news are primary sources)

---

## 3. NLP Processing Pipeline

### 3.1 Pipeline Stages

```
Raw CRS Record
    │
    ▼
[1] TOKENIZATION
    ├─ SentencePiece BPE tokenizer (512k vocabulary, multilingual)
    ├─ 47 supported languages; unsupported languages → transliteration + flag
    └─ Output: token_ids[], attention_mask[]
    │
    ▼
[2] NAMED ENTITY RECOGNITION (NER)
    ├─ Model: XLM-RoBERTa-large fine-tuned on QGIA geopolitical corpus
    ├─ Entity types: PERSON, ORG, GPE (geopolitical entity), LOC, FAC,
    │               WEAPON_SYSTEM, TREATY, EVENT, DATE, QUANTITY
    ├─ Resolution: entities linked to QGIA Entity Registry (680,000+ entries)
    └─ Output: entity_mentions[], entity_ids[], coreference_chains[]
    │
    ▼
[3] SENTIMENT AND TONE ANALYSIS
    ├─ Primary model: QGIA-SentimentNet v3.1 (described in §5)
    ├─ Sentiment dimensions: valence, arousal, domain_hostility, actor_stance
    ├─ Granularity: document-level + sentence-level + entity-directed
    └─ Output: sentiment_vector[4], entity_sentiment_map{}
    │
    ▼
[4] TOPIC CLASSIFICATION
    ├─ QGIA taxonomy: 12 top-level domains × 847 leaf topics
    ├─ Model: DeBERTa-v3-large fine-tuned on QGIA annotated corpus
    ├─ Multi-label (records may carry 1–5 topic labels)
    └─ Output: topic_labels[], topic_confidence_scores[]
    │
    ▼
[5] THREAT SIGNAL SCORING
    ├─ Rule-based + ML hybrid
    ├─ Signals: escalation keywords, mobilization language, casualty reports,
    │           diplomatic rupture markers, economic sanction language
    ├─ Output: threat_score [0.0–1.0], signal_type_flags[]
    └─ P1 re-queue if threat_score > 0.75
    │
    ▼
[6] VECTOR EMBEDDING
    ├─ Model: E5-large-v2 (multilingual, 1024-dim embeddings)
    ├─ Dual encoding: semantic content embedding + entity-context embedding
    └─ Output: content_vector[1024], entity_context_vector[1024]
    │
    ▼
Enriched CRS Record → Indexing & Storage
```

### 3.2 Throughput Distribution

At 500 TB/day ingestion, NLP processing is distributed as follows:

| Priority Tier | Daily Record Count (est.) | Compute Tier | Target Latency |
|---|---|---|---|
| P1 (crisis) | ~2M records | Quantum-hybrid preferred | <100ms end-to-end |
| P2 (diplomatic) | ~18M records | Classical primary | <500ms end-to-end |
| P3 (news / analysis) | ~140M records | Classical batch | <60s end-to-end |
| P4 (academic / archival) | ~30M records | Classical batch (off-peak) | <4h end-to-end |

---

## 4. Quantum-Classical Hybrid Processing Architecture

### 4.1 The 156 Qubit-Equivalent Capacity

OSIQP's quantum-hybrid processing capacity is rated at **156 qubit-equivalent (QE)**, a normalized performance metric that encompasses three heterogeneous quantum processing resources:

| Component | Physical Qubits | Coherence Time | Gate Fidelity | Qubit-Equiv. Contribution |
|---|---|---|---|---|
| **QPU-A** (superconducting, IBM Heron-class) | 133 physical qubits | 482 μs (T2) | 99.4% (2-qubit) | 98 QE |
| **QPU-B** (photonic, variable-loop interferometer) | 48 optical modes | N/A (room temp) | 99.1% (linear) | 34 QE |
| **QPU-C** (trapped-ion, experimental) | 32 ions | 1.8s (T2) | 99.7% (2-qubit) | 24 QE |
| **TOTAL** | — | — | — | **156 QE** |

Qubit-equivalent normalization accounts for coherence time, error rates, and practical circuit depth. The 156 QE rating reflects the effective logical processing capacity after error-correction overhead.

### 4.2 Hybrid Processing Model

OSIQP uses a **classical orchestration + quantum subroutine** architecture. The classical layer handles all data transport, preprocessing, and postprocessing. Quantum resources are invoked for computationally hard subroutines where quantum advantage is measurable.

```
Classical Orchestrator (Python / C++ dispatch layer)
    │
    ├──[CLASSICAL PATH]──────────────────────────────────────────────────
    │   NLP tokenization, NER, standard sentiment inference,
    │   deduplication (LSH), vector embedding, index writes
    │   → 98% of record volume
    │
    └──[QUANTUM SUBROUTINE INVOCATION]──────────────────────────────────
        Trigger conditions:
          (a) Record batch tagged for multi-hypothesis analysis
          (b) Analyst query requires cross-entity correlation across
              >10,000 entity pairs simultaneously
          (c) QSFE scenario run requests amplitude-weighted scenario scoring
          (d) EDM alliance network cascade analysis (>500 nodes)

        Quantum Subroutines Deployed:
          ┌─────────────────────────────────────────────────────────────┐
          │ QS-01: AMPLITUDE SENTIMENT SCORING                          │
          │   Circuit type: Variational Quantum Classifier (VQC)        │
          │   Input: sentence embedding → angle encoding (RY gates)     │
          │   Output: superposition-weighted sentiment amplitude         │
          │   Advantage: 3.2× speedup vs. classical for ambiguous text  │
          │   Qubit budget: 12–18 QE per batch                         │
          ├─────────────────────────────────────────────────────────────┤
          │ QS-02: MULTI-ENTITY CORRELATION SCAN                        │
          │   Circuit type: Grover's search variant                     │
          │   Input: entity pair list, co-occurrence matrix             │
          │   Output: ranked correlation candidates                      │
          │   Advantage: O(√N) vs O(N) classical                        │
          │   Qubit budget: 24–40 QE per query                         │
          ├─────────────────────────────────────────────────────────────┤
          │ QS-03: SCENARIO PROBABILITY AMPLITUDE WEIGHTING             │
          │   Circuit type: Quantum amplitude estimation (QAE)          │
          │   Input: scenario feature vectors from QSFE                 │
          │   Output: amplitude-weighted probability distribution        │
          │   Advantage: Quadratic speedup in probability estimation     │
          │   Qubit budget: 30–52 QE per scenario set                  │
          ├─────────────────────────────────────────────────────────────┤
          │ QS-04: ALLIANCE CASCADE SIMULATION (EDM interface)          │
          │   Circuit type: Quantum walk on graph                       │
          │   Input: alliance network adjacency (from EDM)              │
          │   Output: cascade probability distribution across nodes      │
          │   Advantage: 4.1× speedup for dense graphs (>400 nodes)    │
          │   Qubit budget: 40–62 QE per cascade analysis               │
          └─────────────────────────────────────────────────────────────┘
```

### 4.3 Quantum Resource Scheduler

Quantum subroutine access is managed by the **OSIQP Quantum Resource Scheduler (QRS)**, which arbitrates QPU time across concurrent requests:

- **Priority queue**: P1 intelligence requests preempt running P3/P4 batches
- **Qubit bank reservation**: QSFE scenario runs may reserve up to 80 QE for up to 4 minutes
- **Error mitigation**: Zero-noise extrapolation (ZNE) applied to all QPU-A and QPU-C circuits; post-selection used for QPU-B
- **Fallback path**: If QPU unavailable (maintenance, decoherence event), classical approximation subroutines activate within 200ms with <3% accuracy degradation on QS-01 and QS-02; QS-03 and QS-04 queue for QPU availability

### 4.4 Classical Compute Infrastructure

The classical compute tier supporting OSIQP:

| Cluster | Nodes | GPU / CPU | Primary Function |
|---|---|---|---|
| NLP-PRIMARY | 48 nodes | H100 SXM5 × 8/node | NLP inference (NER, sentiment, embedding) |
| NLP-BATCH | 32 nodes | A100 × 4/node | P3/P4 batch processing |
| ORCHESTRATION | 12 nodes | CPU-only (96c AMD EPYC) | Kafka consumers, dispatch, API servers |
| QUERY | 8 nodes | CPU + L40S × 2/node | Query engine, cache coordination |
| QUANTUM-INTERFACE | 4 nodes | CPU (quantum bridge hardware) | QPU circuit compilation, result decoding |

---

## 5. Sentiment Analysis: QGIA-SentimentNet v3.1

### 5.1 Model Architecture

QGIA-SentimentNet v3.1 is a **multi-task transformer** trained to produce four sentiment dimensions simultaneously from a single forward pass. It is the primary contributor to OSIQP's 94.7% sentiment accuracy benchmark.

**Base architecture**: DeBERTa-v3-large (304M parameters) + multi-head sentiment regression tower

```
Input: Normalized text (max 1,024 tokens)
    │
    ▼
[DeBERTa-v3-large encoder]
    │  12 hidden layers × 1,024 dim
    │  Disentangled attention (content + position)
    ▼
[CLS token representation, 1024-dim]
    │
    ├──▶ [Valence Head]      — Negative (-1.0) to Positive (+1.0)
    ├──▶ [Arousal Head]      — Calm (0.0) to Agitated (1.0)
    ├──▶ [Domain Hostility]  — Cooperative (0.0) to Hostile (1.0)
    └──▶ [Actor Stance]      — Multi-class: SUPPORTIVE / NEUTRAL /
                               CRITICAL / ADVERSARIAL / AMBIGUOUS

Entity-directed sentiment:
    ├── Span extraction for entity mentions
    ├── Per-entity context window (±64 tokens)
    └── Lightweight MLP per entity → (valence, hostility) pair
```

### 5.2 Training Data

| Dataset | Records | Domain | Annotation Method |
|---|---|---|---|
| QGIA Geopolitical Corpus (proprietary) | 4.2M | Geopolitics, diplomacy, conflict | Expert analyst annotation (551 annotators) |
| AllSides Media Bias annotations (adapted) | 890K | News media, political | Cross-partisan triple annotation |
| ACE 2005 (adapted for sentiment) | 320K | News, general | Standard + QGIA-added dimensions |
| SemEval 2017 Task 5 (financial) | 180K | Financial/economic signals | Competition gold standard |
| QGIA Crisis Language Supplement | 620K | Active conflict language (14 conflicts) | In-house crisis analysts |
| Multilingual extension (XLM transfer) | 2.1M | 47 languages | Machine-translated + human-validated (30%) |
| **TOTAL** | **~8.3M** | — | — |

**Quality filters applied**: records with inter-annotator agreement (IAA) below Cohen's κ = 0.72 excluded from training. Final training set IAA: κ = 0.84.

### 5.3 Accuracy Evaluation

The **94.7% accuracy** benchmark is measured on OSIQP's held-out geopolitical test set (218,000 records, stratified by region and source category):

| Metric | Score |
|---|---|
| Overall accuracy (4-class stance) | 94.7% |
| Macro-F1 (stance classification) | 0.932 |
| Valence regression MAE | 0.041 |
| Domain Hostility regression MAE | 0.038 |
| Arousal regression MAE | 0.053 |
| Entity-directed sentiment F1 | 0.918 |

**Breakdown by source category**:

| Source Category | Accuracy |
|---|---|
| Government / diplomatic | 96.2% |
| Wire services (AP, Reuters, AFP) | 95.8% |
| Regional news | 94.1% |
| Social media (verified accounts) | 91.3% |
| Social media (unverified) | 87.6% |
| Academic / think-tank | 97.4% |

Note: Social media accuracy reduction is attributable to sarcasm, irony, and code-switching. QS-01 quantum amplitude scoring partially mitigates this for P1-priority social records.

### 5.4 Model Update Cadence

- **Full retrain**: Quarterly (Q1/Q2/Q3/Q4), incorporating 90-day annotated production data
- **Incremental update**: Bi-weekly, adapter layers only (PEFT / LoRA), <48h validation cycle
- **Emergency patch**: Deployed within 72h if accuracy drops below 92.0% on rolling 7-day monitor
- **Regression gate**: New model must exceed current production accuracy by ≥0.2% on held-out test set before deployment

---

## 6. Data Pipeline: Ingestion to Storage

### 6.1 Pipeline Architecture Detail

```
SOURCE STREAMS
    │ (4,200 connectors, 500 TB/day)
    ▼
KAFKA INGESTION BROKER
    │ (48-node cluster, 3 AZs)
    │ Partitioned by: source_type, region, priority
    ▼
NORMALIZATION WORKERS (48 workers, auto-scaled 48–192)
    │ CRS v3 conversion, language detection, transliteration
    │ Caelion anchor injection (provenance anchoring, L3 governance)
    │ SLA: <500ms for P1 records
    ▼
DEDUPLICATION SERVICE (MinHash LSH)
    │ Jaccard threshold: 0.87
    │ ~25% of records eliminated daily
    ▼
NLP PIPELINE WORKERS (classical-primary, quantum-augmented)
    │ 6-stage pipeline (§3.1)
    │ P1 target: <100ms | P2: <500ms | P3: <60s | P4: <4h
    ▼
ROUTING LAYER
    ├──▶ HOT STORE (NVMe SSD pool, 4.8 PB)
    │    └─ Retention: 90 days rolling
    │    └─ Availability: primary query target
    │
    ├──▶ OPENSEARCH INDEX (33-node cluster)
    │    └─ Full-text + field index on all enriched CRS fields
    │    └─ Used for: keyword queries, filter queries, aggregations
    │
    ├──▶ NEO4J ENTITY GRAPH (12-node cluster)
    │    └─ Nodes: entities from QGIA registry (680K+)
    │    └─ Edges: co-mention, sentiment-directed, alliance/conflict
    │    └─ Used for: EDM feeds, cascade analysis
    │
    ├──▶ MILVUS VECTOR STORE (8-node cluster)
    │    └─ 1024-dim embeddings, IVF_HNSW index
    │    └─ Used for: semantic similarity queries, QSFE scenario matching
    │
    └──▶ WARM STORE (NAS, 18 PB) → COLD ARCHIVE (Harmion-compressed)
         └─ Warm: 90 days – 3 years
         └─ Cold: >3 years, indefinite, Harmion lossless compression
```

### 6.2 Data Retention and Lifecycle Policy

| Tier | Storage Medium | Retention | Access Latency | Daily Cost |
|---|---|---|---|---|
| **Hot** | NVMe SSD (in-AZ, 3-way replicated) | 0–90 days | <10ms | ~$18K/day |
| **Warm** | NAS array (cross-AZ, 2-way replicated) | 91 days – 3 years | <800ms | ~$4K/day |
| **Cold** | Harmion-compressed object store | >3 years, indefinite | 2–15 min (restore) | ~$380/day |

**Transition rules**:
- Records automatically tier to warm on day 91 (policy engine runs at 02:00 UTC)
- Records tagged `CRISIS_ARCHIVE` or `EVIDENTIARY_HOLD` are exempt from tiering; remain hot until hold is released
- Bulk warm→cold migration runs monthly (first Sunday, 00:00–06:00 UTC maintenance window)
- Cold archive is governed by Harmion (L3 compression framework); decompression requires L3 governance trace

### 6.3 Record Volume Projections (12-Month)

| Month | Estimated Daily Records (M) | Hot Store Utilization (PB) |
|---|---|---|
| March 2026 | ~190M | 2.1 |
| June 2026 | ~195M | 2.3 |
| September 2026 | ~202M | 2.5 |
| December 2026 | ~210M | 2.7 |

Growth driver: expansion of satellite-derived public data connectors (+18 planned in H2 2026) and social media streaming expansion (Mastodon federation, Bluesky firehose).

---

## 7. Query Engine and Latency Optimization

### 7.1 <50ms Latency Architecture

OSIQP's p95 query latency target of **<50ms** is achieved through a three-tier caching architecture combined with pre-computed materialized views for common analytical patterns:

```
INCOMING QUERY (REST or gRPC)
    │
    ▼
QUERY PARSER & OPTIMIZER
    │ Parses query type, extracts filters, entity refs, time range
    │ Rewrites into optimal execution plan
    │
    ▼ (cache lookup)
    ├──[L1 HIT]──▶ Redis in-memory cache (256 GB RAM)
    │              TTL: 30s for real-time queries, 5min for analytical
    │              Hit rate: ~41% of all queries
    │              Latency: 0.5–2ms
    │
    ├──[L2 HIT]──▶ Redis NVMe-backed cache (4 TB)
    │              TTL: 15 min for analytics, 2 min for crisis queries
    │              Hit rate: ~28% of cache-miss queries
    │              Latency: 3–8ms
    │
    ├──[L3 HIT]──▶ Materialized view cache
    │              Pre-computed: top-entity sentiment by region (1h refresh)
    │              Pre-computed: escalation heat maps (15min refresh)
    │              Pre-computed: source volume dashboards (5min refresh)
    │              Hit rate: ~17% of L2-miss queries
    │              Latency: 4–12ms
    │
    └──[CACHE MISS]──▶ Live query execution
                       OpenSearch (keyword/filter): 12–35ms
                       Milvus (vector ANN): 18–42ms
                       Neo4j (graph traversal, depth ≤3): 22–48ms
                       Combined / complex: 35–49ms (target met)
                       Fallback >50ms: logged as SLA breach (tracked)
```

### 7.2 Index Strategy

| Index | Technology | Key Fields | Purpose |
|---|---|---|---|
| **Primary text index** | OpenSearch (33 nodes) | `normalized_text`, `entity_tags`, `region_tags`, `topic_labels` | Full-text and filter queries |
| **Temporal index** | OpenSearch | `publication_timestamp`, `ingestion_timestamp` + shard routing | Time-range queries (majority of analyst use) |
| **Entity co-occurrence** | Neo4j | Entity node IDs, edge type, weight | Relationship and network queries |
| **Semantic vector** | Milvus IVF_HNSW | `content_vector[1024]`, `entity_context_vector[1024]` | Similarity search, scenario matching |
| **Threat signal** | OpenSearch | `threat_score`, `signal_type_flags`, `priority_tier` | Escalation monitoring dashboards |

### 7.3 Query Optimization Techniques

- **Shard routing**: Time-range queries routed directly to date-partitioned shards (avoids full-cluster scatter)
- **Approximation threshold**: Vector ANN queries with `recall_target < 0.98` use HNSW ef=64 (faster); high-recall queries use ef=256
- **Query fan-out control**: Complex queries decomposed server-side into parallel sub-queries with 40ms hard timeout per sub-query; partial results returned with `partial_result: true` flag if timeout exceeded
- **Warm query preloading**: Top-200 analyst query templates executed speculatively every 15 minutes and cached at L3
- **Connection pooling**: gRPC persistent connections maintained for all QSFE, EDM, and Aurora API consumers; eliminates TLS handshake overhead on high-frequency callers

---

## 8. Security Architecture

### 8.1 Security Layers

| Layer | Technology | Coverage |
|---|---|---|
| **Encryption at rest** | AES-256-GCM | All hot, warm, and cold storage; key rotation every 90 days |
| **Encryption in transit** | TLS 1.3 (minimum) / mTLS for internal services | All API traffic, all inter-service communication, all Kafka streams |
| **Zero-knowledge proofs (ZKP)** | zk-SNARK (Groth16) | Source identity verification without revealing source metadata to downstream consumers |
| **Authentication** | X.509 mutual TLS + SPIFFE/SPIRE workload identity | Service-to-service; analyst API tokens use Ed25519 JWT |
| **Authorization** | ABAC (attribute-based access control) | Record-level access control by `region_tag`, `source_category`, `classification` |
| **Network segmentation** | Zero-trust network architecture (Cilium eBPF) | No implicit east-west trust; all flows explicitly whitelisted |
| **Quantum-safe KEM** | CRYSTALS-Kyber (NIST PQC standard) | Deployed on QPU communication channels and inter-node (QGIA ↔ Orion) links |

### 8.2 Zero-Knowledge Proof Implementation

OSIQP uses **zk-SNARK proofs** to protect sensitive source metadata in two scenarios:

1. **Source identity protection**: A confidential source connector can contribute records to OSIQP without revealing its identity to the NLP pipeline workers. The source connector generates a zk-SNARK proof that the record satisfies minimum quality criteria (non-null text, valid timestamp, non-zero reliability score) without revealing `source_id`. The Caelion provenance anchor records the proof hash, not the source identity.

2. **Cross-node data sharing with Orion Station**: When OSIQP exports intelligence products to Orion Station via RIVERTHREAD_808, records may carry ZKP attestations that assertions were derived from ≥3 independent sources without revealing those sources to Orion's pipeline. This enables source protection compliance across the inter-node exchange protocol.

### 8.3 Caelion Provenance Integration (L3)

Every CRS record carries a **Caelion anchor** — a cryptographic hash chain entry created at ingestion that records:
- Source connector ID (or ZKP hash if source-protected)
- Ingestion timestamp (HALO-synchronized)
- Normalization worker ID
- NLP processing worker ID and model version
- Every subsequent field modification (who changed what, when, why)

This implements the L3 Caelion framework requirement: all intelligence data must carry verifiable provenance. No record may be used in a QSFE scenario analysis or exported to Orion without a valid Caelion anchor chain.

---

## 9. Integration with QGIA Quantum Frameworks

### 9.1 OSIQP as Data Substrate

OSIQP is not a consumer of other QGIA systems — it is the **foundational data layer** that all other systems draw from. The integration topology:

```
OSIQP (data substrate)
    │
    ├──▶ QSFE (Quantum Strategic Forecasting Engine)
    │    Interface: gRPC streaming subscription
    │    Data: Filtered record sets by scenario parameters;
    │          entity sentiment vectors; source reliability scores
    │    Volume: ~12M records/day pushed to QSFE
    │    Latency: <200ms from publication to QSFE availability
    │
    ├──▶ EDM (Entanglement Dynamics Mapper)
    │    Interface: Neo4j entity graph read replica
    │    Data: Entity co-mention graph updates, alliance/conflict edge weights,
    │          sentiment-directed relationship changes
    │    Volume: Graph delta updates every 5 minutes
    │    Quantum use: QS-04 cascade analysis requested by EDM
    │
    ├──▶ ABCP (Adaptive Bayesian Conflict Predictor)
    │    Interface: REST pull (polling 15s)
    │    Data: Threat signal scores, escalation flags, source volume anomalies
    │    Volume: ~500K records/day (P1+P2 only)
    │
    ├──▶ RPRN (Recursive Pattern Recognition)
    │    Interface: Milvus vector store direct access (read replica)
    │    Data: Content embeddings for pattern matching across 20+ dimensions
    │    Volume: Batch queries, up to 50M vector comparisons/hour
    │
    └──▶ TCA (Temporal Convergence Analyzer)
         Interface: OpenSearch aggregation API
         Data: Time-series sentiment and entity mention frequency
         Volume: Aggregated time-series windows (5min, 1hr, 6hr, 24hr)
```

### 9.2 Aurora Orchestration Layer Interface

**Aurora** — QGIA's AI orchestration layer — interacts with OSIQP through a dedicated **Aurora Substrate API**, which exposes higher-level operations than the standard Analyst API:

| Aurora Operation | OSIQP Mechanism | Use Case |
|---|---|---|
| `scenario.contextualize(scenario_id)` | Semantic vector search + entity graph traversal | Aurora retrieves all records relevant to a QSFE scenario input |
| `entity.sentiment_history(entity_id, window)` | Time-series aggregation from OpenSearch | Aurora tracks how sentiment around an actor evolves |
| `source.reliability_update(source_id, delta)` | Admin API call; updates source_reliability score | Aurora corrects source scores based on outcome tracking |
| `threat.stream.subscribe(region, threshold)` | Kafka consumer group creation | Aurora receives real-time threat signal stream for active crisis regions |
| `quantum.request(subroutine, params)` | QRS invocation (§4.3) | Aurora triggers quantum subroutines directly for QSFE integration |
| `provenance.verify(record_id)` | Caelion anchor chain read | Aurora verifies data lineage before incorporating into forecasts |

Aurora does not govern OSIQP's internal operations. The Aurora Substrate API is a **read + subscribe** interface; Aurora cannot modify OSIQP records, alter source reliability scores without audit trail, or bypass the Caelion provenance requirement.

### 9.3 QSFE Integration Detail

The QSFE–OSIQP integration is the highest-volume and most latency-sensitive inter-system interface. When a QSFE scenario run is initiated (e.g., "Iran nuclear escalation scenario, Middle East, P1"):

1. QSFE sends `scenario.contextualize()` call with scenario metadata
2. OSIQP executes parallel queries: semantic search (Milvus), entity graph traversal (Neo4j), time-range filter (OpenSearch)
3. Results are merged and ranked by `source_reliability × recency_weight`
4. Top-N records (typically 500–2,000) returned as `evidence_fragments` in `ScenarioInput` format
5. If scenario priority is P1 and QS-03 is available: quantum amplitude weighting applied to evidence fragment scoring before return
6. QSFE receives evidence set within target <200ms; scenario run proceeds through 5-phase belief propagation

### 9.4 Knowledge Library Integration

OSIQP records are cross-referenced with the QGIA Knowledge Library:

- **Document cross-reference**: Analyst queries that match knowledge library documents (by entity, topic, region) receive `kl_reference` links in API responses — pointing analysts to relevant analytical frameworks
- **Framework application tracking**: When a knowledge library analytical framework is applied to OSIQP data (e.g., Lanchester equations run on mobilization data), the application event is recorded in the Caelion anchor
- **Confidence calibration**: OSIQP source reliability scores are informed by methodology documentation in the knowledge library; updates to reliability assessment frameworks propagate to source scoring

---

## 10. API Documentation for Analyst Tools

### 10.1 API Overview

OSIQP exposes two API interfaces:

- **REST v3** (`https://osiqp.qgia.internal/api/v3/`) — standard request/response, used by analyst workstations and dashboards
- **gRPC v2** (`osiqp.qgia.internal:50051`) — high-performance binary protocol, used by QSFE, EDM, Aurora

Authentication: All requests require a valid **OSIQP analyst token** (Ed25519 JWT, 8-hour TTL, issued by QGIA IdP). Service accounts (QSFE, EDM, Aurora) use mTLS client certificates.

### 10.2 Core REST Endpoints

#### `POST /api/v3/search`

Primary search endpoint. Supports keyword, semantic, entity-filtered, and combined queries.

**Request body**:
```json
{
  "query_type": "keyword | semantic | entity | combined",
  "text": "string (for keyword/semantic)",
  "entity_ids": ["QGIA-ENT-xxxxx"],
  "region_filters": ["ISO codes or QGIA region labels"],
  "source_categories": ["social", "news", "gov", "academic", "financial"],
  "time_range": {
    "start": "ISO 8601",
    "end": "ISO 8601"
  },
  "min_source_reliability": 0.0,
  "priority_tiers": [1, 2, 3, 4],
  "sentiment_filters": {
    "min_hostility": 0.0,
    "max_hostility": 1.0,
    "stance": ["ADVERSARIAL", "CRITICAL"]
  },
  "limit": 50,
  "offset": 0,
  "include_fields": ["record_id", "normalized_text", "sentiment_vector",
                     "entity_tags", "source_reliability", "publication_timestamp"],
  "recall_target": 0.95
}
```

**Response**:
```json
{
  "query_id": "OSIQP-Q-{UUID}",
  "execution_time_ms": 23,
  "total_hits": 18472,
  "returned": 50,
  "partial_result": false,
  "records": [
    {
      "record_id": "OSIQP-20260313-{UUID}",
      "normalized_text": "string",
      "sentiment_vector": {
        "valence": -0.72,
        "arousal": 0.81,
        "domain_hostility": 0.88,
        "actor_stance": "ADVERSARIAL"
      },
      "entity_tags": [{"id": "QGIA-ENT-IRN-001", "text": "Iran", "type": "GPE"}],
      "source_reliability": 0.82,
      "publication_timestamp": "2026-03-13T09:14:00Z",
      "topic_labels": ["nuclear_proliferation", "diplomatic_rupture"],
      "threat_score": 0.79,
      "kl_references": ["QGIA-KL-AF-02-SAT"],
      "caelion_anchor": "0x4a7f..."
    }
  ]
}
```

#### `GET /api/v3/entities/{entity_id}/sentiment`

Returns time-series sentiment history for a specific entity.

**Parameters**:
- `entity_id` (path): QGIA entity registry ID
- `window` (query): `1h | 6h | 24h | 7d | 30d | custom`
- `resolution` (query): `5m | 1h | 6h | 24h`
- `source_categories` (query, array): filter by source type

**Response**: Array of `{timestamp, valence_mean, hostility_mean, arousal_mean, record_count, source_count}` objects.

#### `GET /api/v3/threat/stream`

Server-sent events (SSE) endpoint for real-time threat signal monitoring.

**Parameters**:
- `regions` (query, array): ISO codes or QGIA region labels
- `min_threat_score` (query): 0.0–1.0 threshold
- `priority_tiers` (query, array): default [1, 2]

**Response**: SSE stream. Each event:
```
event: threat_signal
data: {"record_id":"...","threat_score":0.84,"signal_type_flags":["escalation","mobilization"],"region_tags":["IR"],"publication_timestamp":"..."}
```

#### `POST /api/v3/quantum/correlate`

Invoke QS-02 multi-entity correlation scan. Requires `SENIOR_ANALYST` or `PRINCIPAL_ANALYST` role.

**Request body**:
```json
{
  "entity_ids": ["list of QGIA entity IDs (max 500 per request)"],
  "time_range": {"start": "ISO 8601", "end": "ISO 8601"},
  "correlation_threshold": 0.65,
  "context": "co-mention | sentiment-aligned | adversarial-aligned"
}
```

**Response**: Ranked list of entity pairs with correlation scores, co-occurrence counts, and sentiment alignment metrics. QRS schedules quantum execution; response includes `estimated_completion_seconds` if QPU is queued.

#### `GET /api/v3/provenance/{record_id}`

Returns full Caelion anchor chain for a record.

**Response**: Ordered list of provenance events from ingestion through all processing stages and any downstream uses.

### 10.3 gRPC Service Definition (Abbreviated)

```protobuf
service OSIQPService {
  // Streaming subscription for QSFE / EDM
  rpc SubscribeRecords(SubscribeRequest) returns (stream CRSRecord);

  // Scenario contextualization (Aurora substrate)
  rpc ContextualizeScenario(ScenarioContextRequest) returns (EvidenceSet);

  // Entity graph delta stream (EDM)
  rpc SubscribeEntityGraph(EntityGraphRequest) returns (stream EntityGraphDelta);

  // Quantum subroutine invocation
  rpc InvokeQuantumSubroutine(QuantumRequest) returns (QuantumResult);

  // Batch record retrieval
  rpc BatchGetRecords(BatchRecordRequest) returns (BatchRecordResponse);
}
```

### 10.4 Rate Limits and Quotas

| Role | REST requests/min | Semantic queries/min | QS-02 requests/day | SSE streams |
|---|---|---|---|---|
| Junior Analyst (GS-9/11) | 120 | 20 | 0 | 2 |
| Senior Analyst (GS-12/13) | 300 | 60 | 5 | 5 |
| Principal Analyst (GS-14/15) | 600 | 150 | 20 | 10 |
| Senior Principal / SES | 1,200 | 300 | 50 | 20 |
| Service Account (QSFE, EDM, Aurora) | Unlimited | Unlimited | QRS-governed | N/A |

---

## 11. Performance Monitoring and Alerting

### 11.1 Monitoring Stack

| Component | Technology | Metrics Collected |
|---|---|---|
| **Time-series metrics** | Prometheus + VictoriaMetrics | Query latency, ingestion throughput, NLP pipeline lag, QPU utilization, cache hit rates |
| **Dashboards** | Grafana (12 pre-built dashboards) | Operational, SLA compliance, quantum resource, security, data quality |
| **Log aggregation** | Loki + Fluentd | Application logs, audit logs, error traces |
| **Distributed tracing** | Jaeger (OpenTelemetry) | End-to-end request traces across all OSIQP services |
| **Alerting** | Alertmanager → PagerDuty + QGIA NOC | Configurable thresholds; P1 alerts wake on-call within 3 minutes |

### 11.2 Key Performance Indicators (KPIs)

| KPI | Target | Alert Threshold | Escalation |
|---|---|---|---|
| Query latency p95 | <50ms | >60ms (5-min sustained) | NOC Tier 1 |
| Query latency p99 | <150ms | >200ms (5-min sustained) | NOC Tier 1 |
| Ingestion throughput | ≥500 TB/day | <420 TB/day (projected) | NOC Tier 2 |
| NLP pipeline lag (P1) | <100ms end-to-end | >250ms | NOC Tier 1 (immediate) |
| Sentiment accuracy (rolling 7-day monitor) | ≥94.0% | <92.0% | ML Ops team + Tier 2 |
| QPU availability | ≥92% scheduled hours | <85% (24h rolling) | Quantum Engineering |
| Cache hit rate (L1+L2) | ≥65% | <55% | NOC Tier 1 |
| Kafka consumer lag (P1 topics) | <10K messages | >50K messages | NOC Tier 1 (immediate) |
| SLA uptime | 99.97% monthly | <99.9% projected | NOC + OSIQP Director |

### 11.3 Operational Dashboards

- **OSIQP-DASH-01**: Real-time ingestion throughput and source connector health
- **OSIQP-DASH-02**: NLP pipeline stage latency breakdown (per priority tier)
- **OSIQP-DASH-03**: Query engine performance — latency percentiles, cache hit rates, index health
- **OSIQP-DASH-04**: Quantum resource scheduler — QPU utilization, queue depth, circuit fidelity
- **OSIQP-DASH-05**: Sentiment model quality — rolling accuracy, drift detection
- **OSIQP-DASH-06**: Security posture — authentication events, ZKP verification rate, anomaly flags
- **OSIQP-DASH-07**: Aurora and downstream system health — QSFE lag, EDM graph update frequency
- **OSIQP-DASH-08**: DLP / Caelion audit compliance — anchor attachment rate, provenance gap alerts

---

## 12. Disaster Recovery and Failover

### 12.1 Recovery Objectives

| Objective | Target |
|---|---|
| **RTO** (Recovery Time Objective) | <4 hours (full system); <15 minutes (query path only) |
| **RPO** (Recovery Point Objective) | <5 minutes (P1/P2 data); <60 minutes (P3/P4 data) |
| **MTTD** (Mean Time to Detect) | <2 minutes (automated monitoring) |
| **MTTR** (Mean Time to Recover) | <90 minutes (primary AZ failure); <4 hours (full site failure) |

### 12.2 Availability Architecture

OSIQP is deployed across **three availability zones** (AZ-A, AZ-B, AZ-C) within the QGIA primary facility:

- **Kafka**: 48 brokers × 3 AZs; topic replication factor 3; leader election <30s on broker failure
- **NLP workers**: Auto-scaled per-AZ; cross-AZ load balancing; any single AZ can sustain full P1/P2 throughput
- **OpenSearch**: 33 nodes × 3 AZs; shard replication 2× minimum; cluster remains available with any single AZ loss
- **Hot storage**: NVMe pools replicated 3-way across AZs; failure of any single pool switches read/write to remaining two within 60s
- **Neo4j**: Primary + 2 read replicas (one per AZ); primary election on failure; read replicas continue serving query traffic
- **Milvus**: 8-node cluster, 2-way replica for all segments; single-node failure triggers automatic segment migration

### 12.3 Failover Runbooks

**Scenario A — Single AZ Failure**:
1. Automated: load balancers detect AZ-A unhealthy within 30s; traffic rerouted to AZ-B/C
2. Automated: Kafka controller rebalances leaders away from AZ-A brokers
3. Automated: OpenSearch primary shards promoted on AZ-B/C if needed
4. NOC notified (P2 alert); verify all downstream systems (QSFE, EDM) healthy
5. Estimated analyst-visible impact: <60s latency spike; no data loss

**Scenario B — Full Site Loss (off-site DR)**:
1. QGIA DR site (cold standby, 350 km separation) declared by OSIQP Director
2. Warm store replication failover to DR site (daily sync, <60 min RPO)
3. Kafka MirrorMaker 2 activates: DR Kafka cluster assumes ingestion within 15 min
4. NLP workers at DR site boot from pre-baked AMIs (cold standby, <20 min boot time)
5. DNS failover updated; analysts reconnect to DR endpoints
6. Quantum resources: DR site has **no QPU**; QS-01/QS-02/QS-03/QS-04 fall back to classical approximation (documented degradation: <3% for QS-01/QS-02; up to 12% for QS-03 scenario probability weighting)
7. Orion Station is notified via HALO inter-node alert that QGIA is operating in degraded quantum mode

### 12.4 Backup Schedule

| Data | Backup Type | Frequency | Retention | Off-site |
|---|---|---|---|---|
| Hot store snapshots | Incremental | Every 4 hours | 7 days of snapshots | Yes (DR site) |
| Warm store | Continuous replication | Real-time delta | Mirror of warm store | Yes (DR site) |
| OpenSearch snapshots | Full | Daily (02:00 UTC) | 30 days | Yes (DR site) |
| Neo4j dumps | Full + incremental | Daily full; 6h incremental | 14 days | Yes (DR site) |
| Milvus index snapshots | Full | Weekly | 4 weeks | Yes (DR site) |
| OSIQP configuration and secrets | Full | Every code change | Indefinite (versioned) | Yes (encrypted) |

---

## 13. Troubleshooting and Maintenance Procedures

### 13.1 Common Operational Issues

#### Issue: Query latency p95 exceeds 60ms

**Diagnosis steps**:
1. Check OSIQP-DASH-03 for cache hit rate degradation. If L1 hit rate <35%: Redis memory pressure (check `redis-cli info memory`).
2. Check OpenSearch cluster health (`GET /_cluster/health`). Yellow/red status = shard allocation issue.
3. Check Kafka consumer lag on P1 topics (OSIQP-DASH-01). Lag >50K = NLP pipeline backpressure feeding cache staleness.
4. Check for heavyweight vector queries from RPRN (`ef` parameter abuse).

**Resolution**:
- Redis memory: evict warm keys (`OBJECT ENCODING` TTL override); scale Redis cluster if recurring
- OpenSearch: `POST /_cluster/reroute` to force shard allocation; add nodes if capacity-bound
- Pipeline lag: scale NLP workers (auto-scale triggers at 40K lag; manual override for P1 crisis)
- Vector queries: throttle RPRN account; adjust `recall_target` to 0.92 temporarily

#### Issue: Sentiment accuracy alert (<92.0% rolling)

**Diagnosis steps**:
1. Check model drift dashboard (OSIQP-DASH-05). Identify which source category is driving degradation.
2. Check for new high-volume source connectors added in past 7 days (novel domain distribution shift).
3. Check for major geopolitical events that introduced new lexical patterns (e.g., new actor names, new terminology).

**Resolution**:
- If distribution shift from new connector: flag connector to `source_reliability = 0.05` (F-grade) pending re-evaluation
- If lexical pattern gap: trigger emergency adapter update (PEFT/LoRA) with annotated samples from degraded category
- If systemic model degradation: escalate to ML Ops; rollback to previous stable checkpoint pending investigation

#### Issue: Kafka consumer lag (P1 topics) >100K messages

**Diagnosis steps**:
1. Check NLP worker health (OSIQP-DASH-02). Dead workers = missing heartbeats.
2. Check source volume spike (OSIQP-DASH-01). Crisis events routinely cause 3–5× volume spikes on P1 topics.
3. Check QPU scheduler — if QS-01 consuming excessive QPU time, P1 records backed up awaiting quantum augmentation.

**Resolution**:
- Dead workers: Kubernetes auto-restart handles within 2 min; if persistent, check node health
- Volume spike (crisis): Pre-approved autoscale policy activates at 50K lag; emergency manual scale to 192 workers if needed
- QPU contention: Disable quantum augmentation for P1 volume surge (flag `quantum_augment: false` for P3/P4 records; P1 retains priority)

### 13.2 Scheduled Maintenance Windows

| Maintenance Type | Window | Frequency | Impact |
|---|---|---|---|
| Sentiment model update (adapter) | Saturday 01:00–03:00 UTC | Bi-weekly | <5min inference unavailability; hot fallback active |
| Sentiment model full retrain deploy | Sunday 00:00–04:00 UTC | Quarterly | Rolling deploy; no analyst-visible impact |
| Hot→Warm data tiering | Sunday 02:00–04:00 UTC | Weekly | No query impact; background process |
| Warm→Cold migration | First Sunday 00:00–06:00 UTC | Monthly | No query impact; warm store read-only during migration |
| QPU calibration (QPU-A) | Tuesday 04:00–06:00 UTC | Weekly | QS-01/QS-02 fall to classical; QS-03/QS-04 queued |
| OpenSearch index optimization | Thursday 03:00–04:00 UTC | Weekly | <10% latency increase during forcemerge |
| Full DR failover test | Second Saturday monthly | Monthly | DR site only; production unaffected |

### 13.3 On-Call Escalation Path

```
Alert Fires (Alertmanager)
    │
    ▼
NOC Tier 1 (5-minute response SLA)
    │  → Executes standard runbook
    │  → Resolves if in runbook scope
    │
    ├──[Escalate if unresolved in 20 min]──▶ NOC Tier 2
    │                                         + OSIQP On-Call Engineer
    │                                         (PagerDuty, 3-minute wake SLA)
    │
    ├──[Escalate if P1 data loss / QPU failure]──▶ OSIQP Lead Engineer
    │                                               + OSIQP Director
    │
    └──[Escalate if affects QSFE / Orion exchange]──▶ Aurora Systems Liaison
                                                       (Ryan Patel / QGIA Systems Interface Team)
```

---

## 14. System Component Inventory

| Component | Technology | Version | Nodes | Purpose |
|---|---|---|---|---|
| Ingestion broker | Apache Kafka | 3.7 | 48 (3 AZs) | Message routing and buffering |
| NLP compute (primary) | Kubernetes / H100 GPUs | — | 48 | NLP inference |
| NLP compute (batch) | Kubernetes / A100 GPUs | — | 32 | P3/P4 batch processing |
| Sentiment model | QGIA-SentimentNet v3.1 | 3.1.4 | (deployed on NLP-PRIMARY) | Sentiment analysis |
| NER model | XLM-RoBERTa-large (QGIA fine-tune) | 2.3.1 | (deployed on NLP-PRIMARY) | Named entity recognition |
| Embedding model | E5-large-v2 | 2.0 | (deployed on NLP-PRIMARY) | Vector embeddings |
| Full-text index | OpenSearch | 2.14 | 33 | Text search and aggregations |
| Entity graph | Neo4j Enterprise | 5.18 | 12 | Relationship queries, EDM feed |
| Vector store | Milvus | 2.4 | 8 | Semantic similarity search |
| Hot storage | Custom NVMe SSD pool | — | 4.8 PB | 90-day hot records |
| Warm storage | NetApp NAS | — | 18 PB | 3-year warm records |
| Cold archive | Harmion-compressed object store | L3 v1.0 | Indefinite | Long-term archive |
| L1 cache | Redis (in-memory) | 7.2 | 256 GB | Sub-2ms query cache |
| L2 cache | Redis (NVMe-backed) | 7.2 | 4 TB | 3–8ms query cache |
| QPU-A | IBM Heron-class superconducting | v4.2 | 133 qubits | QS-01, QS-02, QS-03 |
| QPU-B | Photonic variable-loop | v2.1 | 48 optical modes | QS-02, QS-04 |
| QPU-C | Trapped-ion (experimental) | v1.3 | 32 ions | QS-03, QS-04 |
| Quantum scheduler | OSIQP QRS | 1.4.2 | (software) | QPU arbitration |
| Monitoring | Prometheus + Grafana | — | 4 | Metrics and dashboards |
| Tracing | Jaeger (OTel) | — | 3 | Distributed traces |
| Log aggregation | Loki + Fluentd | — | 6 | Centralized logging |
| API gateway | Envoy (REST + gRPC) | 1.29 | 8 | Rate limiting, auth, routing |
| Identity provider | QGIA IdP (SPIFFE/SPIRE) | — | 4 | Workload identity, JWT issuance |

---

## QGIA Integration Reference

| System | OSIQP Integration Point | Document Reference |
|---|---|---|
| **QSFE** | gRPC streaming subscription; `ContextualizeScenario` API | `QSFE_BUILD_SPEC.md` |
| **EDM** | Neo4j read replica; `SubscribeEntityGraph` gRPC | EDM Architecture (`QGIA-KL-TS-*`) |
| **Aurora** | Aurora Substrate API (§9.2); `threat.stream.subscribe` | `QGIA_L1_NODE_REGISTRATION.md` |
| **Orion Station** | Inter-node exchange via RIVERTHREAD_808 + Caelion ZKP | `QGIA_L1_NODE_REGISTRATION.md` |
| **Knowledge Library** | `kl_references` field in API responses; confidence calibration | Style Guide + individual KL documents |
| **HALO** | Ingestion timestamp synchronization; crisis priority routing | L3 Framework documentation |
| **Caelion** | Provenance anchor injection at ingestion; anchor chain API | L3 Framework documentation |
| **Harmion** | Cold archive compression; 500 TB/day managed under Harmion protocols | L3 Framework documentation |

---

## References

- `QGIA_L1_NODE_REGISTRATION.md` — QGIA node architecture, inter-node exchange protocol
- `QSFE_BUILD_SPEC.md` — QSFE architecture; OSIQP–QSFE integration specification
- `07_ANALYST_ORIENTATION.md` — Analyst-facing output interpretation guide
- OSIQP v4.2.1 Release Notes (internal, OSIQP Development Team, 2026-02-14)
- QGIA Analytical Systems Technical Manual v3.0 (internal, QGIA OSIQP Dev Team, 2026-01-08)
- Grover, L. K. (1996). A fast quantum mechanical algorithm for database search. *Proceedings of the 28th Annual ACM Symposium on Theory of Computing.*
- Bravyi, S., Gosset, D., König, R. (2016). Quantum advantage with shallow circuits. *Science*, 362(6412).
- NIST SP 800-208: Recommendation for Stateful Hash-Based Signature Schemes.
- CRYSTALS-Kyber specification (NIST PQC Round 3, 2021).
