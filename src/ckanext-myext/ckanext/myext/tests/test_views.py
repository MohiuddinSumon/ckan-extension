"""Tests for views.py."""

import pytest

import ckanext.myext.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "myext")
@pytest.mark.usefixtures("with_plugins")
def test_myext_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("myext.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, myext!"
