import os
import datetime

file1 = input("Entrez le nom du premier fichier : ")
file2 = input("Entrez le nom du deuxième fichier : ")

if os.path.isfile(file1) and os.path.isfile(file2):

    print("Taille du fichier", file1, ":", os.path.getsize(file1), "octets")
    print("Taille du fichier", file2, ":", os.path.getsize(file2), "octets")

    mtime1 = os.path.getmtime(file1)
    mtime2 = os.path.getmtime(file2)
    if mtime1 > mtime2:
        print("Le fichier", file1, "est le plus récent, modifié le", datetime.datetime.fromtimestamp(mtime1))
    else:
        print("Le fichier", file2, "est le plus récent, modifié le", datetime.datetime.fromtimestamp(mtime2))
else:
    print("Au moins un des fichiers spécifiés n'existe pas.")