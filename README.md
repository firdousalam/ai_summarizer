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

---

## 🖼 MCP Architecture Diagram

Below is a visual representation of how the summarizer project works with MCP:

![MCP Architecture Diagram](https://copilot.microsoft.com/th/id/BCO.d2b4b888-bb40-4692-bfcf-6c5b98da0184.png)

### Flow Explanation
1. **User (Web UI)** → Enters article URL.
2. **Flask App** → Fetches article text and sends it forward.
3. **MCP (Model Context Protocol)** → Standardizes communication between the app and the model.
4. **Ollama Model** → Processes the text and generates a summary.
5. **MCP** → Returns the summary back in a consistent format.
6. **User (Web UI)** → Views the summarized output.

This diagram makes it clear that MCP is the **bridge** ensuring smooth communication between your app and Ollama.

---



## 🧪 Testing the Application
Testing ensures that your summarizer correctly fetches articles, communicates with Ollama through MCP, and displays summaries in the web UI.

🧰 Prerequisites
Before testing, make sure:

Ollama is installed and running locally:

bash
ollama serve
You’ve pulled a model (for example, llama2):

bash
ollama pull llama2
Your Flask app is running:

bash
python app.py
Your virtual environment is activated and dependencies are installed:

bash
pip install -r requirements.txt
🧩 Step‑by‑Step Test Flow
1. Start the Flask Server
Run:

bash
python app.py
You should see:

Code
* Running on http://127.0.0.1:5000
2. Open the Web Interface
Visit http://127.0.0.1:5000 in your browser.

3. Enter a Test URL
Try a simple article, for example:

Code
https://www.bbc.com/news/science-environment-123456
4. Observe the Flow
Flask sends the URL to the fetcher.

The fetcher extracts text from <p> tags.

The summarizer sends the text to Ollama via MCP.

Ollama returns a concise summary.

Flask displays the summary on the page.

🧠 How MCP Works During Testing
Component	Role	MCP Interaction
Flask App	Collects input and displays output	Sends text to MCP
Fetcher	Extracts article content	No direct MCP use
Summarizer	Communicates with Ollama	Uses MCP to standardize request/response
Ollama Model	Generates summary	Responds via MCP
User	Views result	Interacts through UI


MCP ensures that the request format, response structure, and data exchange between Flask and Ollama remain consistent and predictable.

🧩 Example Output
After submitting a URL, you’ll see something like:

Code
Summary:
This article discusses recent advances in renewable energy, highlighting solar and wind power innovations that reduce carbon emissions globally.
## 🧪 Additional Tests
Local file test: Replace the URL input with a local .txt file containing an article.

Error handling test: Try invalid URLs or empty input to verify graceful error messages.

Model swap test: Change the model name in summarizer.py to another Ollama model (e.g., mistral) and confirm MCP still works seamlessly.

## ✅ Expected Results
The app should fetch text, summarize it, and display the result within seconds.

MCP should handle the communication without manual formatting.

No crashes or missing module errors should occur.

## 🧩 Troubleshooting
Issue	Cause	Fix
ModuleNotFoundError	Missing dependencies	Run pip install -r requirements.txt
ConnectionError	Ollama not running	Start Ollama with ollama serve
Empty summary	Article too short or model timeout	Try a longer article or restart Ollama


Once you’ve verified these steps, your MCP‑based summarizer is fully tested and ready for demonstration.

Would you like me to add a testing checklist section (with tick‑boxes for each step) so your juniors can follow it during their own tests?

ollama serve
Error: listen tcp 127.0.0.1:11434: bind: Only one usage of each socket address (protocol/network address/port) is normally permitted.
(venv) PS C:\Users\techn\TechnophileFirdous\ai_summarizer>
That error means Ollama is already running on port 11434, so when you try to start another instance with ollama serve, Windows blocks it because that port is already in use.

## ✅ How to Fix It
🧩 Option 1: Use the Existing Ollama Instance
You don’t need to start a new one — just keep using the one that’s already running.
Try your summarizer directly:

bash
python app.py
If Ollama is active, your app will connect automatically.

🧩 Option 2: Stop the Existing Ollama Process
If you want to restart Ollama cleanly:

Press Ctrl + Shift + Esc to open Task Manager.

Find any process named ollama.exe.

Right-click → End Task.

Then restart Ollama:

bash
ollama serve
🧩 Option 3: Run Ollama on a Different Port
If you want to keep both instances running (for testing multiple setups):

bash
ollama serve --port 11500
Then update your summarizer.py endpoint:

python
response = requests.post("http://localhost:11500/api/generate", json=payload, stream=True)
🧠 Why This Happens
Windows allows only one process to listen on a specific port at a time.
Ollama’s default port 11434 is reserved for its API server, so if one instance is already running, any new attempt to bind to that port fails.

Once you confirm Ollama is running (either existing or restarted), your summarizer should work fine.

Would you like me to show you how to verify Ollama’s active port and test its API connection before running your Flask app?



