"""
File: 3_imc.py
----------------------
indique o que faz este programa

"""

def main():
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    imc = peso / altura ** 2
    print("IMC:", imc)


# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
