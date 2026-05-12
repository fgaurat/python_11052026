import csv

def main():
    with open('sites_web_societes.csv') as file: # ouvrir le fichier en mode lecture, avec gestion automatique de la fermeture.'r' par défaut
        reader = csv.DictReader(file, delimiter=';') # créer un objet DictReader pour lire le fichier CSV en utilisant le point-virgule comme séparateur    
        for row in reader:
            print(row)
            print(row['name'])
            print(row['domain'])

if __name__ == '__main__':
    main()