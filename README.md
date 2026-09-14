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
