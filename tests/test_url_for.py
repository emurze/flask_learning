from flask import url_for, request

from src.app import app


# URL Building (reverse)


def test_url_for_home():
    with app.test_request_context():
        home_path = url_for("home", hello="hi", next="/project/best")
        assert home_path == "/hi?next=/project/best"


def test_url_for_post():
    with app.test_request_context():
        home_path = url_for("post", post_id="24234", search="blue")
        assert home_path == "/post/24234?search=blue"


def test_url_for_projects():
    with app.test_request_context():
        home_path = url_for("projects", color="blue")
        assert home_path == "/projects/?color=blue"


def test_url_for_about():
    with app.test_request_context():
        home_path = url_for("about", color="blue")
        assert home_path == "/about?color=blue"


def test_url_for_static():
    with app.test_request_context():
        home_path = url_for("static", filename="style.css")
        assert home_path == "/static/style.css"


def test_get_articles():
    with app.test_request_context("/get_articles", method="GET"):
        assert request.path == "/get_articles"
        assert request.method == "GET"
