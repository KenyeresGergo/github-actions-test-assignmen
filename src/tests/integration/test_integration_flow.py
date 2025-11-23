from src.calculator import Calculator

def test_division_integration():
    c = Calculator()
    result = c.divide(10, 2)
    assert result == 5