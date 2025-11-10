class Calculadora:
    def sumar(self, a, b) -> float:
        return 0

    def restar(self, a, b) -> float:
        return a - b

    def multiplicar(self, a, b) -> float:
        return a * b

    def dividir(self, a, b) -> float:
        if b == 0:
            raise ValueError("No se puede dividir por cero.")
        return a / b
    
