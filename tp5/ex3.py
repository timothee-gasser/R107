chaine = input("Entrez un mot ou une phrase : ")
chaine = chaine.lower()
chaine_pur = ""

for c in chaine:
    if c.isalpha():
        chaine_pur += c

if chaine_pur == chaine_pur[::-1]:
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")