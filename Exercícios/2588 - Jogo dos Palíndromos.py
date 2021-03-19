def palindromo(palavra, dicio):
    if len(palavra) == 0:
        return
    dicio[palavra[0]] = palavra.count(palavra[0])
    palavra = palavra.replace(palavra[0], '')
    palindromo(palavra, dicio)
    return dicio


while True:
    try:
        palavra = input()
        repete = {}
        cont = 0
        repete = palindromo(palavra, repete)
        for qtd in repete.values():
            if qtd % 2 != 0:
                cont += 1
        if cont >= 2:
            print(cont-1)
        else:
            print(0)

    except EOFError:
        break
