Decoradores
===========

Demostração da utilização de decoradores para alteração da funcionalidade de
funções em Python.


Decorador que imprime "I got decorated" antes da função decorada

.. testcode::

        def make_pretty(func):
            def inner():
                print("I got decorated")
                func()
            return inner


        @make_pretty
        def ordinary():
            print("I am ordinary")

.. doctest::

        >>> ordinary()
        I got decorated
        I am ordinary

Utilizar o decorador ``@make_pretty`` se traduz em:

.. testcode::

        def not_ordinary():
            print("I am not ordinary")

.. doctest::

        >>> not_ordinary = make_pretty(not_ordinary)
        >>> not_ordinary()
        I got decorated
        I am not ordinary

Função decoradora que imprime 30 vezes o caractér '*' antes e depois da execução
da função decorada

.. testcode::

        def star(func):
            def inner(*args, **kwargs):
                print("*" * 30)
                func(*args, **kwargs)
                print("*" * 30)
            return inner

Função decoradora que imprime 30 vezes o caractér '%' antes e depois da execução
da função decorada

.. testcode::

        def percent(func):
            def inner(*args, **kwargs):
                print("%" * 30)
                func(*args, **kwargs)
                print("%" * 30)
            return inner

.. testcode::

        @star
        @percent
        def printer(msg):
            print(msg)

A utilização dessa função faz com que a mensagem seja decorada com linhas de '*'
e '%' antes e depois da mensagem, como no exemplo:

.. doctest::

        >>> printer("Hello")
        ******************************
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        Hello
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        ******************************
