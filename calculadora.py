def menu():

    while True:
        print("CALCULAMENTO MENTAL BÁSICO")
        print("1 - Soma (+) \n" \
        "2 - Subtração (-) \n" \
        "3 - multiplicação (*) \n" \
        "4 - Divisão (/) \n" \
        "5 - Vazar")

        opção = int(input("Fale uma opção:"))

        if opção == 1:
            soma()
        elif opção == 2:
            subtração()
        elif opção == 3:
            multiplicação()
        elif opção == 4:
            divisão()
        elif opção == 5:
            break
        else:
            print("Opção inesistente")

def soma():
        num1 = int(input("Digite o primeiro numero"))
        num2 = int(input("Digite o segundo numero"))

        soma = num1 + num2

        print(f"O resultado da soma é {soma}")

def subtração():
        num1 = int(input("Digite o primeiro numero"))
        num2 = int(input("Digite o segundo numero"))

        subtração = num1 - num2

        print(f"O resultado da subtração é {subtração}")

def multiplicação():
        num1 = int(input("Digite o primeiro numero"))
        num2 = int(input("Digite o segundo numero"))

        multiplicação = num1 * num2

        print(f"O resultado da multiplicação é {multiplicação}")

def divisão():
        num1 = int(input("Digite o primeiro numero"))
        num2 = int(input("Digite o segundo numero"))

        divisão = num1 / num2

        print(f"O resultado da divisão é {divisão}")

menu()