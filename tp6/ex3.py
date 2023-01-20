def ajouter_elt(lst=[0,1,2], elt=3):
    lst.append(elt)
    return lst

print(ajouter_elt()) #a
print("ID lst : ",id(ajouter_elt()))#a
print(ajouter_elt())#b
print("ID lst : ",id(ajouter_elt()))#b
def ajouter_carac(ch = "abc", elt = "d"):#c
    return ch + elt#c

print(ajouter_carac())#d
print("ID ch : ",id(ajouter_carac()))#d
print(ajouter_carac())#e
print("ID ch : ",id(ajouter_carac()))#e