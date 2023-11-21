"""
File: 1_collapse.py
----------------------
indique o que faz este programa
"""

  

def main():
    lista = [7, 2, 8, 9, 4, 13, 7, 1, 9, 10, 5]
    print(collapse(lista))
    

def collapse(lista):
    collapsed_list = []
    i = 0
    for i in range(0, len(lista)-1, 2):
        collapsed_list.append(lista[i] + lista[i+1])
        i += 2
    if len(lista) % 2 != 0:
        collapsed_list.append(lista[-1])
    return collapsed_list


# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
