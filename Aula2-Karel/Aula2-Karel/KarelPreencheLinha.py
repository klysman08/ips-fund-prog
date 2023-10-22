from karel.stanfordkarel import *

"""
File: KarelPreencheLinha.py
---------------------
A Karel coloca uma linha completa de beepers.
BUGGY -- off by one bug
Necessário adicionar um put_beeper() final
"""


def main():
    while front_is_clear():
        put_beeper()
        move()


# Não é necessário editar código para além deste ponto

if __name__ == "__main__":
    run_karel_program()
