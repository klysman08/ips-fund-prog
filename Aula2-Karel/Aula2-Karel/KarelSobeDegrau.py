from karel.stanfordkarel import *

"""
File: KarelSobeDegrau.py
--------------------
O nosso primeiro programa Karel, onde a Karel apanha
um beeper, sobe um degrau e larga o beeper.
"""


# O programa inicia executando uma função especial chamada main
def main():
    # Os comandos são executados um de cada vez começando aqui
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    turn_right()    # vai executar a função turn_right, e depois continuar a executar a partir daqui
    move()
    put_beeper()
    move()


# Esta função faz a Karel voltar-se para a direita
# da direção para onde estava voltada anteriormente.
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Isto é código "padrão" que carrega o seu código
# quando escreve "python3 KarelSobeDegrau.py" (no Mac)
# ou "py KarelSobeDegrau.py" (no PC) no terminal.
if __name__ == "__main__":
    run_karel_program()
