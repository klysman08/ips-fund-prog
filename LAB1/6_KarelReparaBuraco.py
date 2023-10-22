from karel.stanfordkarel import *

"""
Ficheiro: 6_KarelReparaBuraco.py
------------------------------
Quando acabar de escrever este ficheiro, a KarelReparaBuraco
deverá ser capaz de apanhar de reparar o buraco na estrada, 
como descrito no enunciado do problema.
"""


def main():
    move()
    turn_right()
    move()
    turn_left()
    put_beeper()
    turn_left()
    move()
    turn_right()
    move()
    
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Não necessita de editar código para além deste ponto

if __name__ == "__main__":
    run_karel_program()
