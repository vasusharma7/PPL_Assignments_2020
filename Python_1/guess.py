import numpy as np
try:
    d = int(input("Enter the difficulty level in scale of 1 to 10 : "))
except:
    print("You didn't enter a valid literal")
    exit(0)
thresh = 10**d
num = np.random.randint(1,thresh + 1)
count  = 0
while 1:
    try:
        x = int(input('Guess the number : '))
    except:
        print("You didn't enter a valid literal : Enter Again")
        continue
    if x == num:
        count += 1
        print("HOORAY ! You guessed it right !!")
        print("You took %d attempts"%count)
        break
    elif x < num:
        count  += 1
        print("The number is larger than you guessed : Guess Again")
    elif x > num:
        count += 1
        print("The number is smaller than you guessed : Guess Again")

