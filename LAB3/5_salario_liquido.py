"""
File: 5_salario_liquido.py
----------------------
indique o que faz este programa
"""

def main():
    salario = float(input("Salário (€): "))
    irs = float(input("IRS (%): "))
    seg_social = float(input("Segurança Social (%): "))
    salario_liquido = salario * (1 - (irs + seg_social) / 100)
    salario_liquido = salario_liquido + 220
    print("Salário líquido:", salario_liquido)


# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
