import pytest
import pythondemo

# Passing test
def test_add():
    assert pythondemo.add(2, 3) == 5

# Failing test
def test_multiply_fail():
    assert pythondemo.multiply(4, 3) == 11

# Exception test
def test_divide_by_zero():
    with pytest.raises(ValueError):
        pythondemo.divide(10, 0)

# Logical test
def test_is_even():
    assert pythondemo.is_even(4) is True
    assert pythondemo.is_even(5) is False

# Parametrized test
@pytest.mark.parametrize("a,b,result", [
    (1, 2, 3),
    (2, 2, 4),
    (5, 5, 11)   # failing case
])
def test_add_param(a, b, result):
    assert pythondemo.add(a, b) == result

# Task 1: Factorial tests
def test_factorial_base():
    assert pythondemo.factorial(0) == 1
    assert pythondemo.factorial(1) == 1

def test_factorial_positive():
    assert pythondemo.factorial(5) == 120
    assert pythondemo.factorial(10) == 3628800

# Task 2: Negative numbers and large inputs
def test_factorial_negative():
    with pytest.raises(ValueError):
        pythondemo.factorial(-1)

def test_add_negative():
    assert pythondemo.add(-3, -7) == -10
    assert pythondemo.add(-5, 5) == 0

def test_subtract_negative():
    assert pythondemo.subtract(-10, -5) == -5

def test_multiply_negative():
    assert pythondemo.multiply(-3, 4) == -12
    assert pythondemo.multiply(-3, -3) == 9

def test_large_inputs():
    assert pythondemo.add(1000000, 2000000) == 3000000
    assert pythondemo.multiply(1000, 1000) == 1000000
    assert pythondemo.factorial(15) == 1307674368000
