
dictionnaire1 = {
   (count-64) : chr(count) for count in range(65,95)      
}

dictionnaire2 = {
    (count+1) : chr(count) for count in range(0,26)
}

for lettre in dictionnaire1.values() :
    print (lettre)

print('-----------------------------------------------------')
    
for valeur in dictionnaire2.values() :
    print(valeur)
    
print({(count-64) : chr(count) for count in range(65,95)})

# Dictionnaire avec des voyelles

string = "awesome sauce"

print({vowel: string.count(vowel) for vowel in "awesome sauce" if vowel in ["a","e","i","o","u"]})