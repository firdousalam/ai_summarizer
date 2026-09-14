# fetcher.py
from urllib.request import urlopen
from html.parser import HTMLParser


class _ParagraphParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self._in_paragraph = False
        self._paragraphs = []
        self._current = []

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self._in_paragraph = True
            self._current = []

    def handle_endtag(self, tag):
        if tag == 'p' and self._in_paragraph:
            self._paragraphs.append(''.join(self._current).strip())
            self._in_paragraph = False

    def handle_data(self, data):
        if self._in_paragraph:
            self._current.append(data)


def fetch_article(url):
    with urlopen(url) as response:
        html = response.read().decode('utf-8', errors='replace')
    parser = _ParagraphParser()
    parser.feed(html)
    return " ".join(parser._paragraphs)
