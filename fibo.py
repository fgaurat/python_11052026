# Fibonacci numbers module


def fib(n):
    """Write Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    """Return Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b

    return result

if __name__ == "__main__":

    print("fibo name",__name__)# double underscore => dunder => dunder name

    print(50*'-')
    fib(100)
    print(50*'-')
    r = fib2(100)
    print(r)
    print(50*'-')