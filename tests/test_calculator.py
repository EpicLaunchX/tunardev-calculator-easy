import pytest

from src.pytemplate.domain.models import Operands, operands_factory
from src.pytemplate.service.calculator import Calculator

calculator = Calculator()


def test_add():
    operands = operands_factory(45, 35)
    result = calculator.add(operands)
    assert result == 80


def test_multiply():
    operands = operands_factory(45, 35)
    result = calculator.multiply(operands)
    assert result == 1575


def test_subtract():
    operands = operands_factory(45, 35)
    result = calculator.subtract(operands)
    assert result == 10


def test_divide():
    operands = operands_factory(45, 5)
    result = calculator.divide(operands)
    assert result == 9


def test_divide_by_zero():
    operands = operands_factory(45, 0)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(operands)
