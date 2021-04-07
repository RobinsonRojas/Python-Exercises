from math import acos, cos, sin, radians


def distancia_puntos(punto_1, punto_2):
    punto_1 = (radians(punto_1[0]), radians(punto_1[1]))
    punto_2 = (radians(punto_2[0]), radians(punto_2[1]))

    distancia = acos(
        sin(punto_1[0]) *
        sin(punto_2[0]) +
        cos(punto_1[0]) *
        cos(punto_2[0]) *
        cos(punto_1[1] - punto_2[1]))
    return distancia * 6371.01


if __name__ == "__main__":

    # -------------------latitud--------Longitud
    punto_1 = (	37.141700744599994, -79.01640319820001)
    punto_2 = (37.491401670000002, -100.83000180000001)

    resultado = distancia_puntos(punto_1, punto_2)
    print('La distancia en kilómetros es: %f' % resultado)
    resultado = resultado / 1.609
    print('La distancia en millas es: %f' % resultado)
