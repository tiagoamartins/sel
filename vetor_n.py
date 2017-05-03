import operator


class VetorN:
    def __init__(self, *args):
        if not isinstance(args, tuple):
            raise TypeError
        self.values = args
        self.dim = len(args)

    def __str__(self):
        return str(self.values)

    def __add__(self, vec):
        if not isinstance(vec, VetorN) and vec.dim != self.dim:
            raise TypeError

        soma = map(operator.add, self.values, vec.values)
        return VetorN(*soma)
