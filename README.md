# 🐳 Automated Dockerfile Generator

A **GenAI-powered AI agent** that automatically generates **production-grade Dockerfiles** based on simple user input. This tool leverages **Ollama** and the **LLaMA 3 (8B)** model to produce Dockerfiles following industry best practices and multi-stage builds—without requiring deep DevOps knowledge from the user.

---

## ⚙️ Features

- Interactive CLI that gathers details about your application  
- Uses LLaMA 3.2:8B model via Ollama to generate accurate, optimized Dockerfiles  
- Enforces modern best practices (multi-stage builds, minimal base images, etc.)  
- Zero explanation or markdown—pure, deployable Dockerfile output  
- Easy to use with just Python and Ollama  

---

## 📋 Prerequisites

### ✅ Install Ollama

**On Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**On MacOS:**
```bash
brew install ollama
```

**On Windows:**
- Install setup

## 🔁 Start Ollama Service
```bash
ollama serve
```
## 📥 Pull LLaMA 3.2 8B Model
```bash
ollama pull llama3.1:8b
```
# 🚀 Project Setup


