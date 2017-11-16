import math

def factorial_sum(n):

    digit_list = list()
    sums = 0

    for i in str(n):
        digit_list.append(int(i))

    #print digit_list

    for number in digit_list:
        sums += math.factorial(number)

    #print sums

    if sums == n:
        return sums
    else:
        return 0

sums2 = 0

for i in range(1, 10000000):
    sums2 += factorial_sum(i)

print sums2 - 3 # 1! and 2! are not included







