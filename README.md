# Evaluating Follow-up Question Generation Strategies for Complex Multi-hop Question Answering

An experimental study of follow-up question generation and iterative retrieval strategies for improving evidence retrieval in complex multi-hop question answering.

## Overview

Complex multi-hop questions often require combining information from multiple documents before an answer can be produced. This project investigates whether generating targeted follow-up questions can help identify missing information and refine retrieval during the QA process.

The study systematically compares different follow-up question generation and retrieval refinement strategies under the same datasets, retrieval pipeline, language model, and evaluation framework.

## Research Questions

The study investigates:

1. How do iterative follow-up question generation strategies affect retrieval performance?
2. How do different follow-up question generation and retrieval strategies compare in retrieval and downstream QA performance?
3. How do human evaluations of follow-up question quality complement quantitative retrieval and QA metrics?

## Methodology

### Datasets

Experiments were conducted on:

* **2WikiMultihopQA**
* **MuSiQue**

The first 500 queries from the development split of each dataset were used for the experiments.

### Follow-up Question Generation Strategies

Four strategies were evaluated:

* **Baseline**: generates a follow-up question directly from the original query
* **Decomposition**: generates questions targeting different aspects of the query
* **Yes/No**: uses binary questions to validate assumptions
* **Iterative**: identifies missing information from intermediate answers and generates follow-up questions across multiple steps

Three retrieval configurations were also evaluated:

* **Iterative**
* **Iterative Pool**
* **Iterative Pool + Rerank**

The iterative variants progressively collect and refine evidence before final answer generation.

### Experimental Pipeline

```text
Input Question
      ↓
BM25 Top-100 Evidence Pool
(Pre-retrieved Evidence Pool)
      ↓
Follow-up Question Generation
(Baseline / Decomposition / Yes-No / Iterative)
      ↓
Generated Follow-up Question
      ↓
Cross-Encoder Reranking
(Top-5 Documents)
      ↓
Retrieval Configuration
(Iterative / Iterative Pool / Iterative Pool + Rerank)
      ↓
Answer Generation
      ↓
Evaluation
(Recall@5 / EM / F1 / Human Evaluation)
```

The experiments used **Llama 3.2 3B** in a zero-shot setting for both follow-up question generation and answer generation. BM25 was used for initial retrieval and `ms-marco-MiniLM-L12-v2` for cross-encoder reranking. The pipeline was implemented in Python and executed using Jupyter and Kaggle Notebooks.

For iterative strategies, follow-up questions were generated from intermediate answers to progressively refine the information needed to answer the original question. Evidence across iterations was evaluated using **Iterative, Iterative Pool, and Iterative Pool + Rerank** configurations.

## Evaluation

Performance was evaluated using:

* **Recall@5** for retrieval coverage
* **Exact Match (EM)** for answer correctness
* **F1** for token-level answer overlap
* **Human evaluation** of fluency, relevance, and usefulness

The human evaluation used 50 queries from 2WikiMultihopQA and three annotators.

## Key Findings

### 1. Iterative retrieval improved retrieval coverage

Iterative retrieval approaches generally achieved stronger Recall@5 than the simpler follow-up question strategies.

On **2WikiMultihopQA**, Iterative Pool achieved the highest Recall@5 of **0.646**, compared with **0.390** for the Baseline.

On **MuSiQue**, Iterative Pool achieved the highest Recall@5 of **0.508**.

### 2. Better retrieval did not always mean better answers

Improving retrieval coverage did not consistently lead to better downstream QA performance.

On 2WikiMultihopQA, Iterative Pool achieved the strongest overall QA performance with **EM 0.278** and **F1 0.2854**.

On MuSiQue, however, **Iterative Pool + Rerank** performed best for QA, with **EM 0.178** and **F1 0.1855**, despite Iterative Pool having higher retrieval coverage. This suggests that evidence selection can matter as much as evidence quantity.

### 3. More retrieval iterations were not always better

Increasing retrieval depth consistently improved Recall@5, but downstream QA performance did not improve monotonically. The strongest downstream performance in the iteration-depth experiment occurred at 7 steps, after which performance declined slightly despite continued retrieval improvements.

This highlights a trade-off between **evidence coverage, evidence quality, and computational cost**.

### 4. Human evaluation told a different story

Human evaluation produced a different pattern from the quantitative results. Baseline-generated questions were rated higher than Iterative questions across all three dimensions:

| Strategy  | Fluency | Relevance | Usefulness |
| --------- | ------: | --------: | ---------: |
| Baseline  |    4.84 |      3.02 |       2.45 |
| Iterative |    3.64 |      2.31 |       2.18 |

Inter-annotator agreement was substantial for fluency (**Fleiss' κ = 0.7846**) and moderate for relevance (**0.4743**) and usefulness (**0.4623**).

## Main Takeaway

The results show that **retrieval effectiveness and perceived question quality do not always align**.

Iterative strategies can improve evidence coverage, but additional evidence does not automatically produce better answers. Evidence selection, retrieval depth, dataset characteristics, and the quality of generated follow-up questions all influence downstream QA performance.

## Repository Structure

```text
├── 2wikimultihopqa/
├── musique/
├── Qualitative evaluation/
├── README.md
└── .gitignore
```

The notebooks contain the experimental implementations, retrieval and QA evaluations, and qualitative evaluation work.

## Thesis

**Title:** Evaluating Follow-up Question Generation Strategies for Complex Multi-hop Question Answering

**Programme:** MSc Data Science, Statistics and Decision Analysis
**Institution:** Stockholm University
**Year:** 2026

Industry thesis conducted in collaboration with **Accenture**.

