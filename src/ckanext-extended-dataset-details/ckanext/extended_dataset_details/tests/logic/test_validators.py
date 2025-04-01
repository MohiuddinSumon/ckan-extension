"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.extended_dataset_details.logic import validators


def test_extended_dataset_details_reauired_with_valid_value():
    assert validators.extended_dataset_details_required("value") == "value"


def test_extended_dataset_details_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.extended_dataset_details_required(None)
