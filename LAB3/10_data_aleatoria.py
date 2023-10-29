"""
File: 10_data_aleatoria.py
----------------------
indique o que faz este programa
"""

import random
import math

def main():
    data_aleatoria()

def data_aleatoria():
    DIA = random.randint(1, 31)
    MES = random.randint(1, 12)
    ANO = random.randint(2000, 2020)
    print("Data: ", DIA, "/", MES, "/", ANO)


# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
