numeros = [2, 26, 7, 10, 3, 347, 1223, 1, 8, 19, 8, 30]
pares = []
impares = []

for i in numeros:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(f'Os numeros pares são: {pares}')
print(f'Os numeros impares são: {impares}')