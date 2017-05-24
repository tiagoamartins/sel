"""
Demostração da utilização de decoradores para alteração da
funcionalidade de funções em Python.
"""


def make_pretty(func):
    """
    Decorador que imprime "I got decorated" antes da função decorada
    """
    def inner():
        print("I got decorated")
        func()
    return inner


@make_pretty
def ordinary():
    """
    Utilizar o decorador '@make_pretty' se traduz em:
        >>> ordinary = make_pretty(ordinary)
        >>> ordinary()
    """
    print("I am ordinary")


def star(func):
    """
    Função decoradora que imprime 30 vezes o caractér '*' antes e depois
    da execução da função decorada
    """
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    """
    Função decoradora que imprime 30 vezes o caractér '%' antes e depois
    da execução da função decorada
    """
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    """
    A utilização dessa função faz com que a mensagem seja decorada
    com linhas de '*' e '%' antes e depois da mensagem, como no exemplo:
        >>> printer("Hello")
        ******************************
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        Hello
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        ******************************
    """
    print(msg)
