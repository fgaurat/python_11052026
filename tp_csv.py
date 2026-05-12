
def main():
    # with open('sites_web_societes.csv', 'r') as file:
    with open('sites_web_societes.csv') as file: # ouvrir le fichier en mode lecture, avec gestion automatique de la fermeture.'r' par défaut
        # read_data = file.read()
        # print(type(read_data))
        # print(read_data)
        
        # for line in file:
        #     current_line = line.strip() # supprimer les espaces et les sauts de ligne
        #     columns = current_line.split(';') # séparer les éléments de la ligne en utilisant le point-virgule comme séparateur
        #     print(columns)

        lines = file.readlines() # lire toutes les lignes du fichier et les stocker dans une liste
        header = lines[0].strip().split(';') # extraire l'en-tête du fichier
        print(header)
        for line in lines[1:]: # parcourir les lignes à partir de la deuxième
            current_line = line.strip()
            columns = current_line.split(';')
            d = dict(zip(header, columns)) # créer un dictionnaire en associant les éléments de l'en-tête aux éléments de la ligne
            print(d)
            print(d['name'])
            print(d['domain'])

if __name__ == '__main__':
    main()