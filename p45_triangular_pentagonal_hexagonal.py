def triangle_number_generator(n):

    tri_list = list()

    for i in range(1, n + 1):
        tri_list.append(i * (i + 1) / 2)

    return tri_list

def pentagonal_number_generator(n):

    penta_list = list()

    for i in range(1, n + 1):
        penta_list.append(i * (3 * i - 1) / 2)

    return penta_list

def hexagonal_number_generator(n):

    hexa_list = list()

    for i in range(1, n + 1):
        hexa_list.append(i * (2 * i - 1))

    return hexa_list

n = 200000

list_tri = triangle_number_generator(n)
list_penta = pentagonal_number_generator(n)
list_hexa = hexagonal_number_generator(n)

for number in list_tri:
    if number in list_penta and number in list_hexa:
        print number




