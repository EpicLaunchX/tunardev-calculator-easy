from unittest.mock import MagicMock, patch

import pytest

from src.pytemplate.entrypoints.cli.main import main


@patch("builtins.input", side_effect=["45", "35", "add"])
@patch("service.calculator.Calculator.add", return_value=80)
def test_main_add(mock_add, mock_input):
    with patch("builtins.print") as mock_print:
        main()
        mock_print.assert_called_once_with("Result: 80")


@patch("builtins.input", side_effect=["45", "35", "subtract"])
@patch("service.calculator.Calculator.subtract", return_value=10)
def test_main_subtract(mock_subtract, mock_input):
    with patch("builtins.print") as mock_print:
        main()
        mock_print.assert_called_once_with("Result: 10")


@patch("builtins.input", side_effect=["45", "35", "multiply"])
@patch("service.calculator.Calculator.multiply", return_value=1575)
def test_main_multiply(mock_multiply, mock_input):
    with patch("builtins.print") as mock_print:
        main()
        mock_print.assert_called_once_with("Result: 1575")


@patch("builtins.input", side_effect=["45", "5", "divide"])
@patch("service.calculator.Calculator.divide", return_value=9)
def test_main_divide(mock_divide, mock_input):
    with patch("builtins.print") as mock_print:
        main()
        mock_print.assert_called_once_with("Result: 9")


@patch("builtins.input", side_effect=["45", "0", "divide"])
@patch("service.calculator.Calculator.divide", side_effect=ValueError("Cannot divide by zero"))
def test_main_divide_by_zero(mock_divide, mock_input):
    with patch("builtins.print") as mock_print:
        main()
        mock_print.assert_called_once_with("Cannot divide by zero")


@patch("builtins.input", side_effect=["45", "35", "invalid"])
def test_main_invalid_action(mock_input):
    with patch("builtins.print") as mock_print:
        main()
        mock_print.assert_called_once_with("Invalid action.")
