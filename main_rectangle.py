# import rectangle
from rectangle import Rectangle
from carre import Carre

def main():
    try:
        r = Rectangle(4,2) # Constructeur de la classe Rectangle
        # print(r.longueur)
        # print(r.largeur)

        print(r.surface())

        c = Carre(5) # Constructeur de la classe Carre
        print(c.surface())
        c.set_cote(-10)
        print(c.surface())
        print(c.get_cote())
        print(c.get_cote())
    except Exception as e:
        print("Erreur:", e)

if __name__ == '__main__':
    main()