from time import*
n=int(input("Entrez votre valeur de N :"))
while not (n>0):
    n = int(input("N doit etre positif: "))
for i in range(n ,-1,-1):
    print(i)
    sleep(0.2)
