a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

def menu():
    while True:
        print("Selecione a operação abaixo /n" \
        "1- Soma(+) /n" \
        "2- Subtração(-) /n" \
        "3- Multiplicação(.) /n" \
        "4- Divisão(/) /n" \
        "5- Se retire")
        opção = int(input("Selecione uma operação: "))

        if opção == 1:
            soma(a, b)
        elif opção == 2:
            subtração(a, b)
        elif opção == 3:
            multiplicação(a, b)
        elif opção == 4:
            divisão(a, b)
        elif opção == 5:
            break
        else:
            print("Opção inválida")

def soma(a, b):
    print(f'A soma de {a} mais {b} é {a + b}: ')

def subtração(a, b):
    print(f'A subtração de {a} menos {b} é {a - b}: ')

def multiplicação(a, b):
    print(f'A multiplicação de {a} multiplicado por {b} é {a * b}: ')

def divisão(a, b):
    print(f'A divisão de {a} dividido por {b} é {a / b}: ')


menu()