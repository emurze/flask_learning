from uuid import UUID

from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)


# Converters


@app.route("/<hello>")
def home(hello: str) -> str:
    return f"<h2>home2 {escape(hello)}</h2>"


@app.route("/post/<int:post_id>")
def post(post_id: int) -> str:
    return f"Post {escape(post_id)}"


@app.route("/money/<float:some_money>")
def money(some_money: float) -> str:
    return f"Money {escape(some_money)}"


@app.route("/path/<path:subpath>")
def path(subpath: str) -> str:
    return f"Path {escape(subpath)}"


@app.route("/secret/<uuid:key>")
def secret(key: UUID) -> str:
    """Example: /secret/f81d4fae-7dec-11d0-a765-00a0c91e6bf6"""
    return f"Secret {escape(key)}"


# Unique Redirect Behavior


@app.route("/projects/")
def projects() -> str:
    """
    You will be redirected in this example:
     /projects -> /projects/
    """
    return "Projects"


@app.route("/about")
def about() -> str:
    """
    You won't be redirected in this example:
     /about
     /about/ -> Not Found
    """
    return "About"


# By default, only method GET


@app.route("/article/<int:article_id>", methods=["GET", "POST"])
def article(article_id: int) -> str:
    if request.method == "POST":
        pass
    return f"Article {escape(article_id)}"


# Route alternatives


@app.get("/cake/<int:cake_id>")
def get_articles() -> str:
    """
    if GET is present, Flask automatically adds the HEAD and OPTIONS methods
    """
    return "Articles"


@app.post("/cake/<int:cake_id>")
def post_articles() -> str:
    return "Articles"
