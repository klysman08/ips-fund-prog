"""
File: 3_rotate_list_right.py
----------------------
indique o que faz este programa
"""
def main():
    lista = [1, 2, 3, 4, 5, 6, 7, 8]
    passos = 5
    print(lista)
    print(rotate_list_right(lista, passos))
    
def rotate_list_right(lista, passos):
    return [lista[(i - passos)] for i in range(0, len(lista))]

# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
