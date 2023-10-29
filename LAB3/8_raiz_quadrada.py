"""
File: 8_raiz_quadrada.py
----------------------
indique o que faz este programa
"""

def main():
    raiz_quadrada()
    

def raiz_quadrada():
    numero = float(input("Número: "))
    raiz = numero ** 0.5
    print("Raiz quadrada:", raiz)


# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
