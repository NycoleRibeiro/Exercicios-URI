while True:
    try:
        n, m = input().split(" ")
        soma = 0

        for i in m:
            soma += int(i)
        print(soma, end=' ')

        if soma % 3 == 0:
            print("sim")
        else:
            print("nao")
    except EOFError:
        break