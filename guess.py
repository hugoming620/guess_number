#import random game
import random

r = random.randint(1, 100)

while True :
	number = input('猜數字：')
	number = int(number)
	if number == r :
		print('well done!')
		break
	elif number != r :
		print("wrong!")
		if number > r :
			print('it`s too bigger!')
		else :
			print('it`s too smaller!')

