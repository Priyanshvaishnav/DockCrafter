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
## 1. Clone the repo
```bash
git clone  https://github.com/Priyanshvaishnav/DockCrafter.git
cd DockCrafter
```

## 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate

.\venv\Scripts\activate  ##For Windows
```

## 3. Install dependencies
```bash
pip install -r requirements.txt
```

## 4.▶️ Run the Application
```bash
python dockerfile_generator.py
```
You’ll be prompted to enter details such as:
    Programming language and framework (e.g., Node.js + Express)
    Build command (e.g., npm run build)
    Dependency file (e.g., package.json)
    Start command (e.g., node index.js)
    Runtime port (e.g., 3000)
    App type (e.g., backend server, static site)
    Any extra/special instructions

### ✅ Output
After collecting your inputs, the tool sends a formatted prompt to the Ollama LLM.
A clean Dockerfile is generated and saved as Dockerfile in the current directory.

# 🧠 How It Works

The main script is dockerfile_generator.py, and it works as follows:
    collect_user_input() – Gathers structured input from the user interactively.
    build_prompt() – Creates a prompt with strict output formatting rules for the LLM.
    query_ollama() – Sends the prompt to the Ollama CLI using subprocess and retrieves only the raw Dockerfile content.
    Outputs the file – The Dockerfile is saved locally as Dockerfile.






