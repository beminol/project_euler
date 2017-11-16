def digit_sum(n):
    sums = 0
    x = str(2 ** n)
    lst = list()

    for integer in x:
        lst.append(integer)

    print lst

    for integer in lst:
        sums += int(integer)

    return sums

print digit_sum(1000)