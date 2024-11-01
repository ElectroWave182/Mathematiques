def pgcd():
    print("PGCD(?)")
    a,b = int(input()),int(input())
    resteA,resteB = max([a,b]),min([a,b])
    while resteB != 0:
        resteC = resteA % resteB
        resteA,resteB = resteB,resteC
    return ("PGCD(" + str(a) + "," + str(b) + ") = " + str(resteA))
print(pgcd())
