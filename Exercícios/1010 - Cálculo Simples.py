a, b, c = input().split(" ")

a = int(a)
b = int(b)
c = float(c)

d, e, f = input().split(" ")

d = int(d)
e = int(e)
f = float(f)

preco = (b*c)+(e*f)

print("VALOR A PAGAR: R$ {:.2f}".format(preco))
