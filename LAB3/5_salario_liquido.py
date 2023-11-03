"""
File: 5_salario_liquido.py
----------------------
indique o que faz este programa
"""

def main():
    salario_base = float(input("Salário base: "))
    taxa_irs = float(input("Taxa de IRS (%): "))
    taxa_ss = float(input("Taxa de SS (%): "))
    salario_liquido = salario_base * (1 - (taxa_irs + taxa_ss) / 100)
    print("Salário líquido:", salario_liquido)



# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
