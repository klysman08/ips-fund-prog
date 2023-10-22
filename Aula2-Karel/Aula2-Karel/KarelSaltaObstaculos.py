from karel.stanfordkarel import *

"""
File: KarelSaltaObstaculos.py
--------------------------
A Karel faz uma corrida de obstáculos com 9 avenidas de comprimento.
Os obstáculos têm altura e posição arbitrárias.
"""


def main():
    """
    Para fazer uma corrida com 9 avenidas de comprimento, temos de
    andar para a frente ou saltar 8 vezes.
    """
    for i in range(8):
        if front_is_clear():
            move()
        else:
            saltar_obstaculo()


def saltar_obstaculo():
    """
    Pré-condição: Virada para este na base do obstáculo
    Pós-condição: Virada para este na base na próxima avenida após o obstáculo
    """
    subir_obstaculo()
    move()
    descer_obstaculo()


def subir_obstaculo():
    """
    Pré-condição: Virada para este na base do obstáculo
    Pós-condição: Virada para este imediatamente acima do obstáculo
    """
    turn_left()
    while right_is_blocked():
        move()
    turn_right()


def descer_obstaculo():
    """
    Pré-condição: Virada para este acima e imediatamente após o obstáculo
    Pós-condição: Virada para este na base do obstáculo
    """
    turn_right()
    move_to_wall()
    turn_left()


def move_to_wall():
    """
    Pré-condição: nenhuma
    Pós-condição: Junto à parede na mesma direção que a Karel estava virada anteriormente

    """
    while front_is_clear():
        move()


def turn_right():
    """
    Pré-condição: nenhuma
    Pós-condição: Karel está voltada para a direita da direção que estava virada anteriormente
    """
    for i in range(3):
        turn_left()


# Não é necessário editar código para além deste ponto

if __name__ == "__main__":
    run_karel_program()
