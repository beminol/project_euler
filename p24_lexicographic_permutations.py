import itertools

def function(n):

    n = str(n)
    number_list = list()

    lexi_list = list()

    for number in n:
        number_list.append(int(number))

    print number_list

    combi_list = itertools.combinations(number_list, len(number_list))

    print combi_list




function(3124)
