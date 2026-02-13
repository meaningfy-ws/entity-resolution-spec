"""Temporary test to validate the CI pipeline."""

from ere.hello import greet


def test_greet():
    assert greet("World") == "Hello, World!"


def test_greet_empty():
    assert greet("") == "Hello, !"
