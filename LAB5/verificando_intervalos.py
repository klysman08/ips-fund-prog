"""
File: 1_verificando_intervalos.py
----------------------
indique o que faz este programa
"""

def main():
    while True:
        print("Verificando se um numero esta entre dois outros")
        x = int(input("x: "))
        y = int(input("y: "))
        z = int(input("z: "))

        if in_range(x, y, z):
            print(f'o numero {y} esta entre {x} e {z}')
        else:
            print(f'o numero {y} nao esta entre {x} e {z}')

        if input("Deseja continuar? (s/n) ") == "n":
            break


def in_range(x, y, z):
    if x <= y <= z:
        return True
    else:
        return False

# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
