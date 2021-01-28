n = int(input())

for i in range(0, n):
    exp = input().split()

    x = exp[:3]
    y = exp[4:]
    n1 = int(x[0])
    d1 = int(x[2])
    n2 = int(y[0])
    d2 = int(y[2])

    if '+' in exp:
        num = n1*d2 + n2*d1
        denom = d1*d2
    elif '-' in exp:
        num = n1*d2 - n2*d1
        denom = d1*d2
    elif '*' in exp:
        num = n1*n2
        denom = d1*d2
    else:
        num = n1*d2
        denom = n2*d1

    menor = denom
    if num < denom:
        menor = num

    print('{}/{} = '.format(num, denom), end='')
    for j in range(1, abs(menor)+1):
        if (num % j == 0) and (denom % j == 0):
            div_comum = j

    num = num//div_comum
    denom = denom//div_comum
    print('{}/{}'.format(num, denom))
