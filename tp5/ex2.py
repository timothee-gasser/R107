x1 = str(input("Veuillez entrer la note du module 1 et le coefficient correspondant :"))
x1 = x1.split(" ");
y1 = int(x1 [0]);
if y1 < 0 or y1 > 20 :
    print("valeur incorect")
    exit()
if y1 < 8 :
    print("non admis")
    exit()
z1 = int(x1 [1]);
m1 = y1 * z1


x2 = str(input("Veuillez entrer la note du module 2 et le coefficient correspondant :"))
x2 = x2.split(" ");
y2 = int(x2 [0]);
if y2 < 0 or y2 > 20 :
    print("valeur incorect")
    exit()
if y2 < 8 :
    print("non admis")
    exit()
z2 = int(x2 [1]);
m2 = y2 * z2


x3 = str(input("Veuillez entrer la note du module 3 et le coefficient correspondant :"))
x3 = x3.split(" ");
y3 = int(x3 [0]);
if y3 < 0 or y3 > 20 :
    print("valeur incorect")
    exit()
if y3 < 8 :
    print("non admis")
    exit()
z3 = int(x3 [1]);
m3 = y3 * z3


x4 = str(input("Veuillez entrer la note du module 4 et le coefficient correspondant :"))
x4 = x4.split(" ");
y4 = int(x4 [0]);
if y4 < 0 or y4 > 20 :
    print("valeur incorect")
    exit()
if y4 < 8 :
    print("non admis")
    exit()
z4 = int(x4 [1]);
m4 = y4 * z4


x5 = str(input("Veuillez entrer la note du module 5 et le coefficient correspondant :"))
x5 = x5.split(" ");
y5 = int(x5 [0]);
if y5 < 0 or y5 > 20 :
    print("valeur incorect")
    exit()
if y5 < 8 :
    print("non admis")
    exit()
z5 = int(x5 [1]);
m5 = y5 * z5

an = m1 + m2 + m3 + m4 + m5
ac = z1 + z2 + z3 + z4 + z5
r = an/ac
if r < 10:
    print("Non admis")

else:
    print("Admis")