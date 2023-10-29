"""
File: 7_seno_angulo.py
----------------------
indique o que faz este programa
"""

import math

def main():
    seno_angulo()
    

def seno_angulo():
    angulo = float(input("Ângulo: "))
    angulo = math.radians(angulo)
    seno = math.sin(angulo)
    print("Seno:", seno)
    
# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
