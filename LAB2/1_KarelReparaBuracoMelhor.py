from karel.stanfordkarel import *

"""
Ficheiro: 1_KarelReparaBuracoMelhor.py
------------------------------
Quando acabar de escrever este ficheiro, a KarelReparaBuracoMelhor
vai reparar o buraco como na versão anterior, mas problema será
resolvido com decomposição, resultando num código mais legível. 
"""



def main():
    move_to_beeper()
    put_beeper()
    return_to_start()

def move_to_beeper():
    move()
    turn_right()
    move()
    turn_left()

def return_to_start():
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