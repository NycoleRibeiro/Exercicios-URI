while True:
    qt_emoticon, qt_frases = input().split()
    qt_emoticon = int(qt_emoticon)
    qt_frases = int(qt_frases)
    qt_mudanca = 0
    emoticons = []
    if qt_emoticon == 0 and qt_frases == 0:
        break

    for i in range(qt_emoticon):
        emoticons.append(input())

    for i in range(qt_frases):
        frases = input()
        for emoticon in emoticons:
            if emoticon in frases:
                qt_mudanca += frases.count(emoticon)
                frases = frases.replace(emoticon, ' ')

    print(qt_mudanca)
