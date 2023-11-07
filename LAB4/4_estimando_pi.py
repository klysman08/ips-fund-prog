"""
File: 4_estimando_pi.py
----------------------
indique o que faz este programa
"""
import random

def main():
    print(f'PI estimado: {estima_pi()}')
    
NUM_PONTOS = 100000

def gera_pontos(num_pontos):
    soma=0
    for i in range(num_pontos):
        x=random.uniform(-1,1)
        y=random.uniform(-1,1)
        i=i+1
        if x**2+y**2<=1:
            soma=soma+1
    return soma
    
def estima_pi(pontos=gera_pontos(NUM_PONTOS)):
    print(f'Total de pontos somados: {pontos}')
    pi=4*pontos/NUM_PONTOS
    return pi



# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
