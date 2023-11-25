"""
File: estudante.py
----------------
A classe Estudante faz a gestão dos seguintes dados sobre um
estudante: o nome do estudante, número de estudante, e o
número de créditos ECTS que o estudante já acumulou no curso.
"""


ECTS_PARA_TERMINAR = 90     # Constante


class Estudante:

    def __init__(self, nome_estudante, numero_estudante):
        """
        Cria um objeto Estudante com o nome e número fornecidos.
        O número inicial de ECTS é 0.
        """
        self.nome = nome_estudante
        self.numero = numero_estudante
        self.creditos_feitos = 0

    def get_nome(self):
        """
        Devolve o nome do estudante.
        """
        return self.nome

    def get_numero(self):
        """
        Devolve o número do estudante.
        """
        return self.numero

    def get_creditos(self):
        """
        Devolve o número de créditos feitos por este estudante.
        """
        return self.creditos_feitos

    def set_creditos(self, creditos):
        """
        Define o número de créditos feitos por este estudante.
        """
        self.creditos_feitos = creditos

    def incrementar_creditos(self, creditos_adicionais):
        """
        Adiciona creditos_adicionais ao número de creditos feitos por este estudante.
        """
        self.creditos_feitos += creditos_adicionais

    def terminou_curso(self):
        return self.creditos_feitos >= ECTS_PARA_TERMINAR
