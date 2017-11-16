# a**2 + b**2 = c**2
# a + b + c = 1000
# a < b < c
import math

def sr_sum(a, b):
    c = math.sqrt(a**2 + b**2)
    print "a:", a, "b:", b, "c:", c
    return a + b + c


print sr_sum(3, 4)



