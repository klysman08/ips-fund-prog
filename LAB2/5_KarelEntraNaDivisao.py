from karel.stanfordkarel import *

"""
Ficheiro: 5_KarelEntraNaDivisao.py
------------------------------
Quando acabar de escrever este ficheiro, a 5_KarelEntraNaDivisao
vai ser capaz de entrar na divisão, tal
como descrito no enunciado do problema. Tente obter uma solução
genérica, que funcione em mundos diferentes.
"""


def main():
    while front_is_clear():
        move()
    turn_left()
    move()
    while left_is_blocked():
        move()
    turn_left()
    move()


# Não necessita de editar código para além deste ponto

if __name__ == "__main__":
    run_karel_program()
