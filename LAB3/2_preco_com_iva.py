"""
File: 2_preco_com_iva.py
----------------------
indique o que faz este programa
Calcule o preço final de um produto aplicando o IVA ao preço base. O preço base e a taxa de IVA em percentagem são fornecidos pelo utilizador
"""

def main():
    preco_base = float(input("Preço base: "))
    taxa_iva = float(input("Taxa de IVA (%): "))
    preco_final = preco_base * (1 + taxa_iva / 100)
    print("Preço final:", preco_final)


# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
