from flask import url_for

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
