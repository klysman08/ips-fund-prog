from karel.stanfordkarel import *

"""
Ficheiro: 7_KarelFormigaApanhaMigalha.py
------------------------------
Quando acabar de escrever este ficheiro, a 7_KarelFormigaApanhaMigalha
vai ser capaz de apanhar a migalha, tal como descrito
no enunciado do problema. 
"""


def main():
    while front_is_clear(): #andar até o degrau
        move()
    turn_left()

    while right_is_blocked(): #subir o degrau
        move()
    turn_right()

    while no_beepers_present(): #andar até pegar a migalha
        move()
    pick_beeper()

    while front_is_clear(): #andar até o final
        move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Não necessita de editar código para além deste ponto

if __name__ == "__main__":
    run_karel_program()
