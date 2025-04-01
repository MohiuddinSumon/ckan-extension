from flask import Blueprint


myext = Blueprint(
    "myext", __name__)


def page():
    return "Hello, myext!"


myext.add_url_rule(
    "/myext/page", view_func=page)


def get_blueprints():
    return [myext]
