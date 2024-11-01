from math import exp
def encadre(dec):
    for prec in range(dec + 1):
        a,x,y = 0.1**prec,0,2
        while y > 0:
            x += a
            y = x - exp(x) + 3
    return str(round(x - a,dec)) + " < a < " + str(round(x,dec))
print("Précision voulue :\n(en nombre de décimales)")
print(encadre(int(input())))