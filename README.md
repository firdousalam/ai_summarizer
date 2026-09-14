# ai_summarizer
AI Summarizer for Articles (Python + Ollama)


# 📰 AI Summarizer with Ollama (Python + MCP)

A simple project that demonstrates the **Model Context Protocol (MCP)** in action using **Ollama**.  
This tool fetches articles from the web, sends them to Ollama for summarization, and displays concise summaries via a minimal **Flask web UI**.

---

## 🚀 Features
- **[Article Fetcher](ca://s?q=Fetch_articles_with_Python)**: Scrapes text content from any given URL.
- **[Summarization](ca://s?q=Summarize_text_with_Ollama)**: Uses Ollama models (e.g., `llama2`) to generate a short summary.
- **[Web UI](ca://s?q=Enhance_Flask_UI_for_summarizer)**: Simple Flask interface with a textbox for URLs and summary output.
- Demonstrates **MCP integration** with Ollama in a real-world workflow.

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai-summarizer.git
   cd ai-summarizer


## Create a virtual environment:

bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
Install dependencies:

## bash
pip install flask requests beautifulsoup4
Make sure Ollama is installed and running locally:

## bash
ollama run llama2
🛠 Usage
Start the Flask app:

## bash
python app.py
Open your browser at:

## Code
http://127.0.0.1:5000
Enter an article URL and click Summarize.

The summary will appear below the form.

## 📂 Project Structure
Code
ai-summarizer/
│── app.py          # Flask web app
│── fetcher.py      # Article fetcher (scraping logic)
│── summarizer.py   # Ollama summarization logic
│── README.md       # Project documentation
🎯 Example Workflow
Input: https://example.com/news/article

Fetcher extracts text from <p> tags.

Text is sent to Ollama via MCP.

Ollama returns a concise summary.

Flask UI displays the summary.

🔧 Customization
Change the model in summarizer.py:

python
"model": "llama2"
Replace with any Ollama model you’ve pulled.

Adjust the prompt for different summary styles (short, bullet points, etc.).

📌 Outcome
This project is small enough to build in a few hours but powerful enough to demonstrate:

MCP’s role in connecting applications with AI models.

Real-world utility of AI summarization.

Integration simplicity using Python + Flask.

🖼 Future Enhancements
Add CLI mode for terminal-based summarization.

Support file uploads (PDF, TXT).

Improve scraping logic for cleaner text extraction.

Code

---

Would you like me to also create a **[CLI version](ca://s?q=Build_CLI_version_for_summarizer)** of this project so you can run summaries directly from the terminal without the Flask UI?


---

## 📦 Dependency Setup with requirements.txt

This project uses a `requirements.txt` file to manage dependencies.  
It ensures that anyone cloning the repo can install the exact packages needed.

### 1. Create and Activate a Virtual Environment
It’s best practice to use a virtual environment so dependencies don’t conflict with your global Python setup.

```bash
# Create venv
python -m venv venv

# Activate venv (Windows)
venv\Scripts\activate

# Activate venv (Linux/Mac)
source venv/bin/activate


2. Install Dependencies
Once inside the virtual environment, install all required packages:

pip install -r requirements.txt

This will install:

Flask → Web framework for the UI

Requests → Fetches article content

BeautifulSoup4 → Parses HTML text

3. Verify Installation
Check that packages are installed correctly:

bash
pip list
You should see flask, requests, and beautifulsoup4 listed.

4. Run the App
Now you can start the summarizer:

bash
python app.py
Open your browser at:

Code
http://127.0.0.1:5000
📂 requirements.txt Contents
Code
flask
requests
beautifulsoup4
🔧 Notes
Always activate your virtual environment before running the app.

If you add new dependencies, update requirements.txt with:

bash
pip freeze > requirements.txt
This ensures collaborators or future setups can reproduce the environment easily.

Code

---

This addition makes your README much more **developer-friendly** and prevents the exact issue you ran into (global vs venv mismatch).  

Would you like me to also add a **[Project Structure diagram](ca://s?q=Add_project_structure_to_README)** section so new contributors can instantly see how `app.py`, `fetcher.py`, and `summarizer.py` fit together?




---

# 🧩 Understanding Model Context Protocol (MCP)

This project demonstrates the **Model Context Protocol (MCP)** in action with **Ollama**.  
MCP is a standard way to connect applications (like our Python/Flask app) with AI models, ensuring smooth communication and interoperability.

---

## 🔍 What is MCP?

**Model Context Protocol (MCP)** is a protocol designed to:
- Standardize how applications talk to AI models.
- Provide a consistent interface for sending prompts and receiving responses.
- Allow developers to swap models or backends without rewriting the entire app.

Think of MCP as the "translator" between your app and the AI model.

---

## 🏗️ Architecture in This Project

Here’s how MCP fits into our summarizer:

1. **[Frontend (Flask UI)](ca://s?q=Enhance_Flask_UI_for_summarizer)**  
   - User enters an article URL.  
   - Flask sends the request to the backend.

2. **[Fetcher](ca://s?q=Fetch_articles_with_Python)**  
   - Scrapes the article text using `requests` + `BeautifulSoup`.

3. **[Summarizer](ca://s?q=Summarize_text_with_Ollama)**  
   - Sends the text to Ollama via MCP.  
   - MCP ensures the request is properly formatted and the response is standardized.

4. **[Ollama Model](ca://s?q=Use_Ollama_as_backend_for_chat)**  
   - Processes the text and generates a summary.  
   - Returns the result back through MCP.

5. **Output**  
   - Flask displays the summary in the browser.

### Diagram



User (Web UI) → Flask App → Fetcher → MCP → Ollama Model → MCP → Flask → User


---

## 🎯 Use Case

In this project, MCP is used to:
- Fetch article text.
- Send it to Ollama for summarization.
- Return a concise summary to the user.

This demonstrates a **real-world workflow**: integrating AI into a web app with minimal friction.

---

## 🌟 Benefits of MCP

- **[Interoperability](ca://s?q=Explain_MCP_interoperability)**: Works with different models (Llama2, GPT, etc.) without changing app logic.
- **[Consistency](ca://s?q=Explain_MCP_consistency)**: Standard request/response format makes debugging and scaling easier.
- **[Flexibility](ca://s?q=Explain_MCP_flexibility)**: Swap models or backends quickly (e.g., Ollama → OpenAI).
- **[Scalability](ca://s?q=Explain_MCP_scalability)**: Same protocol can be used across multiple apps and services.
- **[Developer Productivity](ca://s?q=Explain_MCP_productivity)**: Focus on building features, not reinventing communication layers.

---

## 📌 Why MCP is Helpful

Without MCP:
- Each app would need custom code for each model.
- Switching models would mean rewriting integration logic.
- Debugging would be inconsistent across projects.

With MCP:
- One protocol, many models.
- Easier demos, faster prototypes.
- Clear separation of concerns (UI, fetcher, summarizer, model).

---

## 🧑‍💻 Explaining to Juniors

When teaching MCP:
- Compare it to **HTTP for the web** — just like HTTP standardizes communication between browsers and servers, MCP standardizes communication between apps and AI models.
- Show how our summarizer project uses MCP to connect Flask → Ollama seamlessly.
- Highlight that MCP makes AI integration **future-proof**: if tomorrow you want to use a different model, you don’t need to rebuild the whole app.

---
