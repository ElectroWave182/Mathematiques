from sys import stdin, stdout
input, print = stdin.readline, stdout.write
def diviseurs(nb):
    racine = nb**0.5
    doublon = int(racine)
    liste = sorted(list(map(int, " ".join([str(div) + " " + str(nb // div) for div in range(1, int(racine + 1)) if nb % div == 0]).split())))
    if racine == doublon: liste.remove(doublon)
    return str(liste)
print(diviseurs(int(input())))
