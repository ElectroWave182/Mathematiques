from math import *

cos = float(input("Pour x appartenant à ]-pi ; pi], saisir cos(x) = "))
cos = 5/6
if -1 <= cos <= 1:
    reponse = input('x appartient-il à ]0 ; pi] ? Répondre par "OUI" ou par "NON".')
    if reponse == "OUI":
        sin = sqrt(1 - cos*cos)
    else:
        sin = -sqrt(1 - cos*cos)
    print(sin)