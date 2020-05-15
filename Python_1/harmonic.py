l = []
def get_factors(num):
    res = []
    i = 1
    while i*i <= num:
        if num %i == 0:
            res.append(i)
            if not num//i == i:
                res.append(num//i)
        i += 1
    return res

i = 0
while not len(l) == 10:
    i += 1
    factors = get_factors(i)
    den = 0.0
    add = 0.0
    for j in factors:
        add += i/j
    den = float(add)/i
    h_mean = len(factors)/den
    if (h_mean) == int(h_mean):
        l.append(i)
print(l)
