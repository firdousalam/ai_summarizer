# summarizer.py
import json
from urllib.request import Request, urlopen


def summarize_text(article_text):
    payload = {
        "model": "llama2",  # or any Ollama model you’ve pulled
        "prompt": f"Summarize this article in 5 sentences:\n\n{article_text}"
    }

   # If you want GPT‑4 or Claude:
    # payload = {
    #     "model": "gpt4",  # or "claude"
    #     "prompt": f"Summarize this article in 5 sentences:\n\n{article_text}"
    # }

    request = Request(
        "http://localhost:11434/api/generate",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    summary = ""
    with urlopen(request) as response:
        for line in response:
            if line:
                summary += json.loads(line.decode("utf-8")).get("response", "")
    return summary
