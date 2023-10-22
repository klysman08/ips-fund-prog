from karel.stanfordkarel import *

"""
Ficheiro: 2_KarelVaiBuscarJornal.py
------------------------------
Quando acabar de escrever este ficheiro, a KarelVaiBuscarJornal
deverá ser capaz de ir buscar o jornal e voltar à cama. No 
final, a Karel termina na posição inicial (mesma esquina, mesma
direção) com o jornal.
"""




def main():
    turn_left()
    move()
    move()
    turn_left()
    move()
    move()
    turn_left()
    move()
    move()
    turn_left()
    move()


def turn_right():
    turn_left()
    turn_left()
    turn_left() 

def move_3():
    move()
    move()
    move()

# Não necessita de editar código para além deste ponto

if __name__ == "__main__":
    run_karel_program()
