def power_of_digit(n):

    digit_list = list()
    sums = 0

    for i in str(n):
        digit_list.append(int(i))

    #print digit_list

    for i in digit_list:
        sums += i ** 5

    #print sums

    if n == sums:
        return n

    else:
        return None


total_sum = 0

for number in range(1, 1000000):
    if power_of_digit(number) == number:
        print number
        total_sum += number

print "Total:", total_sum-1



