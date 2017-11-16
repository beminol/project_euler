numbers_list = range(1000)

#print numbers_list

sum_numbers = 0

for number in numbers_list:
    if number%5 == 0 or number%3 == 0:
        #print number
        sum_numbers = sum_numbers + number

print(sum_numbers)