# NTUGPT: LLM-Powered Campus Chatbot with Advanced RAG

> This repository contains the official LINE Bot implementation for my Master's Thesis: **"Revolutionizing Campus Conversation: LLM-Powered Chatbot with Retrieval-Augmented Generation"** (Data Science Degree Program, National Taiwan University, 2024).
> 🎓 **Read the full thesis paper here:** [NTU Academic Repository (PDF)](https://tdr.lib.ntu.edu.tw/jspui/retrieve/23e76241-ebae-4ce4-93a7-9f02a9d20adf/ntu-112-2.pdf)

---

## 🌟 Project Overview

**NTUGPT** is an end-to-end, production-ready campus Retrieval-Augmented Generation (RAG) system deployed as a LINE Bot. It answers complex, domain-specific questions about university regulations, administrative processes, and campus life with extreme precision, addressing the hallucination challenges of general LLMs.

### 📸 Demo Preview

| User Interface (LINE Bot) | Ingestion & Retrieval Flow |
| --- | --- |
| *[Add a screenshot of your LINE Bot chatting here]* | *[Add a system diagram or architecture flowchart here]* |

---

## 🏗️ System Architecture & Core Pipelines

The system is designed with scalability and data quality in mind, split into three main pipelines:

### 1. Ingestion & Data Readiness (ETL)

* **Annotation-Free Processing:** Automatically parses unstructured, multi-media campus data (websites, PDF guidelines, and images).
* **Advanced OCR Integration:** Extracts high-fidelity text from embedded tables and flowcharts within administrative PDFs.
* **Recursive Character Text Splitting:** Optimized chunk sizes to preserve semantic context and hierarchy for complex campus regulations.

### 2. Systematic Embedding & Retrieval Optimization

* **Model Benchmarking:** Evaluated and benchmarked multiple embedding models (including BERT MLM and contrastive learning models ranging from 30M to 330M parameters).
* **Performance Trade-offs:** Analyzed the latency-to-recall Pareto frontier, optimizing vector database searches (using **ChromaDB**) to significantly reduce cost-per-request while maintaining a high top-k recall.

### 3. LLM-Native Evaluation (RAGAS & ARES)

* Instead of relying on manual, expensive human labeling, this project implements an automated, LLM-native evaluation framework.
* We continuously track and optimize three core retrieval and generation metrics:
* **Faithfulness:** Ensuring the generator does not hallucinate and only generates answers grounded in retrieved documents.
* **Answer Relevance:** Measuring if the generated response directly addresses the user's query.
* **Context Relevance:** Quantifying the signal-to-noise ratio of the retrieved chunks.



---

## 🛠️ Tech Stack

* **Core Machine Learning:** PyTorch, Hugging Face Transformers
* **RAG & Vector Database:** LangChain, ChromaDB, Hugging Face Embeddings
* **Evaluation Frameworks:** RAGAS, ARES
* **Backend API & Deployment:** FastAPI, Heroku, LINE Messaging API
* **Language:** Python 3.10+

---

## 🚀 Getting Started

### Prerequisites

* Python 3.10 or higher
* A LINE Developer Account (for LINE Bot channel access tokens)

### 1. Installation

Clone this repository and install the dependencies:

```
git clone https://github.com/rubycheen/NTUGPT-linebot.git
cd NTUGPT-linebot
pip install -r requirements.txt

```

### 2. Environment Variables

Create a `.env` file in the root directory and configure your credentials:

```
LINE_CHANNEL_SECRET=your_line_channel_secret
LINE_CHANNEL_ACCESS_TOKEN=your_line_channel_access_token
OPENAI_API_KEY=your_openai_api_key
DATABASE_URL=your_chromadb_or_postgres_url

```

### 3. Run Locally (Uvicorn)

```
uvicorn main:app --reload

```

---

## 📊 Key Results & Impact

* **95% Reduction in Human Evaluation Costs:** Leveraged the ARES/RAGAS framework to automate evaluation pipelines, eliminating the need for constant manual validation.
* **High Human Alignment:** In blind A/B testing with real university students, the NTUGPT system won user preference in **4 out of 5 randomly selected evaluation queries** compared to baseline GPT models.

---

## 🎓 Citation

If you find this project or the thesis helpful in your research, please cite:

```
@mastersthesis{chen2024ntugpt,
  author       = {Pei-Ju (Ruby) Chen},
  title        = {Revolutionizing Campus Conversation: LLM-Powered Chatbot with Retrieval-Augmented Generation},
  school       = {National Taiwan University},
  year         = {2024},
  type         = {Master's Thesis},
  url          = {https://tdr.lib.ntu.edu.tw/jspui/retrieve/23e76241-ebae-4ce4-93a7-9f02a9d20adf/ntu-112-2.pdf}
}

```

---

## 📬 Contact

* **Author:** Pei-Ju (Ruby) Chen
* **Email:** [rubychen@ntu.im](https://www.google.com/search?q=mailto%3Arubychen%40ntu.im)
* **LinkedIn:** [Pei-Ju (Ruby) Chen](https://www.linkedin.com/in/pei-ju-chen-9a4b2b1a6/)
