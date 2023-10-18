import pytest
from calculator import calculate

@pytest.mark.parametrize("num1,num2,expected_result",[(-3, -2, -5),(-1,0,-1), (1,2,3), (3,4,7),(-1,3,2)])
def test_add(num1,num2,expected_result):
  """Tests the addition operation."""
  operator = "+"
  result = calculate(num1, num2, operator)

  assert result == expected_result

@pytest.mark.parametrize("num1,num2,expected_result",[(-3, -2, -1),(-1,0,-1), (1,2,-1), (3,4,-1)])
def test_subtract(num1,num2,expected_result):
  """Tests the subtraction operation."""

  operator = "-"
  
  result = calculate(num1, num2, operator)

  assert result == expected_result

@pytest.mark.parametrize("num1,num2,expected_result",[(-3, -2, 6),(-1,0,0), (1,2,2), (3,4,12)])
def test_multiply(num1,num2,expected_result):
  """Tests the multiplication operation."""

  operator = "*"
  
  result = calculate(num1, num2, operator)

  assert result == expected_result

@pytest.mark.parametrize("num1,num2,expected_result",[(-3, -2, 1.5),(-1,2,-0.5), (1,2,0.5), (3,4,0.75)])
def test_divide(num1,num2,expected_result):
  """Tests the division operation."""

  operator = "/"
  
  result = calculate(num1, num2, operator)

  assert result == expected_result


def test_divide_by_zero():
  """Tests that division by zero raises a ZeroDivisionError exception."""

  num1 = 2
  num2 = 0
  operator = "/"

  with pytest.raises(ZeroDivisionError):
    calculate(num1, num2, operator)

    