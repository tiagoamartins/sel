favorites = {
    "appetizer": "calamari",
    "vegetable": "broccoli",
    "beverage": "coffee",
}


def describe(category):
    """
    Esse exemplo serve para demonstrar a utilização de dicionários.
    A utilização dos colchetes [] para obtenção do elemento a partir da
    chave causa exceção 'KeyError' quando a chave não existe no dicionário.
    Entretanto, a função 'get' do dicionário retorna 'None' e não causa
    exceção quando a chave buscada não é encontrada.

    >>> categories = ['beverage', 'vegetable', 'sport']
    >>> for category in categories:
    ...     describe(category)
    My favorite beverage is coffee
    My favorite vegetable is broccoli
    I don't have a favorite sport. I love them all!
    """

    food = favorites.get(category)

    if food is None:
        message = "I don't have a favorite {}. I love them all!".format(category)
    else:
        message = "My favorite {} is {}".format(category, food)

    print(message)
