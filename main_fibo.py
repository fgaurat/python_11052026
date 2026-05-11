# import fibo as fb


# fb.fib(1000)

# values = fb.fib2(100)
# print(values)

# from fibo import fib, fib2
# from fibo import *

import fibo

a=1000

# hoisting => variable declaration is moved to the top of the scope
def scope():
    # Déclaration de la variable a dans la portée locale de la fonction scope
    global a
    a=2
    print(a)
    


def main():
    print("main_fibo name",__name__)
    fibo.fib(100)
    print("avant",a)
    scope()
    print("après",a)
    


if __name__ == "__main__":
    main()





