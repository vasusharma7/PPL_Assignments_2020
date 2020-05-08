try:
    x = int(input("Enter starting number :"))
    y = int(input("Enter terminating number :"))
except:
    print("Enter a valid number :(")
    exit(0)
l = []
def armstrong(x):
    x = str(x)
    t = sum([int(i)**3 for i in x])
    return t
for i in range(x,y+1):
    if i == armstrong(i):
        l.append(i)
print(l)