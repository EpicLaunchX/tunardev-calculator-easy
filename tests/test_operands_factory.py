import pytest

from src.pytemplate.domain.models import Operands, operands_factory


def test_operands_factory_creation():
    operands = operands_factory(5, 10)
    assert isinstance(operands, Operands)
    assert operands.first_operand == 5
    assert operands.second_operand == 10


def test_operands_factory_negative_values():
    operands = operands_factory(-5, -10)
    assert operands.first_operand == -5
    assert operands.second_operand == -10


def test_operands_factory_zero_values():
    operands = operands_factory(0, 0)
    assert operands.first_operand == 0
    assert operands.second_operand == 0


def test_operands_factory_large_values():
    operands = operands_factory(1_000_000, 2_000_000)
    assert operands.first_operand == 1_000_000
    assert operands.second_operand == 2_000_000
