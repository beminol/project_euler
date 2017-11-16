def perfect_number(n):

    all_list = range(n + 1)
    all_list.remove(0)
    divisor_list = list()

    for i in all_list:
        if n % i == 0:
            divisor_list.append(i)

    divisor_list.remove(n)
    print divisor_list

    print "Sum of all divisors:", sum(divisor_list)

    if sum(divisor_list)  == n:
        print n, "IS A PERFECT NUMBER !"

    elif sum(divisor_list) > n:
        print n, "is a abundant number"

    else:
        print n, "is a deficient number"

    return sum(divisor_list)


perfect_number(28122)



