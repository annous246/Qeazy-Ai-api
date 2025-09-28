<p align="center"> 
  <img src="src/assets/logo.png" alt="Qeazy Summarizer Icon" width="250"/> 
</p>

# <h1 align="center">Qeazy Summarizer Microservice</h1>
<p align="center">
This Flask microservice handles **abstractive summarization** and **category classification** for Qeazy 📄🤖.  
It leverages **Qwen/Qwen3-Next-80B-A3B-Instruct**, Hugging Face Inference API, and **ChromaDB** to provide concise summaries and semantic categorization of PDF content.
</p>

---

## 🔥 Tech Stack

### Backend
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Hugging Face](https://img.shields.io/badge/HuggingFace-inference-orange?style=for-the-badge&logo=huggingface&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-00BFFF?style=for-the-badge&logoColor=white)

---

## ✨ Features

- 📝 **Abstractive summarization** using **Qwen/Qwen3-Next-80B-A3B-Instruct** via Hugging Face API  
- 📊 **Category classification** with **ChromaDB** for semantic retrieval  
- ⚡ Enforces **token/character constraints** via controlled prompt design  
- 🔗 Works as a **microservice** integrated with Node.js/Express backend for full-stack AI workflows  

---

## 🚀 Getting Started

### Prerequisites
- [Python 3.10+](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/)
- [Hugging Face API Token](https://huggingface.co/docs/api-inference/index)

### Installation

```bash
# Navigate to the microservice folder
cd flask-summarizer

# Install dependencies
pip install -r requirements.txt

# Run Flask server
python app.py
