import sys
import os

# Force Python to see Jenkins workspace
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from app import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(2, 3) == 6


def test_divide():
    assert divide(6, 3) == 2


def test_divide_by_zero():
    assert divide(5, 0) == "Error: Division by zero"
