from random import randint

def advinhacao():
    secreto = randint(0, 100)
    tentativas = 0

    while True:
        chute = int(input("Tenta chutar um número de 0 a 100 ai doido"))
        tentativas += 1

        if secreto > chute:
            print("Chutais baxo")
        elif secreto < chute:
            print("Chutais alto")
        else:
            print(f"Você conseguiu fazer o minimo da sua vida mero ser de possivel capacidade de inteligencia racional, o numero secreto era {secreto} e você errou {tentativas} vezes.")

while True:
    advinhacao()
    break
    continuar = str(input("Quer voltar a sofrer? s / n ?")). lower().strip()
    if continuar != "s":
        break