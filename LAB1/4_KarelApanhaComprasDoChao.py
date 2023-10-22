from karel.stanfordkarel import *

"""
Ficheiro: 4_KarelApanhaComprasDoChao.py
------------------------------
Quando acabar de escrever este ficheiro, a KarelApanhaComprasDoChao
deverá ser capaz de apanhar as compras, como descrito no enunciado
do problema.
"""


def main():
    turn_left()
    turn_left()
    move()
    move()
    pick_beeper()
    move()
    turn_right()
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    pick_beeper()
    turn_right()
    move()
    pick_beeper()
    #voltar para o começo
    turn_left()
    turn_left()
    move_3()
    turn_left()
    move_3()
    move()

    

def move_3():
    move()
    move()
    move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()


# Não necessita de editar código para além deste ponto

if __name__ == "__main__":
    run_karel_program()
