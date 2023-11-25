"""
File: contador.py
----------------
Este ficheiro define uma Classe para um contador que simplesmente
atribui uma série sequencial de inteiros (senhas) a começar em 1.
Um novo número (senha) é produzido sempre que é pedida a próxima
senha ao contador.
"""


class Contador:

    def __init__(self):
        """
        Cria um objeto contador e inicializa o número de senha interno
        """
        self.num_senha = 0   # variável de instância para controlar as senhas

    def proximo_valor(self):
        """
        Returns the next ticket number for this counter.
        """
        self.num_senha += 1
        return self.num_senha
