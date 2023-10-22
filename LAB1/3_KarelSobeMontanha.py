from karel.stanfordkarel import *

"""
Ficheiro: 3_KarelSobeMontanha.py
------------------------------
Quando acabar de escrever este ficheiro, a KarelSobeMontanha
deverá ser capaz de escalar a montanha, colocar a bandeira,
e descer pelo lado oposto, como descrito no enunciado do 
problema.
"""


def main():
    move()
    turn_left()
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()
    turn_right()
    move()
    put_beeper()
    move()
    turn_right()
    move()
    turn_left()
    move()
    turn_right()
    move()
    move()
    turn_left()
    move()

def turn_right():
    turn_left()
    turn_left()
    turn_left() 



# Não necessita de editar código para além deste ponto

if __name__ == "__main__":
    run_karel_program()
