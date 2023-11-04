"""
File: 3_pedra_papel_tesoura.py
----------------------
indique o que faz este programa
"""

import random


def main():
    vitorias = 0
    derrotas = 0
    while True:
        
        humano = int(input("Pedra (1), papel (2) ou tesoura (3)? "))
        computador = jogada_computador()
        resultado = verifica_ganhador(humano, computador)

        if resultado == 1:
            vitorias += 1
            print("Ganhou rodada!")
            if vitorias >= 3:
                print("Ganhou o jogo!")
                break
        else:
            derrotas += 1
            print("Perdeu rodada!")
            if derrotas >= 3:
                print("Perdeu o jogo!")
                break 

def jogada_computador():
    return random.randint(1,3)

def verifica_ganhador(humano, computador):
    if humano == 1 and computador == 3:
        print("Pedra ganha tesoura")
        return 1
    elif humano == 2 and computador == 1:
        print("Papel ganha pedra")
        return 1
    elif humano == 3 and computador == 2:
        print("Tesoura ganha papel")
        return 1
    else:
        return 0




# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
