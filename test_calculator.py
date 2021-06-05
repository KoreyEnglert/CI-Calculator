"""
Tests for calc app
"""
import calculator


class TestCalculatorApp:
    def test_add(self):
        assert 2 == calculator.add(1, 1)


    def test_subtract(self):
        assert 0 == calculator.subtract(2, 2)
