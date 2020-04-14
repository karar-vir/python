langs = ["haskell", "clojure", "apl"]
print(sorted(langs)) #sorted(langs) will return the new list bt it will not effect the original list
print('original list : ',langs)
langs.sort()        #langs.sort() will return the new sorted list placed at the previous list
print(langs)


#Reverse() funtion
print('original list : ',langs)
langs.reverse()
print(langs)


