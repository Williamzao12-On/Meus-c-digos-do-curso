def menu():
    print("selecione a Progressão desejada: \n" \
        "1~ Progressão aritimetica PA \n" \
        "2~ Progressão Geometrica PG")
    opcao = int(input("Escolha uma opção: "))
    num = int(input("selecione o 1° numero da Progressão:"))
    r = int(input("Escolha a Razão da progressão:"))
    match opcao:
        case 1:
            PA(num,r)
        case 2:
            PG(num,r)
        case _ :
            print("opção invalida!")

def PA(num,r):
    pa = []
    for i in range(10):
        termo = num + i + r
        pa.append(termo)
    print(pa)

def PG(num,r):
    pg = []
    for i in range(10):
        termo = num * r ** i
        PG.append(termo)
    print(pg)

menu()