from typing import NoReturn
from uuid import UUID

from flask import (
    Flask,
    request,
    render_template,
    make_response,
    Response,
    abort,
    redirect,
    url_for,
    session,
)
from markupsafe import escape

app = Flask(__name__)
app.secret_key = "LERKA_IS_MEGA_SECRET"


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


@app.get("/logic/")
@app.get("/logic/<name>")
def logic(name: str = "Empty") -> str:
    return f"Logic(name={name})"


@app.get("/lera/<name>")
def anti_pattern(name: str) -> str:
    print(request)
    return render_template("lera.html", name=name)


@app.get("/main")
def request_object() -> Response:
    # 1 Access form data

    app.logger.warning(
        request.form.get("username"),
        request.form.get("password"),
    )

    # 2 Access query args

    app.logger.warning(request.args.get("lera"))

    # 3 Access files

    f = request.files["file_name"]
    f.save("files/wfw.txt")

    # 4 Access Cookies

    app.logger.warning(request.cookies.get("username"))

    # Explicitly setup response
    response = make_response(render_template("lera.html"))
    response.set_cookie("username", "user")
    return response


@app.get("/abort")
def view_abort() -> NoReturn:
    app.logger.warning("before abort")
    abort(404)
    # app.logger.warning('after abort')


# @app.get("/redirect")
# def view_redirect():
#     return redirect(url_for("logic"))


@app.errorhandler(404)
def page_not_found(*args) -> tuple[str, int]:
    """
    str -> Response  << automatically >>
    """
    app.logger.warning(args)
    return render_template("not_found.html"), 404  # It says status to flask


# Response


@app.get("/")
def extra_info1():
    response = make_response(Response(f"INFO {escape(session)}"))
    response.headers["wef"] = "something"
    return response, 234


@app.get("/users")
def users() -> list:
    """
    List or Dict -> JSON  << automatically >>
    """
    return [
        {"id": 1, "name": "user_1"},
        {"id": 2, "name": "user_2"},
    ]


@app.get("/login")
def login_get() -> str:
    return """
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    """


@app.post("/login")
def login_post():
    session["username"] = request.form["username"]
    return redirect(url_for("extra_info1"))


# @app.get("/logout")
# def logout():
#     session.pop("username", None)
#     return redirect(url_for("login_get"))
