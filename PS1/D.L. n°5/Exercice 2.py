import sys
input,print = sys.stdin.readline,sys.stdout.write
print('Entrez le calcul ("rang_n", "suite", ou "mystère").\n')
fonction = input()
print('Entrez le nombre naturel "n".\n')
n = int(input())
def rang_n(n):
    return 2*n*n - n + 1
def suite(n):
    return [rang_n(i) for i in range(n + 1)]
def mystère(n):
    s = 0
    for i in range(n + 1):
        s += rang_n(i)
    return s
def affichage(nom,resultat):
    if fonction == nom:
        print(str(resultat))
affichage("rang_n\n",rang_n(n))
affichage("suite\n",suite(n))
affichage("mystère\n",mystère(n))