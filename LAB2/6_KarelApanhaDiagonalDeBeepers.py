from karel.stanfordkarel import *

"""
Ficheiro: 6_KarelApanhaDiagonalDeBeepers.py
------------------------------
Quando acabar de escrever este ficheiro, a 6_KarelApanhaDiagonalDeBeepers
vai ser capaz de apanhar todos os beepers na diagonal,
como descrito no enunciado do problema. Tente obter uma solução
genérica, que funcione em mundos diferentes.
"""


def main():

    turn_right()
    move()
    turn_left()
    pick_beeper()

    for i in range(6):
        move()
        turn_left()
        move()
        turn_right()
        pick_beeper()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()


# Não necessita de editar código para além deste ponto

if __name__ == "__main__":
    run_karel_program()
