from karel.stanfordkarel import *

"""
Ficheiro: 5_KarelFazSlalom.py
------------------------------
Quando acabar de escrever este ficheiro, a KarelFazSlalom
deverá ser capaz de apanhar de fazer um oito no menor 
número possível de movimentos, como descrito no enunciado
do problema.
"""


def main():
    move()
    move_left()
    move_right()
    move_right()
    move_left()


def move_left():
    turn_left()
    move()
    move()
    turn_left()
    move()
    move()

def move_right():
    turn_right()
    move()
    move()
    turn_right()
    move()
    move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()


# Não necessita de editar código para além deste ponto

if __name__ == "__main__":
    run_karel_program()
