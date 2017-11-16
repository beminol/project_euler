def sum_if_pisagor(a, b, c):
    if c**2 == a**2 + b**2:
        return a + b + c
    else:
        return False

temp_list = list()

for a in range(1, 121):
    for b in range(1, 121):
        for c in range(1, 121):
            if sum_if_pisagor(a, b, c) is not False:
                #print a + b + c, ",", a, b, c
                temp_list.append(a+b+c)

print list(set(temp_list))
print temp_list