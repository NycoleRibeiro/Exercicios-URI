x=1
y=0
while x!=y:
    x, y = (input("")).split(" ")
    x = int(x)
    y = int(y)
    if x < y:
        print ("Crescente")
    elif x > y:
        print ("Decrescente")
