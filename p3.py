'''Write a Python program to guess a number between 1 to 9.

Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct,
on successful guess, user will get a "Well guessed!" message, and the program will exit.'''
import  random
while True:
        n=int(input('enter no 1 to 9 : '))
        if n>=1 and n<=9:
                n1=random.randint(1,n)
                if n1==n:
                        print("well gussed",n1)
                        break


	
