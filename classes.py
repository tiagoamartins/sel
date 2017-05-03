"""
>>> rex = Cao('Rex')
>>> rex.qtd_patas
4
>>> rex.nome
'Rex'
>>> rex.latir()
Rex: Au! 
>>> rex.latir(5)
Rex: Au! Au! Au! Au! Au! 
>>> rex.nervoso
False
>>> rex.nervoso = True
>>> rex.latir()
Rex: Au! Au! 
>>> rex.latir(5)
Rex: Au! Au! Au! Au! Au! Au! Au! Au! Au! Au! 

>>> nana = GoldenRetriever('Nana')
>>> nana.nome
'Nana'
>>> nana.nervoso
False
>>> nana.carnívoro
True
>>> nana.latir()
Nana: Au! 
>>> nana.latir(5)
Nana: Au! Au! Au! Au! Au! 
>>> nana.itens
[]
>>> nana.pega('bola')
Nana pegou bola
>>> nana.itens
['bola']
>>> nana.devolve()
Nana devolve bola
'bola'
>>> nana.devolve()
Nana não está segurando item algum!

>>> toto = GoldenRetriever('Totó')
>>> toto.nome
'Totó'
>>> toto.itens
[]
>>> toto.pega('chinelo')
Totó pegou chinelo
>>> toto.pega('bola')
Totó pegou bola
>>> toto.itens
['chinelo', 'bola']
>>> toto.devolve_ultimo()
'bola'
>>> toto.devolve('meia')
Totó não está segurando meia!
>>> toto.devolve('chinelo')
Totó devolve chinelo
'chinelo'
>>> toto.devolve_ultimo()
Totó não está segurando item algum!

>>> from datetime import date
>>> totó = GoldenRetriever('Totó', date(2017, 4, 26))
>>> totó.data_nascimento
datetime.date(2017, 4, 26)
>>> print(totó.data_nascimento)
2017-04-26
>>> fido = GoldenRetriever('Fido')
>>> print(fido.data_nascimento)
None

>>> mimi = Pinscher('Mimi')
>>> mimi.nervoso
True
>>> mimi.nome
'Mimi'
>>> mimi.latir()
Mimi: Au! Au! Au! Au! 
>>> mimi.latir(5)
Mimi: Au! Au! Au! Au! Au! Au! Au! Au! Au! Au! Au! Au! Au! Au! Au! Au! Au! Au! Au! Au! 

>>> isinstance(mimi, GoldenRetriever)
False
>>> isinstance(mimi, Pinscher)
True
>>> isinstance(mimi, Cao)
True
"""


class Cao:
    qtd_patas = 4
    carnívoro = True
    nervoso = False

    def __init__(self, nome, data_nascimento=None):
        self.nome = nome
        self.data_nascimento = data_nascimento

    def latir(self, vezes=1):
        """ Latir do cão. Quanto mais nervoso mais late. """

        vezes += self.nervoso * vezes
        latido = 'Au! ' * vezes
        print('{}: {}'.format(self.nome, latido))


class GoldenRetriever(Cao):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.itens = []

    def pega(self, item):
        """ busca/pega um item quando ordenado """
        self.itens.append(item)
        print('{} pegou {}'.format(self.nome, item))

    def devolve(self, item=None):
        """ devolve um item, caso o item não seja especificado retorna o último """
        if not self.itens:
            print('{} não está segurando item algum!'.format(self.nome))
            return

        if not item:
            item = self.itens.pop()
        elif item not in self.itens:
            print('{} não está segurando {}!'.format(self.nome, item))
            return
        else:
            self.itens.remove(item)
        print('{} devolve {}'.format(self.nome, item))
        return item

    def devolve_ultimo(self):
        if not self.itens:
            print('{} não está segurando item algum!'.format(self.nome))
            return

        return self.itens.pop()


class Pinscher(Cao):
    nervoso = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def latir(self, vezes=1):
        vezes *= 2
        super().latir(vezes)
