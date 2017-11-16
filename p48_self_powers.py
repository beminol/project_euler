self_power = lambda x: x**x

sums = 0

for i in range(1, 1001):
    #print i, self_power(i)
    sums += self_power(i)

print "sums:", sums