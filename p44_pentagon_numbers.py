def pentagon_numbers_generator(n):  # generates pentagon numbers list of n numbers

    pentagon_numbers_list = list()

    for i in range(1, n + 1):
        pentagon_numbers_list.append(i * (3 * i - 1) / 2)

    return pentagon_numbers_list

#print pentagon_numbers_generator(15)

lst1 = pentagon_numbers_generator(1000)
diff_list = list()

for no1 in lst1:
    for no2 in lst1:
        if no1 - no2 > 0:
            if no1 + no2 in lst1 and no1 - no2 in lst1:
                #print no1, no2
                diff_list.append(no1 - no2)

        else:
            if no1 + no2 in lst1 and no2 - no1 in lst1:
                diff_list.append(no2 - no1)


print diff_list
#print min(diff_list)
