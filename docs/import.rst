Utilizando o ``import``
=======================

.. doctest::

        >>> import arithmetics.addition
        >>> arithmetics.addition.soma_vezes_pi(10, 5)
        47.12388980384689

        >>> from arithmetics import addition
        >>> addition.soma_vezes_pi(5, 15)
        62.83185307179586

        >>> from arithmetics import addition as arit
        >>> arit.soma_vezes_pi(5, 15)
        62.83185307179586

        >>> from arithmetics.addition import soma_vezes_pi
        >>> soma_vezes_pi(15, 45)
        188.49555921538757

        >>> from arithmetics.addition import soma_vezes_pi as svpi
        >>> svpi(15, 45)
        188.49555921538757
