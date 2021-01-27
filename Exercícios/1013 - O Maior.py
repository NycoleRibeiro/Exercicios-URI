A, B, C = input().split(' ')
A = int(A)
B = int(B)
C = int(C)
MaiorAB = (A + B + abs(A - B))/2
print("{:.0f} eh o maior".format((MaiorAB + C + abs(MaiorAB - C))/2))
