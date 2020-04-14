#country is a default argument so if you don't give any value when we call the detail funtion
#it will automatically take the default country India otherwise if you give it will take that,and one thing
#will always keep remember default argument is always placed at the end not at the first like default parameter is hold after the name
#not before the name



def detail(name,country='India'):
    print('Hello',name,'Are you from ',country,"?")
detail('Karan','America')
