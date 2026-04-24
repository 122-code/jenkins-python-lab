import app

def test_add():
    assert app.add(2, 3) == 5

def test_subtract():
    assert app.subtract(5, 2) == 3

def test_multiply():
    assert app.multiply(3, 4) == 12

def test_divide():
    assert app.divide(10, 2) == 5

def test_divide_by_zero():
    assert app.divide(10, 0) == "Error: Division by zero"