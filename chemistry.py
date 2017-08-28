#!/usr/bin/env python3

import math

def nernst(e, cox, cred, z=1):
    return e + ((0.059 / z) * math.log10(cox / cred))

ph = 0

while ph <= 14:
    print(str(ph) + ": " + str(round(nernst(0.4, 1, 10**(-(14-ph))), 2)))
    ph += 1



# 1. print(str(ph) + ": " + str(round(nernst(1.23, 10**(-ph), 1), 2)))
# 2. print(str(ph) + ": " + str(round(nernst(-0.83, 10**(-ph), 1), 2)))
# 3. print(str(ph) + ": " + str(round(nernst(-0.83, 1, 10**(-(14-ph))), 2)))
# 4. print(str(ph) + ": " + str(round(nernst(0.4, 1, 10**(-(14-ph))), 2)))