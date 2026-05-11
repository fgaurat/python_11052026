
def main():

    # f = open("tp_file.txt", "r")  # ouvrir le fichier en mode lecture
    # f = open("tp_file.txt", "a")  # ouvrir le fichier en mode ajout
    f = open("tp_file.txt", "w")  # ouvrir le fichier en mode écriture
    
    with open("tp_file.txt", "w") as f:  # ouvrir le fichier en mode écriture, avec gestion automatique de la fermeture
        
        for i in range(101):
            # f-string pour formater la chaîne de caractères
            l = f"Ligne {i:03d}"  # :03d pour afficher le nombre avec 3 chiffres, en ajoutant des zéros si nécessaire
            f.write(l + "\n")  # écrire la ligne dans le fichier
            # error !

    # f.close()  # fermer le fichier
        
if __name__ == '__main__':
    main()