"""
File: 1_media3notas.py
----------------------
indique o que faz este programa
"""

def main():
    soma = 0
    for _ in range(3):
        nota = float(input("Nota: "))
        soma += nota
        media = soma / 3
    print("A média é", media)


# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
