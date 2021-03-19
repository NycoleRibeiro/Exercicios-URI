A = []
QUANTIDADE = 100

for i in range(QUANTIDADE):
    A.append(float(input('Digite: ')))

for j in range(QUANTIDADE):
    if(A[j] <= 10):
        print("A[{}] = {}".format(j, A[j]))
