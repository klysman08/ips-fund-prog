from karel.stanfordkarel import *

"""
Ficheiro: 4_KarelAprendeMetodos.py
------------------------------
Quando acabar de escrever este ficheiro, a 4_KarelAprendeMetodos
irá aprender a executar os três métodos descritos no enunciado:
MoveMile, MoveBackward e MoveKilomile.
"""


def main():
    move_mile()


def move_mile():
    for _ in range(8):
        move()

def move_backward():
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()

def move_kilomile():
    1000 * move_mile()



# Não necessita de editar código para além deste ponto

if __name__ == "__main__":
    run_karel_program()
