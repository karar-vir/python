#factorial

no=int(input('enter any to check its factorial : '))

fact=1

if no<=1:
    fact=fact+1
    print(fact)
else:
    for i in range(1,no+1):
        fact=fact*i
    print(fact)
