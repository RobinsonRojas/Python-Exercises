# #Usando el sistema RSA
# #diccionario:
# #A=00
# B=01 C=02 D=03 E=04 F=05 G=06 H=07 I=08 J=09 K=10 L=11 M=12 N=13 
# Ñ=14 O=15 P=16 Q=17 R=18 S=19 T=20 U=21 V=22 W=23 X=24 Y=25 Z=25

# # Desencipta C y retornas las P
def desencriptar():
    C = [100, 3275, 2694, 2578, 1695, 1480]
    s = 511
    z = 4087

    P = []

    for i, c in enumerate(C):
        P.append(pow(c, s) % z)

    print("P = ", P)
desencriptar()

# Encripta las P y retornas las C 
def encriptar():
    P = [1808,	1104,	1302,	408,	1806,	1411,	304,	1323]
    z = 2773
    n = 21

    C = []

    for p in P:
        C.append(pow(p, n) % z)

    print("C = ", C)



encriptar()


def AckermanFunction(Number1, Number2):
    if Number1 == 0:
        return Number2 + 1
    else:
        if Number2 == 0:
            return (AckermanFunction(Number1 - 1, 1))
        return (AckermanFunction(Number1 - 1, AckermanFunction(Number1, Number2 - 1)))


print("A = ", AckermanFunction(2, 3))
