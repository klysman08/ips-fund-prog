"""
File: 1_anos_cao.py
----------------------
indique o que faz este programa
"""


def main():
    while True:
        idade_humano = int(input("Idade: "))
        if idade_humano == 0:
            print("Programa terminado")
            break
        elif idade_humano < 0:
            print("Idade inválida")
        else:
            print("Idade em anos de cão: " +
                  str(anos_cao_para_anos_humanos(idade_humano)))


ANOS_CAO_POR_ANO_HUMANO = 7


def anos_cao_para_anos_humanos(idade_humano):
    """
    Devolve a idade do cão em anos humanos.
    """
    return idade_humano * ANOS_CAO_POR_ANO_HUMANO


# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
