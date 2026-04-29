a = int(input("Lado do triangulo: "))
b = int(input("Outro lado do triangulo: "))
c = int(input("Ultimo lado do triangulo: "))
perimetro = a + b + c
semiper = perimetro / 2
area = sqrt(semiper * (semiper - a) * (semiper - b) * (semiper - c))

if a == b == c: