# Desencipta C y retornas las P
def desencriptar():
    C = [100, 3275, 2694, 2578, 1695, 1480]
    s = 511
    z = 4087

    P = []

    for i, c in enumerate(C):
        P.append(pow(c, s) % z)

    print("P = ", P)


# Encripta las P y retornas las C
def encriptar():
    P = [1808,	1104,	1302,	408,	1806,	1411,	304,	1323]
    z = 2773
    n = 21

    C = []

    for p in P:
        C.append(pow(p, n) % z)

    print("C = ", C)


desencriptar()
encriptar()


def AckermanFunction(Number1, Number2):
    if Number1 == 0:
        return Number2 + 1
    else:
        if Number2 == 0:
            return (AckermanFunction(Number1 - 1, 1))
        return (AckermanFunction(Number1 - 1, AckermanFunction(Number1, Number2 - 1)))


print("A = ", AckermanFunction(2, 3))
