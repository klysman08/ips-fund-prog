"""
File: 2_preco_com_iva.py
----------------------
indique o que faz este programa
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
