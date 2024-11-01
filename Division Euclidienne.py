from math import fabs
def divEucl():
    print("Entrez le dividende:")
    div1 = int(input())
    print("Entrez le diviseur:")
    div2 = int(input())
    if div2 == 0: return "Error 404: not found"
    div3 = abs(div2)
    return ("\nQuotient: " + str(div1*div2//div3**2 + (div2 - div3)//div2//2) + "\nReste: " + str(div1%div3))
print(divEucl())