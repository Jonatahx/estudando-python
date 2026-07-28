'''3. Controle de temperatura
Crie uma classe chamada Temperatura que armazene uma temperatura em graus
Celsius.
Implemente métodos para:
● converter Celsius para Fahrenheit;
● converter Celsius para Kelvin;
● exibir os três valores.
Utilize as fórmulas:
Fahrenheit = Celsius × 1,8 + 32
Kelvin = Celsius + 273,15
Conceitos trabalhados: classe, métodos e cálculos dentro de objetos.
'''

class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius

    def calcular_fahrenheit(self):
        return self.celsius * 1.8 + 32

    def calcular_kelvin(self):
        return self.celsius + 273.15

    def exibir_dados(self):
        print(f"Celsius: {self.celsius:.2f} °C")
        print(f"Fahrenheit: {self.calcular_fahrenheit():.2f} °F")
        print(f"Kelvin: {self.calcular_kelvin():.2f} K")

temperatura1 = Temperatura(float(input("Digite uma temperatura em celsius: ")))
temperatura1.exibir_dados()