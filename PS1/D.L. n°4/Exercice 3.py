from math import *
import math

S = 1
for x in range(1,101):
    S += cos(x*math.pi/4)
print(S)