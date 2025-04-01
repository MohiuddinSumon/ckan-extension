"""Tests for views.py."""

import pytest

import ckanext.extended_dataset_details.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "extended_dataset_details")
@pytest.mark.usefixtures("with_plugins")
def test_extended_dataset_details_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("extended_dataset_details.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, extended_dataset_details!"
