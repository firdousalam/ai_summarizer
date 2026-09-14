# app.py
from flask import Flask, request, render_template_string
from fetcher import fetch_article
from summarizer import summarize_text

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<title>AI Summarizer</title>
<h1>Summarize an Article</h1>
<form method="POST">
  <input type="text" name="url" placeholder="Enter article URL" style="width:400px"/>
  <button type="submit">Summarize</button>
</form>
{% if summary %}
  <h2>Summary:</h2>
  <p>{{ summary }}</p>
{% endif %}
"""


@app.route("/", methods=["GET", "POST"])
def index():
    summary = None
    if request.method == "POST":
        url = request.form["url"]
        article_text = fetch_article(url)
        summary = summarize_text(article_text)
    return render_template_string(HTML_TEMPLATE, summary=summary)


if __name__ == "__main__":
    app.run(debug=True)
