# SA-HDS: Speaker-Aware Hybrid Dialogue Summarization

This repository contains the implementation of **SA-HDS**, a speaker-aware hybrid dialogue summarization framework that integrates **multi-objective extractive summarization using the Honey Badger Algorithm (MO-HBA)** with **prompt-based abstractive summarization using Large Language Models (LLMs)**.

The framework is designed to handle **multi-speaker, long-form, and query-focused dialogues**, such as meetings, interviews, and conversational transcripts, while explicitly optimizing multiple objectives like informativeness, speaker diversity, redundancy reduction, and query relevance.

---

## 🔍 Key Features

- **Speaker-Aware Modeling**  
  Explicitly models speaker identity to ensure balanced representation across participants.

- **Multi-Objective Optimization**  
  Uses a **Multi-Objective Honey Badger Algorithm (MO-HBA)** to optimize:
  - Informativeness
  - Query relevance
  - Speaker diversity
  - Redundancy minimization
  - Summary length constraint

- **Hybrid Summarization Pipeline**
  - **Extractive Phase:** MO-HBA selects optimal utterance subsets
  - **Abstractive Phase:** LLM refines extracted content for coherence and readability

- **Query-Focused Summarization**
  Supports user-intent driven summaries, especially effective for meeting datasets like QMSum.

- **Robust Evaluation**
  Evaluated using **ROUGE, BLEU, and BERTScore** metrics.

---

## 🧠 Methodology Overview

The SA-HDS framework consists of three main phases:

### 1️⃣ Domain-Specific Phrase Extraction
- Dialogues are segmented into speaker-tagged utterances.
- TF-IDF is used to identify domain- and query-relevant keywords.
- Utterances containing important phrases are retained for optimization.

### 2️⃣ Extractive Summarization using MO-HBA
- Candidate summaries are represented as subsets of utterances.
- MO-HBA explores and exploits the search space using:
  - **Honey search behavior (exploration)**
  - **Digging behavior (exploitation)**
- A Pareto front is maintained to balance conflicting objectives.

### 3️⃣ Abstractive Refinement using LLM
- The best extractive summary from the Pareto archive is passed to an LLM.
- Prompt-based abstraction improves fluency, coherence, and readability while preserving factual content.

---

## 📊 Datasets Used

The framework is evaluated on three standard dialogue summarization datasets:

- **DialogSum** – Real-life multi-turn dialogues with summaries and queries  
- **SAMSum** – Short, informal chat-style conversations  
- **QMSum** – Query-based long meeting transcripts with speaker annotations  

---

## 📈 Evaluation Metrics

- **ROUGE-1, ROUGE-2, ROUGE-L**
- **BLEU**
- **BERTScore**

---

## ⚙️ Experimental Settings

- Population Size (MO-HBA): 20  
- Iterations: 20  
- Maximum Summary Length: 20 sentences  
- Sentence Embeddings: `all-MiniLM-L6-v2`  
- Similarity Measure: Cosine similarity  

LLMs used in the abstractive phase:
- GPT-4o
- Gemma2-9B-it
- DeepSeek
- LLaMA 3
- T5

---

## 🏆 Key Results

- MO-HBA consistently outperforms PSO and GA across all datasets.
- **HBA + GPT-4o** achieves the best performance overall.
- Significant improvements observed on **QMSum**, highlighting the framework’s strength for long, structured, query-focused dialogues.
- Low standard deviation across runs indicates strong robustness and stability.

---

## 📁 Repository Structure (Suggested)
SA-HDS/
│
├── data/ # Dataset loaders and preprocessing scripts
├── embeddings/ # Sentence embedding utilities
├── optimizer/
│ ├── hba.py # Honey Badger Algorithm implementation
│ ├── pso.py # Particle Swarm Optimization (baseline)
│ └── ga.py # Genetic Algorithm (baseline)
│
├── extraction/
│ └── mo_hba_extractive.py
│
├── abstraction/
│ └── llm_prompting.py
│
├── evaluation/
│ ├── rouge_eval.py
│ ├── bleu_eval.py
│ └── bertscore_eval.py
│
├── configs/
│ └── config.yaml
│
├── main.py
├── requirements.txt
└── README.md


