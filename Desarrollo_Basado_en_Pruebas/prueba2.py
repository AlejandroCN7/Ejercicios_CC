import doctest

def sumar(a,b):
    """ Suma dos valores y devuelve su resultado

    Argumentos:
    a -- primer sumando
    b -- segundo sumando

    Test:
    >>> sumar(5,2)
    7
    >>> sumar(5,-3)
    2
    >>> sumar(3,-4)
    -1
    >>> sumar(0,0)
    1
    """

    return a+b


if __name__=="__main__":
    doctest.testmod()
