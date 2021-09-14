f=open('poem.txt','r').read()
def vowels(string):
    string=string.lower()
    all_vowels={
        'a':0,
        'e':0,
        'i':0,
        'o':0,
        'u':0
        }
    for i in list(all_vowels.keys()):
        all_vowels[i]=string.count(i)
    return all_vowels

def cases(string):
    upper=0
    lower=0
    for i in string:
        if i.isupper():
            upper+=1
        if i.islower():
            lower+=1
    return {'upper':upper,'lower':lower}

vowel_dict=vowels(f)
for key in list(vowel_dict.keys()):
    print(key.upper(),":",vowel_dict[key])

ul=cases(f)
print("Total upper case:",ul['upper'])
print("Total lower case:",ul['lower'])
