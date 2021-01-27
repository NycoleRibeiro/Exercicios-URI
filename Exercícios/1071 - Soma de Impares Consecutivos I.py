#Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

x = int(input("Nº "))
y = int(input("Nº "))
soma = 0

if x < y:
    for i in range(x, y):
        if i % 2 != 0:
            soma += i