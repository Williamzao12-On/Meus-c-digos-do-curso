from math import log10

def menu():
    while True:
        print("Calculadora de escalas logaritimas")
        print("Selecione uma option \n" \
        "1 - Escala pH \n" \
        "2 - Escala richter \n" \
        "3 - Sair")
        opcao = int(input("Escolha"))

        if opcao == 1:
            ph()
        elif opcao == 2:
            richter()
        elif opcao == 3:
            print("Até Logo!")
            break
        else:
            print("Opção invalida")

def ph():
    print("Escala de pH")
    print("------------")

    while True:
        print("Para sair do progama, digite 0")
        h30 = float(input("Digite a quantidade de h30/mol na substância: "))

        if h30 == 0:
            print("Saindo")
            break

        else:
            ph = -1 * log10(h30)

            if ph > 0 and ph < 7:
                print(f'O pH de {ph:.2f} é considerado ácido')
            elif ph < 7 and ph <= 14:
                print(f'O pH de {ph:.2f} é considerado alcalino')
            elif ph == 7:
                print(f'O pH de 7 é considerado neutro')
            else:
                print("O pH não pode ser calculado")
    
def richter():
    print("Escala Richter")
    print("--------------")

    while True:
            print("Selecione uma opção abaixo: \n" \
            "1 - Joules para Magnetude \n" \
            "2 - Magnetude para Joules \n" \
            "3- Voltar ao menu principal")
            opcao = int(input("Opção Escolhida"))

            if opcao == 1:
                joules = float(input("Digite a quantidade de energia(Joules):"))
                if joules <= 0:
                    print("Quantidade de energia inválida")
                else:
                    res = (log10(joules) - 4.8) / 1.5
                    print(f'A Magnetude do terremoto é de {res:.2f} na escala Richter')
            elif opcao == 2:
                magnetude = float(input("Digite a magnetude do terremoto"))
                if magnetude <=0:
                    print("Magnetude inválida!")
                else:
                    res = 10 ** (1.5 * magnetude + 4.8)
                    print(f'A Magnetude equivale a {res:.2f} Joules de Energia')
            elif opcao == 3:
                break
        
menu()