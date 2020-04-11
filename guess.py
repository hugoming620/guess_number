#import random game
import random

r = random.randint(1, 100)
count = 0
while True :
	count +=1 # count = count + 1 
	number = input('猜數字：')
	number = int(number)

	if number == r :
		print('well done!')
		print('this is the', count , 'th times you guess')
		break
	elif number != r :
		print("wrong!")
		if number > r :
			print('it`s too bigger!')
		else :
			print('it`s too smaller!')

	print('this is the', count , 'th times you guess')

