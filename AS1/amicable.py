def sumOfFactors(num):
    i = 1
    sum = -num
    while i*i <= num:
        if num %i == 0:
            sum += i
            if not num//i == i:
                sum += num//i
        i += 1
    return sum

x = 0
fact_sum = []
inv_fact_sum  = []
def generate():
    global x
    n = len(fact_sum) + 40000
    for i in range(x,n):
        t = sumOfFactors(i)
        if not i == t:
            fact_sum.append((i,t))
amicable = []


while 1:
    generate()
    for entry in fact_sum:
        inv_fact_sum.append((entry[1],entry[0]))
    amicable = list(set(fact_sum) & set(inv_fact_sum))
    for i in amicable:
        if (i[0],i[1]) in amicable and (i[1],i[0]) in amicable:
            amicable.remove((i[0],i[1]))
    if len(amicable) >= 10:
        break
    amicable = sorted(amicable,key=lambda x: x[0] > x[1])
print(amicable[:])