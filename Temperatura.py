def menu():
    print("CONVERSOR DE TEMPERATURA\n" \
    "1 - Celsius pra Fahrenheit \n" \
    "2 - Fahrenheit para Celsius \n" \
    "3 - Celsius para Kelvin \n" \
    "4 - Fahrenheit para Kelvin \n" \
    "5 - Kelvin para Celsius \n" \
    "6 - Kelvin para Fahrenheit")
    opção = int(input("Escolhe uma opção: "))
    Temperatura = float(input("Digite a temperatura que sera convertida: "))

    match opção:
        case 1:
            CpF(Temperatura)
        case 2:
            FpC(Temperatura)
        case 3:
            CpK(Temperatura)
        case 4:
            FpK(Temperatura)
        case 5:
            KpC(Temperatura)
        case 6:
            KpF(Temperatura)
        case _:
            print("Opção não existe")
        
def CpF(X):
    res = (X * (9/5)) + 32
    print(f'{X}ºC equivalem a {res:.2f}ºF')

def FpC(X):
    res = (X- 32) * (5/9)
    print(f'{X}ºF equivalem a {res:.2f}ºC')

def CpK(X):
    res = X + 273.15
    print(f'{X}ºC equivalem a {res:.2f}ºK')

def FpK(X):
    res = (X - 32) * (5/9) + 273.15
    print(f'{X}ºF equivalem a {res:.2f}ºK')

def KpC(X):
    res = X - 273.15
    print(f'{X}ºK equivalem a {res:.2f}ºC')

def KpF(X):
    res = (X - 273.15) * (9/5)
    print(f'{X}ºK equivalem a {res:.2f}ºF')

menu()