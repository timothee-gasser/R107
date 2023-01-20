L1 = [0]*3
print("Liste initiale :",L1)
print("Type de la liste :",type(L1))
print("Identifiant de la liste :",id(L1))

print("Type et identifiant des éléments de la liste initiale :")
for i in L1:
    print("Type :",type(i)," Identifiant :",id(i))

L1[1] += 1
print("Liste après modification :",L1)
print("Type de la liste :",type(L1))
print("Identifiant de la liste :",id(L1))

print("Type et identifiant des éléments de la liste après modification :")
for i in L1:
    print("Type :",type(i)," Identifiant :",id(i))