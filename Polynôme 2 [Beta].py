from math import fabs,sqrt
def arr(val):
    nb = list(str("%.3f"%val))
    chf = nb[-1]
    while chf == "0":
        del nb[-1]
        chf = nb[-1]
    if chf == ".": del nb[-1]
    return "".join(nb)
def poly():
    print("Soit f(x) = ax² + bx + c\n\na: ")
    a = float(input())
    print("b: ")
    b = float(input())
    print("c: ")
    c = float(input())
    delta = b**2 - 4*a*c
    print("\nDiscriminant:",arr(delta))
    if delta > 0: print("Racine 1:",str(arr(-b - sqrt(delta))/(2*a)),"\nRacine 2:",str(arr(-b + sqrt(delta))/(2*a)))
    elif delta < 0:
        re,im = -b/(2*a),abs(sqrt(-delta)/(2*a))
        if a > 0: sign1,sign2 = " - "," + "
        else: sign1,sign2 = " + "," - "
        print("Racine 1: ",arr(re),sign1,arr(im),"i\nRacine 2: ",arr(re),sign2,arr(im),"i",sep = "")
    else: print("Racine double:",arr(-b/(2*a)))
poly()