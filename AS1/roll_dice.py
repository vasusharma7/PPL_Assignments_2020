import numpy as np
while 1:
	x = input("Press 'r' to roll the dice and 'q' to exit")
	if x == 'r':
		print(np.random.randint(1,7)
	elif x == 'q':
		break
	else:
		continue
