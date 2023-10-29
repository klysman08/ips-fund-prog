"""
File: 9_desconto_aleatorio.py
----------------------
indique o que faz este programa
"""

import random
import math

def main():
    desconto_aleatorio()

def desconto_aleatorio():
    DESCONTO = random.uniform(0, 0.5)
    produto1 = float(input("Produto 1: "))
    produto2 = float(input("Produto 2: "))
    print("Desconto: ", DESCONTO)
    print("Produto 1: ", produto1*(1-DESCONTO))
    print("Produto 2: ", produto2*(1-DESCONTO))


# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
