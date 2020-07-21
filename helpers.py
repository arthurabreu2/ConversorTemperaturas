def celsius_kelvin(temperatura_celsius):
    """
    Função para converter a temperatura de Celsius para Kelvin
    :param temperatura_celsius:
    :return: temperatura em kelvin
    Formaula: C + 273.15
    """
    temperatura_kelvin = temperatura_celsius + 273.15
    return temperatura_kelvin

def celsius_fahrenheit(temperatura_celsius):
    """
    Função para converter temperatura de Celsius para Fahrenheit
    :param temperatura_celsius:
    :return: temperatura em fahrenheit
    Formula: (C * 9 / 5) + 32
    """
    temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32
    return temperatura_fahrenheit

def kelvin_fahrenheit(temperatura_kelvin):
    """
    Função que converte temperatura Kelvin para Fahrenheit
    :param temperatura_kelvin:
    :return: temperatura em fahrenheit
    Formula: (K - 273.15) * 9 / 5 + 32
    """
    temperatura_fahrenheit = (temperatura_kelvin - 273.15) * 9 / 5 + 32
    return temperatura_fahrenheit

def fahrenheit_kelvin(temperatura_fahrenheit):
    """
    Função para converter a temperatura Fahrenheit para Kelvin
    :param temperatura_fahrenheit:
    :return: temperatura kelvin
    Formula: ( F - 32) * 5 / 9 + 273.15
    """
    temperatura_kelvin = (temperatura_fahrenheit - 32) * 5 / 9 + 273.15