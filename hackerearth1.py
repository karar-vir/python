#HackerEarth print the no of letter of each word from the list
lst=['apple','mango','banana']
string_count=0
for fruits in lst:
   
    for words in fruits:
        string_count+=1
   # print(fruits,' has ',string_count,'characters.')
    print('%s has %d characters'%(fruits,string_count))
print('fruits in list : ',lst)
