dias = int(input("Quantos dias para a entrega: "))
valor = int(input("Qual valor do produto: "))

if dias > 7 or valor < 100:
    print("prioridade baixa")
elif dias <= 7 and dias >= 4:
    print("prioridade média")
elif dias < 4 or valor > 500:
    print("prioridade alta")