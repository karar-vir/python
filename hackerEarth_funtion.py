def string_multiplier(string_arg, number):
     '''takes the string_arg and multiplies it with one more than the number'''
     return string_arg * (number + 1)


# passing string_arg and number and in that order...
print(string_multiplier('a', 5))        #aaaaaa




langs = ["haskell", "clojure", "apl"]
langs.append(["kite"])
langs.extend(["scala"])
print(langs)
print(langs.index("scala"))
['haskell', 'clojure', 'apl', 'scala', 'F#']
