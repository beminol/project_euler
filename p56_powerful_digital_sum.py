def powerful_digit(a, b):
    return a**b

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

# print sum_digits(powerful_digit(99, 99))

list_max = list()

for a in range(1, 100):
    for b in range(1, 100):
        list_max.append(sum_digits(powerful_digit(a, b)))

print max(list_max)


