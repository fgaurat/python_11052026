# Procédure => une fonction qui ne retourne rien
def toto():
    print("toto")


# Fonction => une fonction qui retourne une valeur
def add(a: int, b: int) -> int:
    """
    Additionne deux nombres.
    Args:
        a (int): le premier nombre
        b (int): le deuxième nombre
    Returns:
        int: la somme des deux nombres
    """
    r = a + b
    return r

# Fonction avec des paramètres par défaut


def add2(a: int = 0, b: int = 0) -> int:
    r = a + b
    return r


# passage de paramètres par position
c = add(1, 2)
print(c)  # 3

c = add2()
print(c)  # 0

# passage de paramètres par nom
c = add2(a=4, b=45)
print(c)  # 49

c = add2(b=45, a=4)
print(c)  # 49
print(50 * "-")

# fonction avec un nombre variable de paramètres passés par position


def add3(*args):  # args=(1, 2, 3)
    r = 0

    for a in args:  # a=3
        # r = r+a # r=1+2=3 = 3+3=6
        r += a  # r = r+a
    return r


c = add3(1, 2, 3)
print(c)
c = add3(1, 2, 3, 5, 6)
print(c)

# fonction avec un nombre variable de paramètres passés par nom


def hello(**kwargs):  # kwargs={"name":"toto", "age": 49}
    print(kwargs)
    print("Hello " + kwargs["name"] + " tu as " + str(kwargs["age"]) + " ans")


hello(name="toto", age=49, job="dev")

print(50 * "-")


def mult2(the_list):
    """ 
    Multiplie par 2 les éléments d'une liste 
    Args:
        the_list (list): la liste à traiter
    Returns:
        list: la liste avec les éléments multipliés par 2
    """
    list_result = []
    for v in the_list:
        r = v*2
        list_result.append(r)

    return list_result


def map_mult2(i):
    return i*2


l = [1, 2, 3, 4, 5]

l2 = mult2(l)

print(l2)  # [2, 4, 6, 8, 10]
# l2 = map( map_mult2, l)
# l2 = map( lambda i: i*2, l)
l2 = list(map(lambda i: i*2, l))
# l2 = list(l2)

# print(l2)

for i in l2:
    print(i)


lines = ["  toto  ", " titi   ", " tutu   "]

clean_lines = list(map(lambda l: l.strip(), lines))
print(lines)  # ['  toto  ', ' titi   ', ' tutu   ']
print(clean_lines)  # ['toto', 'titi', 'tutu']
