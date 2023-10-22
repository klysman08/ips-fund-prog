from karel.stanfordkarel import *

"""
Ficheiro: 9_KarelSaltaObstaculos.py
------------------------------
Quando acabar de escrever este ficheiro, a 9_KarelSaltaObstaculos
vai ser capaz de saltar os obstáculos, tal como descrito
no enunciado do problema. Tente obter uma solução genérica, 
que funcione em mundos diferente2s.
"""


def main():
    for i in range(11):
        if front_is_clear():
            move()
        else:
            pular_obstaculo()

def pular_obstaculo():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def turn_right():
    for i in range(3):
        turn_left()

# Não necessita de editar código para além deste ponto

if __name__ == "__main__":
    run_karel_program()
