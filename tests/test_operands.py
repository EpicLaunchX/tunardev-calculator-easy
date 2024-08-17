import pytest
from src.pytemplate.domain.models import Operands

def test_operands_initialization():
    operands = Operands(first_operand=5, second_operand=10)
    assert operands.first_operand == 5
    assert operands.second_operand == 10

def test_operands_type():
    operands = Operands(first_operand=5, second_operand=10)
    assert isinstance(operands.first_operand, int)
    assert isinstance(operands.second_operand, int)

def test_operands_negative_values():
    operands = Operands(first_operand=-5, second_operand=-10)
    assert operands.first_operand == -5
    assert operands.second_operand == -10

def test_operands_zero_values():
    operands = Operands(first_operand=0, second_operand=0)
    assert operands.first_operand == 0
    assert operands.second_operand == 0

def test_operands_large_values():
    operands = Operands(first_operand=1_000_000, second_operand=2_000_000)
    assert operands.first_operand == 1_000_000
    assert operands.second_operand == 2_000_000
