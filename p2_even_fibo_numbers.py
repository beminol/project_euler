def fib(n):
    a, b = 1, 2
    for i in range(n - 1):
        a, b = b, a + b
    return a

lst = list()

for x in range(100):

    if fib(x) % 2 == 0:
        lst.append(fib(x))

    if fib(x) >= 4000000:
        #print "Value: ", fib(x - 1), ",", x, "th element"
        break

print lst, "\n", "Lenght of list: ", len(lst)

# print fib(0), fib(1), fib(2)

print "Sum of list:", sum(lst)
