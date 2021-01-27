n = int(input())
c = 0
for i in range(1, n+1):
    for j in range(0, 4):
        c += 1
        if j == 3:
            print("PUM")
        else:
            print(c, end=' ')
