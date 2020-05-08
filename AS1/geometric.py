try:
    a = int(input("Enter a : "))
    r = int(input("Enter r : "))
    n = int(input("Enter number of terms of GP : "))
except:
    print("You entered invalid literals")
    exit(0)
for i in range(n):
    print(a*(r**i))