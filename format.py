"""
Day X: Name
"""
from unittest import TestCase


def thing(stuff):
    pass


class TestThing(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print(f'\nExecuting {cls.__name__}')

    def setUp(self) -> None:
        self.current_result = False
        print(f'\t Running {self._testMethodName}', end='\n\t\t')

    def assertion(self, test_passes) -> None:
        self.current_result = test_passes
        assert test_passes

    def tearDown(self) -> None:
        test_result = 'PASS' if self.current_result else 'FAIL'
        self.current_result = False
        print('\t\t' + test_result)

    def test_one_example(self):
        self.assertion(True)

    def test_one_data(self):
        self.assertion(True)

    def test_two_example(self):
        self.assertion(True)

    def test_two_data(self):
        self.assertion(True)
