from karel.stanfordkarel import *

"""
Ficheiro: 2_KarelReparaEstrada.py
------------------------------
Quando acabar de escrever este ficheiro, a 2_KarelReparaEstrada
vai ser capaz de reparar todos os buracos de uma estrada, tal
como descrito no enunciado do problema. 
"""


def main():
    while front_is_clear():
        if not right_is_blocked():
            put_beeper()
        move()

# Não necessita de editar código para além deste ponto

if __name__ == "__main__":
    run_karel_program()
