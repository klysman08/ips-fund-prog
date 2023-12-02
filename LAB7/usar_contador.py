"""
File: usar_contador.py
--------------------
Este programa fornece um exemplo de utilização de objetos Contador.
"""

from contador import Contador  # importar a Classe


def contar_duas_vezes(contador):
    """
    Get and prints next two numbers in a Counter object
    """
    for _ in range(2):
        print(contador.proximo_valor())


def main():
    contador1 = Contador()  # Criar um novo objeto Contador
    contador2 = Contador()  # Criar outro novo objeto Contador

    print('Contador1: ')
    contar_duas_vezes(contador1)

    print('Contador2: ')
    contar_duas_vezes(contador2)

    print('Contador1: ')
    contar_duas_vezes(contador1)


if __name__ == '__main__':
    main()
