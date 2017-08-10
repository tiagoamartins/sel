from unittest import TestCase

from tuple_vector import Vetor, soma_vetor, subtrai_vetor


class TestVetor(TestCase):
    """
    Verifica a funcionalidade da tupla ``Vetor``
    """

    def test_vetor(self):
        """
        Verifica a atribuição da tupla ``Vetor``
        """

        v = Vetor(x=1, y=-1)
        self.assertEqual(v.x, 1)
        self.assertEqual(v.y, -1)

    def test_soma(self):
        """
        Verifica soma de duas tuplas ``Vetor``
        """

        v1 = Vetor(5, 1)
        v2 = Vetor(0, 3)
        v = soma_vetor(v1, v2)
        self.assertEqual(v, Vetor(5, 4))

    def test_subtrai(self):
        """
        Verifica subtração de duas tuplas ``Vetor``
        """
        v1 = Vetor(5, 1)
        v2 = Vetor(2, 3)
        v = subtrai_vetor(v1, v2)
        self.assertEqual(v, Vetor(3, -2))
