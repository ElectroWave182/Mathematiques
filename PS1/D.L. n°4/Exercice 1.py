import math

x, pi = float(input("Mesure de l'angle, en radians/π : "))*math.pi, math.pi
while x > pi:
    x -= pi*2
while x <= -pi:
    x += pi*2
print("Mesure principale : " + str(x))