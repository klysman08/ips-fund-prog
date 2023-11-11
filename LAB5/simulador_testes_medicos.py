"""
File: 3_simulador_testes_medicos.py
----------------------
indique o que faz este programa
"""

import random

def main():
    num_pessoas = 10000
    taxa_infeccao = 0.01
    acuracia = 0.99
    pessoas_doentes = quantidade_pessoas_doentes(num_pessoas, taxa_infeccao)

    vp = verdadeiro_positivo(pessoas_doentes, acuracia)
    fp = falso_positivo(num_pessoas - vp, acuracia)
    fn = falso_negativo(pessoas_doentes, acuracia)

    print('-------------------')

    print(f'Total de pessoaas do estudo: {num_pessoas}')
    print(f'Acuracia do teste: {acuracia}')
    print(f'Taxa de infeccao: {taxa_infeccao}')

    print('-------------------')

    print(f'Verdadeiros positivos: {vp}')
    print(f'Falsos positivos: {fp}')
    print(f'Falsos negativos: {fn}')
    print(f'Verdadeiro negativos: {num_pessoas - vp - fp - fn}')

    print('-------------------')

    #numero de resultados positivos incorretos dividido pelo numero total de resultados positivos
    print(f'Falsos positivos em relacao aos verdadeiros positivos: {fp / (vp + fp)}')
    
    print('-------------------')

def quantidade_pessoas_doentes(num_pessoas, taxa_infeccao):
    return num_pessoas * taxa_infeccao

def verdadeiro_positivo(pessoas_doentes, acuracia):
    return pessoas_doentes * acuracia

def falso_positivo(num_pessoas, acuracia):
    return num_pessoas * (1 - acuracia)

def falso_negativo(pessoas_doentes, acuracia):
    return pessoas_doentes * (1 - acuracia)



# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
