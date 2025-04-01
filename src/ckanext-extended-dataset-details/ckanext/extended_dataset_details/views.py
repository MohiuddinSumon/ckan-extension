from flask import Blueprint


extended_dataset_details = Blueprint(
    "extended_dataset_details", __name__)


def page():
    return "Hello, extended_dataset_details!"


extended_dataset_details.add_url_rule(
    "/extended_dataset_details/page", view_func=page)


def get_blueprints():
    return [extended_dataset_details]
