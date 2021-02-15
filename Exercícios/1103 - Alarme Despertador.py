while True:
    h1, m1, h2, m2 = input().split(" ")
    h1 = int(h1)
    m1 = int(m1)
    h2 = int(h2)
    m2 = int(m2)

    if h1 == m1 == h2 == m2 == 0:
        break

    else:
        start = h1 * 60 + m1
        end = h2 * 60 + m2
        if end <= start:
            end += 24*60

        total = end - start

    print(abs(total))
