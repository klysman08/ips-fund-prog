"""
File: 2_fizzbuzz.py
----------------------
indique o que faz este programa
"""
import time

def main():
    contador = 0
    numero = int(input("Insira um numero: "))

    for i in range(numero+1):
        
        time.sleep(1) #delay de 1 segundo
        
        if divisivel_por_3_ou_5(i) == 1:
            print("Fizz")
            contador = contador + 1
        elif divisivel_por_3_ou_5(i) == 2:
            print("Buzz")
            contador = contador + 1
        elif divisivel_por_3_ou_5(i) == 3:
            print("FizzBuzz")
            contador = contador + 1
        else:
            print(i)
        i = i + 1

    print(f"Total de fizz+fizzbuzz: {contador}")



def divisivel_por_3_ou_5(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return 3
    elif numero % 5 == 0:
        return 2
    elif numero % 3 == 0:
        return 1
    else:
        return 0


# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
