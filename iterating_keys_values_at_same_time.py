#iterate keys and values at same time
person_information = {'city': 'San Francisco', 'name': 'Sam', "food": "shrimps"}
print(person_information.items())
for i,j in person_information.items():
    print("keys is : %s  and values is : %s" %(i,j))
    #print('value is : %s' %j)
    
    
