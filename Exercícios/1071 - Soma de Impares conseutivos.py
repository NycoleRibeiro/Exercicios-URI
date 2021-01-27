x = int(input())
y = int(input())
soma = 0

if x < y:
    for i in range(x, y):
        if i % 2 != 0:
            soma += i

elif x > y:
    for i in range(x, y, -1):
        if i % 2 != 0:
            print(i)
            soma += i

print(soma)