"""
File: 6_distancia2pontos.py
----------------------
indique o que faz este programa
"""

def main():
    calcula_distancia()
    

def calcula_distancia():
    ponto1 = [float(input("Ponto 1 (x,y): ")) for _ in range(2)]
    ponto2 = [float(input("Ponto 2 (x,y): ")) for _ in range(2)]
    distancia = ((ponto2[0] - ponto1[0]) ** 2 + (ponto2[1] - ponto1[1]) ** 2) ** 0.5
    print("Distância:", distancia)

# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
