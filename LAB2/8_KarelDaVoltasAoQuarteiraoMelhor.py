from karel.stanfordkarel import *

"""
Ficheiro: 8_KarelDaVoltasAoQuarteiraoMelhor.py
------------------------------
Quando acabar de escrever este ficheiro, a 8_KarelDaVoltasAoQuarteiraoMelhor
irá continuar a conseguir dar as voltas ao quarteirão, como descrito
no enunciado do problema, mas a solução será suficientemente genérica 
para funcionar bem com qualquer dos três mundos fornecidos.
"""


def main():
    move()
    while front_is_clear():
        if left_is_blocked():
            move()
        else:
            turn_left()
            move()
        



# Não necessita de editar código para além deste ponto

if __name__ == "__main__":
    run_karel_program()
