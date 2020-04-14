print("This is Gusssing Game ")
import random
random_number=random.randrange(1,10)
guess=int(input('enter your number'))
correct=False
print(random_number)

while not correct:
    if random_number==guess:
        print("Congrates")
    elif random_number>guess:
        print('your no is low')
        break
    elif random_number<guess:
        print('your number is high')
        break
    else:
        print('invalid')
