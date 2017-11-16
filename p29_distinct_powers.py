def dis_power(a1, a2, b1, b2):

    list_a = range(a1, a2 + 1)
    list_b = range(b1, b2 + 1)
    temp_list = list()
    comb_list = list()

    #print "a:", list_a, "\n", "b:", list_b

    for a in list_a:
        for b in list_b:
            temp_list.append(a ** b)

    comb_list = list(set(temp_list))    # remove duplicates
    comb_list.sort()

    #print comb_list
    print "Length:", len(comb_list)


dis_power(2, 100, 2, 100)

