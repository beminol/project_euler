def is_digit_equal_power(a, b):
    c = str(a**b)
    if len(c) == b:
        return True


#print is_digit_equal_power(7, 5)
#print is_digit_equal_power(8, 9)

total = 0

for a in range(1, 100):
    for b in range(1, 100):
        if is_digit_equal_power(a, b) == True:
            print a**b, b
            total += 1

print total