"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.myext.logic import validators


def test_myext_reauired_with_valid_value():
    assert validators.myext_required("value") == "value"


def test_myext_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.myext_required(None)
