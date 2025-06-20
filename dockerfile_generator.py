import subprocess

def query_ollama(prompt, model="llama3.1:8b"):
    """Query the Ollama LLM with the given prompt using the specified model."""
    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt,
            capture_output=True,
            check=True,
            encoding='utf-8',
            errors='false'
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print("Error calling Ollama:", e.stderr)
        return None

def collect_user_input():
    print("📦 Please describe your application by answering the following:\n")
    lang = input("1. 🧠 Language + Framework (e.g., Java + Spring Boot):\n> ").strip()
    build = input("2. 🛠️ Build command (e.g., mvn clean package, npm run build):\n> ").strip()
    deps = input("3. 📂 Dependencies file or tool (e.g., pom.xml, requirements.txt):\n> ").strip()
    start = input("4. 🚀 Start command (e.g., java -jar app.jar):\n> ").strip()
    port = input("5. 🌐 Runtime port (e.g., 8080):\n> ").strip()
    app_type = input("6. 🔁 App type (static site / backend server / CLI):\n> ").strip()
    extras = input("7. 🧩 Special instructions (e.g., custom Nginx, env vars, multi-port):\n> ").strip()

    return f"""
Language and Framework: {lang}
Build Command: {build}
Dependencies File: {deps}
Start Command: {start}
Runtime Port: {port}
App Type: {app_type}
Special Instructions: {extras}
""".strip()

def build_prompt(user_description):
    return f"""
You are a professional DevOps assistant.

Your task is to generate a **production-ready, multi-stage Dockerfile** based on the application description below.

STRICT RULES:
- DO NOT include explanations, bullet points, markdown, or comments
- DO NOT wrap the Dockerfile in triple backticks (```), markdown, or extra formatting
- Output ONLY the raw Dockerfile content
- Use appropriate, modern, official base images
- Use multi-stage builds if there is a build step
- Use `COPY . .` only after dependency optimization
- Copy everything to the dockerfile except files in .dockerignore
- Set WORKDIR in both stages
- Use `EXPOSE` only in the final stage
- Use `ENTRYPOINT` or `CMD` to run the app
- The output must be a valid Dockerfile and nothing else

Application Description (use exactly as stated — do not infer or correct):
\"\"\"
{user_description}
\"\"\"

"""


def main():
    print("🔧 Dockerfile Generator AI Agent (llama3.1:8b) 🔧\n")
    user_description = collect_user_input()
    prompt = build_prompt(user_description)
    dockerfile_content = query_ollama(prompt, model="llama3.1:8b")

    if dockerfile_content:
        with open("Dockerfile", "w") as f:
            f.write(dockerfile_content)
        print("\n✅ Dockerfile generated successfully:\n")
        print(dockerfile_content)
    else:
        print("❌ Failed to generate Dockerfile.")

if __name__ == "__main__":
    main()
