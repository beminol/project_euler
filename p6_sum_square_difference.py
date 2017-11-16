lst_10 = range(11)
lst_100 = range(101)

def sum_of_square(lst):
    sums = 0
    for element in lst:
        sums += element**2
    return sums

def square_of_sum(lst):
    sums = 0
    for element in lst:
        sums += element

    square = sums**2
    return square

def difference(lst):
    return square_of_sum(lst) - sum_of_square(lst)

print "Sum of squares 1 to 100 is:", sum_of_square(lst_100)
print "Square of sum 1 to 100 is:", square_of_sum(lst_100)
print "Difference:", difference(lst_100)

