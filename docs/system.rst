Interagindo com o sistema
=========================

Exemplo de utilização de argumentos passados pelo sistema

.. testcode::

        import sys

        if __name__ == '__main__':
            if len(sys.argv) < 3:
                print("Poucos argumentos")
            else:
                print("WOOOOOOOWWWWWWW!!!!")
                print(sys.argv)

            sys.exit("Usage: {} non-sense string".format(sys.argv[0]))
