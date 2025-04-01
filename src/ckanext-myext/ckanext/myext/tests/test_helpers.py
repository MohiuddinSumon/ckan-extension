"""Tests for helpers.py."""

import ckanext.myext.helpers as helpers


def test_myext_hello():
    assert helpers.myext_hello() == "Hello, myext!"
