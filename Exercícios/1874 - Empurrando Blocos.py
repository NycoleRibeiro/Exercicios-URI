def insere(blocos, num):
    for i in range(1, qtd_colunas):
        for m in range(len(blocos)-1, -1, -1):
            linha = blocos[m]
            if linha[-i] == '0':
                linha[-i] = num
                return blocos
    return blocos


while True:
    qtd_linhas, qtd_colunas, tam_fila_nova = input().split()
    qtd_linhas = int(qtd_linhas)
    qtd_colunas = int(qtd_colunas)
    tam_fila_nova = int(tam_fila_nova)
    if qtd_linhas == 0:
        break

    blocos = []
    for i in range(0, qtd_linhas):
        linha = input().split(' ')
        blocos.append(linha)

    fila_nova = input().split(' ')
    for n in fila_nova:
        blocos = insere(blocos, n)

    for line in blocos:
        for atual in range(0, len(line)):
            print(int(line[atual]), end=' ')
        print('')
