from src.calculator import Calculator

def test_add():
    c = Calculator()
    assert c.add(1, 2) == 3