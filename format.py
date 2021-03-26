"""
Day X: Name
"""
from unittest import TestCase


def thing(stuff):
    pass


class TestThing(TestCase):

    def setUp(self) -> None:
        print(f'\n--- Running test: {self._testMethodName} ---')

    def test_one_example(self):
        assert True

    def test_one_data(self):
        assert True

    def test_two_example(self):
        assert True

    def test_two_data(self):
        assert True
