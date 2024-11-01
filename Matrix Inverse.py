def inverse(ex):
    print(ex)
    a,b = map(int,input().split())
    c,d = map(int,input().split())
    det = a*d - b*c
    return str(d/det) + " " + str(-b/det) + "\n" + str(-c/det) + " " + str(a/det)
print(inverse("Entrez votre matrice...\nExemple:\n4 2\n6 9\n"))