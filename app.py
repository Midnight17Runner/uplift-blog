from flask import Flask, render_template, send_from_directory, request, redirect, url_for
import os

app = Flask(__name__)

ARTICLES_DIR = "articles"

@app.route("/")
def index():
    files = sorted(os.listdir(ARTICLES_DIR), reverse=True)
    articles = [
        {"title": f.replace(".html", ""), "filename": f}
        for f in files if f.endswith(".html")
    ]
    return render_template("index.html", articles=articles)

@app.route("/article/<filename>")
def view_article(filename):
    try:
        with open(os.path.join(ARTICLES_DIR, filename), encoding="utf-8") as f:
            content = f.read()
        return render_template("article.html", content=content)
    except FileNotFoundError:
        return "Article not found", 404

if __name__ == "__main__":
    app.run(debug=True)
