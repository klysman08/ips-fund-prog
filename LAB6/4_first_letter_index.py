"""
File: 4_first_letter_index.py
----------------------
indique o que faz este programa
"""

def main():
    palavras = ['banter', 'brahm', 'crhow', 'aardvark', 'python', 'antiquated']
    first_list_1(palavras)


def first_list_1(palavras):
    dicionario = {}
    for palavra in palavras:
        letra_inicial = palavra[0]
        if letra_inicial not in dicionario:
            dicionario[letra_inicial] = [palavra]
        else:
            dicionario[letra_inicial].append(palavra)

    print(dicionario)

def first_list(palavras):
    dicionario = {}
    for i in range(0, len(palavras)):
        for j in range(0, len(palavras)):
            if palavras[i][0] == palavras[j][0]:
                dicionario[palavras[i][0]] = palavras[j]

    print(dicionario)
    

# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
