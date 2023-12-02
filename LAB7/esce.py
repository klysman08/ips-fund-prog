"""
File: esce.py
-----------------
Este programa fornece um exemplo de utilização de objetos Estudante.
"""


from estudante import Estudante


ECTS_FP = 4.5


def print_creditos(e):
    """
    Imprime o nome e o número de créditos que o estudante e tem,
    bem como se o estudante terminou o curso.
    """
    print(f"{e.get_nome()} tem {str(e.get_creditos())} ECTS")
    print(f"{e.get_nome()} terminou o curso: {str(e.terminou_curso())}")


def fazer_FP(e):
    """
    Declara que o estudante e fez a UC de FP e incrementa o número de créditos
    """
    print(f"{e.get_nome()} fez FP!!")
    e.incrementar_creditos(ECTS_FP)


def main():
    maria = Estudante("Maria Geraldo", 220353035)
    maria.set_creditos(9)
    print_creditos(maria)

    joao = Estudante("João Marreiros", 220353015)
    joao.set_creditos(85.5)
    print_creditos(joao)

    fazer_FP(maria)
    fazer_FP(joao)

    print_creditos(maria)
    print_creditos(joao)


if __name__ == '__main__':
    main()
