Fábricas de dados
=================

.. testcode::

        import csv
        from faker import Factory

        if __name__ == '__main__':
            faker = Factory.create('pt_BR')  # cria fábrica de dados falsos em pt-BR

            with open('dados.txt', 'w') as arq:
                escritor = csv.writer(arq, delimiter="-", quotechar="Z")

                for _ in range(100):
                    dados = faker.name(), faker.job(), faker.company()
                    escritor.writerow(dados)
