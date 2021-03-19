n = int(input())
for i in range(n):
    kg = float(input())
    dias = 0
    while kg > 1:
        dias += 1
        kg = kg/2
    print("{} dias".format(dias))
