
def main():
    try:
        a = 2
        b = "0"
        c = a / b
        print(c)
    except ZeroDivisionError as e: # Gestion de l'exception
        print("Erreur",e)
    except TypeError as e: # Gestion de l'exception
        print("Erreur",e)
    except Exception as e: # Gestion de toutes les autres exceptions
        print("Erreur",e)    

    print("Fin du programme")
if __name__ == '__main__':
    main()