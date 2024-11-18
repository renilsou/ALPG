def exibirMenu():
    print('''=== SELECIONE UMA DAS OPÇÕES DE CONVERSÃO ABAIXO: ===
[1] - CELSIUS PARA KELVIN
[2] - KELVIN PARA CELSIUS
[3] - CELSIUS PARA FAHRENHEIT
[4] - FAHRENHEIT PARA CELSIUS
[5] - SAIR''')
    
def celsiusParaKelvin():
    celsius = float(input("\nINFORME A TEMPERATURA EM CELSIUS: "))
    kelvin = celsius + 273.15
    print(f"{celsius}°C EQUIVALE(M) A {kelvin:.2f} K")

def kelvinParaCelsius():
    kelvin = float(input("\nINFORME A TEMPERATURA EM KELVIN: "))
    celsius = kelvin - 273.15
    print(f"{kelvin} K EQUIVALE(M) A {celsius:.2f}°C")

def celsiusParaFahrenheit():
    celsius = float(input("\nINFORME A TEMPERATURA EM CELSIUS: "))
    fahrenheit = (celsius * 1.8) + 32
    print(f"{celsius}°C EQUIVALE(M) A {fahrenheit:.2f}°F")

def fahrenheitParaCelsius():
    fahrenheit = float(input("\nINFORME A TEMPERATURA EM FAHRENHEIT: "))
    celsius = (fahrenheit-32) * 1.8
    print(f"{fahrenheit}°F EQUIVALE(M) A {celsius:.2f}°C")

opcao = 0

while opcao != 5:
    exibirMenu()
    opcao = int(input("INFORME A OPÇÃO: "))

    match opcao:
        case 1:
            celsiusParaKelvin()
        case 2:
            kelvinParaCelsius()
        case 3:
            celsiusParaFahrenheit()
        case 4:
            fahrenheitParaCelsius()
        case 5:
            break
        case _:
            print("\nOPÇÃO INVÁLIDA\n")
            continue