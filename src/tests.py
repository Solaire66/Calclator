from main import Calculator # Importamos tu clase desde main.py

def test_suma_calculator():
    calc = Calculator()
    # Ahora probamos tu código real
    assert calc.sum(10, 5) == 15