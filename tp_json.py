import json

def main():
    with open("todos.json", "r") as f:
        todos = json.load(f)  # charger le contenu du fichier JSON dans une variable Python
        # print(todos)  # afficher la variable Python
        todo = todos[0]
        print(todo)  # afficher le premier élément de la liste
        print(todo['title'])  # afficher le premier élément de la liste
if __name__ == '__main__':
    main()



