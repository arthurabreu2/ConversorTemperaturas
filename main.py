"""
Programa em Python 3 para converter  Celsius para Kelvin ou Fahrenheit
"""
from helpers import celsius_kelvin, celsius_fahrenheit

if __name__ == '__main__':
    while True:
        mensagem = "\nPor favor insira a temperatura em Celsius."
        mensagem += "\nSe desejar sair pressione 'q': "

        try:
            celsius = input(mensagem)
            if celsius.lower() != 'q':
                print(f"\nTemperatura em Kelvin(K) = {celsius_kelvin(float(celsius))}")
                print(f"Temperatura em Fahrenheit(F) = {celsius_fahrenheit(float(celsius))}")
            else:
                print(f"\n Até a proxima!")
                break
        except ValueError:
            print("\n Voce digitou um caractere inválido. \n Por favor insira um numero ou a letra 'q'.")

