def fact(n):
    pro = 1
    while True:
        pro *= n
        n = n-1
        if n == 0: break

    return pro

print fact(100)

def fact_sum(k):
    sums = 0
    for i in str(k):
        sums += int(i)

    return sums

print fact_sum(fact(100))
