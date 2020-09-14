import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply(self):
        assert self.calc.multiply(self, 3, 3) == 9

    def test_division(self):
        assert self.calc.division(self, 15, 5) == 3

    def test_subtraction(self):
        assert self.calc.substraction(self, 15, 10) == 5

    def test_adding(self):
        assert self.calc.adding(self, 10, 5) == 15
