#HACKREARTH DNA into RNA
DNA=input()
DNA=['A','C','G','T']
for i in DNA:
    if i=='A':
        DNA='U'
        print(DNA)
        break
    elif  i=='C':
        DNA='G'
        print(DNA)
        break
    elif i=='G':
        DNA='C'
        print(DNA)
        break
    elif i=='T':
        DNA='A'
        print(DNA)
        break
    else:
        print('Invalid Input')
