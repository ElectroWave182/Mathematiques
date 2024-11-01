from string import digits
from sys import stdout
print = stdout.write


def valide(entre):
    for char in entre:
        if not char in digits + " +-.i":
            return False
    return True


def impur(z):
    return "+" in z or "-" in z.lstrip("-")


def zero(re):
    return "".join(re.split()) == "+0"


def parts(cplx):
    cplx = "".join(cplx.split()).lstrip("+")
    neg = cplx[0] == "-"
    if "+" in cplx:
        cplx = cplx.rstrip("i").split("+")
    elif "-" in cplx.lstrip("-"):
        cplx = list(cplx.rstrip("i").lstrip("-").split("-"))
        cplx[1] = "-" + cplx[1]
        if neg:
            cplx[0] = "-" + cplx[0]
    elif "i" in cplx:
        cplx = ("0", cplx.rstrip("i"))
    else:
        cplx = (cplx, "0")
    im = cplx[1]
    if im == "-" or im == "":
        cplx = cplx[0], im + "1"
    return map(float, cplx)


def arr(part):  # Cette fonction retourne l'arrondi d'une valeur *part* flottante
    ent, dec = str(part).split(".")
    if "e-" in dec:
        return "0"
    if "e" in dec:
        return "{résultat ⩾ 10 billards}"
    nb = len(ent.lstrip("-"))
    if int(dec[:3]) == 0:
        return ent
    if ent == "0" or ent == "-0":
        return ent + "." + dec[:3].rstrip("00")
    if nb < 3:
        return ent + "." + dec[:3 - nb].rstrip("0")
    return ent


def rAff(rew, imw):
    nul, sRew, sImw = "0", arr(rew), arr(imw)
    rewZ, imwZ = sRew.lstrip("-") == nul, sImw.lstrip("-") == nul
    if sImw.lstrip("-") == "1":
        sImw = sImw[0].lstrip("1")
    if rewZ and imwZ:
        print("0")
    elif rewZ:
        print(sImw + "i")
    elif imwZ:
        print(sRew)
    elif imw > 0:
        print(sRew + " + " + sImw + "i")
    else:
        print(sRew + " - " + sImw.lstrip("-") + "i")


def final(e, f, reb, imb, rew, imw):
    return ((rew - reb) * e + (imw - imb) * f) / (2 * (e**2 + f**2))


def poly():

    print("Entrez vos coefficients a, b, et c complexes (sous la forme algébrique) tels que votre polynôme s'exprime : ax² + bx + c, avec x un complexe...\n")
    while True:
        a = input("...x² + bx + c -> ")
        aImpur = impur(a)
        if aImpur:
            b = input("(" + a + ")x² + ...x + c -> ")
        else:
            b = input(a + "x² + ...x + c -> ")
        bImpur = impur(b)
        if not bImpur and b.lstrip(" ")[0] != "-":
            b = "+ " + b
        if zero(b) and aImpur:
            c = input("(" + a + ")x² + ... -> ")
        elif zero(b):
            c = input(a + "x² + ... -> ")
        elif aImpur and bImpur:
            c = input("(" + a + ")x² + (" + b + ")x + ... -> ")
        elif aImpur:
            c = input("(" + a + ")x² " + b + "x + ... -> ")
        elif bImpur:
            c = input(a + "x² + (" + b + ")x + ... -> ")
        else:
            c = input(a + "x² " + b + "x + ... -> ")
        if c.lstrip(" ")[0] != "-":
            c = "+ " + c

        if valide(a) and valide(b) and valide(c) and a.strip(" ") != 0:
            if aImpur:
                print("(" + a + ")x² ")
            else:
                print(a + "x² ")
            if not zero(b):
                if bImpur:
                    print("+ (" + b + ")x ")
                else:
                    print(b + "x ")
            if not zero(c):
                print(c)
            break
        else:
            print("Votre entrée est cassée.\n")

    print("\nDiscriminant : ")
    rea, ima = parts(a)
    reb, imb = parts(b)
    rec, imc = parts(c)
    red, imd = reb**2 - imb**2 - 4 * (rea * rec - ima * imc), 2 * reb * imb - 4 * (ima * rec + rea * imc)
    rAff(red, imd)

    print("\nRacines du discriminant : ")
    mod = (red**2 + imd**2)**0.5
    rew1, imw1 = (mod + red) / 2, (mod - red) / 2
    if imd < 0:
        imw1 *= -1
    rew2, imw2 = -rew1, -imw1
    rAff(rew1, imw1)
    rDouble = rew1 != rew2 or imw1 != imw2
    if rDouble:
        print(" et ")
        rAff(rew2, imw2)

    print("\nRacines du polynôme :o ")
    rer1, imr1 = final(rea, ima, reb, imb, rew1, imw1), final(ima, rea, reb, imb, rew1, imw1)
    rAff(rer1, imr1)
    if rDouble:
        print(" et ")
        rer2, imr2 = final(rea, ima, reb, imb, rew2, imw2), final(ima, rea, reb, imb, rew2, imw2)
        rAff(rer2, imr2)


poly()

# Todo: Install isort
