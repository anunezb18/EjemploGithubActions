from main import Calculadora

def test_suma():
    calc = Calculadora()
    assert calc.sumar(2, 3) == 5
    assert calc.sumar(-1, 1) == 0
    assert calc.sumar(0, 0) == 0

def test_resta():
    calc = Calculadora()
    assert calc.restar(5, 3) == 2
    assert calc.restar(0, 0) == 0
    assert calc.restar(-1, -1) == 0

def test_multiplicacion():
    calc = Calculadora()
    assert calc.multiplicar(2, 3) == 6
    assert calc.multiplicar(-1, 1) == -1
    assert calc.multiplicar(0, 5) == 0

def test_division():
    calc = Calculadora()
    assert calc.dividir(6, 3) == 2
    assert calc.dividir(-6, 2) == -3
    try:
        calc.dividir(5, 0)
        assert False  # Should not reach this point
    except ValueError:
        assert True  # Expected exception