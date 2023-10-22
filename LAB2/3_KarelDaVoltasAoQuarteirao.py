from karel.stanfordkarel import *

"""
Ficheiro: 3_KarelDaVoltasAoQuarteirao.py
------------------------------
Quando acabar de escrever este ficheiro, a 3_KarelDaVoltasAoQuarteirao
vai ser capaz de dar quatro voltas ao quarteirão, tal
como descrito no enunciado do problema.
"""


def main():
    for i in range(4):
        for i in range(5): 
            move()
        turn_left()


# Não necessita de editar código para além deste ponto

if __name__ == "__main__":
    run_karel_program()
