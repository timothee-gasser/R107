choix=0
i=0
n=0
x=1
choix = input("Quelle boucle voulez vous utiliser?(for|while)")
n = int(input("Entrer la valeur d'un entier n:"))
if choix == "for":
    for i in range (1,n+1):
        print(f"{i}*{x}")
        x=i*x

elif choix == "while":
    while i<n:
        i=i+1
        print(f"{i}*{x}")
        x = i * x
else:
    exit("entrer un nom de boucle corect")

print(x)