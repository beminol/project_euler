def rule(n):

    if n % 2 == 0:
        n /= 2
    else:
        n = 3 * n + 1
    return n

count = 0
a = 9  # enter first number
lst = [a]

while True:
    x = rule(a)
    temp = rule(x)
    a = rule(temp)

    lst.append(x)
    lst.append(temp)
    lst.append(a)

    count += 3
    #print x, temp, a

    if a == 1: break

print "List:", lst,"\n", "iteration:", count





