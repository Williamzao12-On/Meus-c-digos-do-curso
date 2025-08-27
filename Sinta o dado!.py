from random import randint

def main():
    while True:
        dados_batatas = [4, 6, 8, 10, 12, 20, 100]
        result = []
        print("--Simulador de RNG desgraçado--")
        dados = int(input("Escolhe ser humano"))
        if dados not in dados_batatas:
            print("digite um dado que exista")
            break
        else:
            quantidade = int(input("Quantos dados você quer rolar?"))
            if quantidade <= 0:
                print("Quantidade invalida! desgraçado")
            else:
                for i in range(quantidade):
                    rolagem = randint(1, dados)
                    result.append(rolagem)
            print(f'A soma das rolagens foram: {sum(result)}')
            print(f'As rolagens foram: {result}')
main()