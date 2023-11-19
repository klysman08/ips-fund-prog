"""
File: 2_distinct_elements.py
----------------------
indique o que faz este programa
"""

def distinct_elements(lst):
    nova_lista = []
    for i in lst:
        if i not in nova_lista:
            nova_lista.append(i)
    return nova_lista

def main():
    lst = [1, 2, 3, 2, 1, 5, 6, 5, 5, 5]
    print(distinct_elements(lst))

# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
