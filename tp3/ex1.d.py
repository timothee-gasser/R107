n=int(input("Entrez votre valeur de N :"))
y=0
x=0
while x<n:
    y=y+1
    x=x+y
if x !=n:
    print("Impossible")
else:
    print(y)