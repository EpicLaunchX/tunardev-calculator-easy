import pytest

from src.pytemplate.domain.models import Operands, operands_factory
from src.pytemplate.service.calculator import Calculator


def test_add():
    calculator = Calculator()
    operands = operands_factory(45, 35)
    result = calculator.add(operands)
    assert result == 80


def test_subtract():
    calculator = Calculator()
    operands = operands_factory(45, 35)
    result = calculator.subtract(operands)
    assert result == 10


def test_multiply():
    calculator = Calculator()
    operands = operands_factory(45, 35)
    result = calculator.multiply(operands)
    assert result == 1575


def test_divide_by_zero():
    calculator = Calculator()
    operands = operands_factory(45, 0)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(operands)


def test_divide():
    calculator = Calculator()
    operands = operands_factory(45, 5)
    result = calculator.divide(operands)
    assert result == 9
