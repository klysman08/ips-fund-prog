"""
File: 2_encontrar_divisores.py
----------------------
indique o que faz este programa
"""

def main():
    
    while True:
        numero = int(input("Digite o numero para encontrar seus divisores: "))
        if numero == 0:
            print("Programa terminado")
            break
        elif numero < 0:
            print("Numero inválido")
        else:
            encontrar_divisores(numero)

def encontrar_divisores(numero):
    """
    Devolve os divisores de um numero.
    """
    print("Os divisores de", numero, "são:")
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i)
    

# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
