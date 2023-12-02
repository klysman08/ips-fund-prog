"""
File: 3_simulador_testes_medicos.py
----------------------
indique o que faz este programa
"""

import random

def main():
    num_pessoas = int(input("Digite o número de pessoas: "))
    taxa_infeccao = float(input("Digite a taxa de infeção (entre 0 e 1): "))
    acuracia = float(input("Digite a taxa de precisão do teste (entre 0 e 1): "))

    vp, fp, fn = simulate_tests(num_pessoas, acuracia, taxa_infeccao)
        
    print('-------------------')

    print(f'Total de pessoaas do estudo: {num_pessoas}')
    print(f'Acuracia do teste: {acuracia}')
    print(f'Taxa de infeccao: {taxa_infeccao}')

    print('-------------------')

    print(f'Verdadeiros positivos: {vp}')
    print(f'Falsos positivos: {fp}')
    print(f'Falsos negativos: {fn}')
    print(f'Verdadeiro negativos: {num_pessoas - vp}')

    print('-------------------')

    print(f'Falsos positivos em relacao aos verdadeiros positivos: {fp / (vp + fp)}')
    
    print('-------------------')

def simulate_tests(num_pessoas, acuracia, taxa_infeccao):
    
    vp = 0
    fp = 0
    fn = 0

    for _ in range(num_pessoas):

        is_infected = random.random() < taxa_infeccao
        test_result = random.random() < acuracia

        if is_infected and test_result:
            vp += 1
        elif not is_infected and not test_result:
            fp += 1
        elif is_infected:
            fn += 1

    return vp, fp, fn

# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
