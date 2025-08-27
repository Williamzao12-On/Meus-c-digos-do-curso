listinha = []

while True:
    print("Selecione uma opção abaixo: \n" \
    "1 - Adicionar um troço na lista \n" \
    "2 - Remover um treco da lista \n" \
    "3 - Limpar a bagaça toda \n" \
    "4 - Mostrar a bagaça \n" \
    "5 - Vazar")

    opções = int(input("Digite a opção que tu quer: "))

    if opções == 1:
        coisa = str(input("Bote alguma coisa para botar na listinha:"))
        listinha.append(coisa)
        print("Coisa botada na listinha")

    elif opções == 2:
      coisa = str(input("Escolha o coisa que vai tirar da listinha"))
      listinha.remove(coisa)
      print("Coisa expulsa da lista")
    
    elif opções == 3:
        listinha.clear()
        print("Jogou tudo fora")
    
    elif opções == 4:
        print(listinha)
    
    elif opções == 5:
        print("Valeu parceiro flw.")    
        break

    else:
        print("Escolhe o coisa que exista parça")
