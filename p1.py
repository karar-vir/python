# Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
num=int(input('enter number between 1500 to 2700 :'))
if num>=1500 and num<=2700 :
        if num%7==0 and num%5==0:
                print('it is divisible 7 and multiple of 5 : ',num)
