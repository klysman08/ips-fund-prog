import random

def simulate_tests(num_people, test_accuracy, infection_rate):
    # Inicializar contadores
    true_positives = 0
    false_positives = 0
    false_negatives = 0

    # Simular o teste para cada pessoa
    for _ in range(num_people):
        # Passo 1: Escolher aleatoriamente se a pessoa está ou não doente
        is_infected = random.random() < infection_rate

        # Passo 2: Escolher aleatoriamente se o teste é correto para a pessoa
        test_result = random.random() < test_accuracy

        # Passo 3: Atualizar contadores com base nos resultados
        if is_infected and test_result:
            true_positives += 1
        elif not is_infected and test_result:
            false_positives += 1
        elif is_infected and not test_result:
            false_negatives += 1

    # Calcular proporção de resultados positivos incorretos
    total_positives = true_positives + false_positives
    if total_positives == 0:
        incorrect_ratio = 0.0
    else:
        incorrect_ratio = false_positives / total_positives

    # Exibir as 4 quantidades
    print(f'True Positives: {true_positives}')
    print(f'False Positives: {false_positives}')
    print(f'False Negatives: {false_negatives}')
    print(f'True Negatives: {num_people - true_positives - false_positives - false_negatives}')

    return incorrect_ratio

def main():
    num_people = int(input("Digite o número de pessoas: "))
    test_accuracy = float(input("Digite a taxa de precisão do teste (entre 0 e 1): "))
    infection_rate = float(input("Digite a taxa de infeção (entre 0 e 1): "))

    incorrect_ratio = simulate_tests(num_people, test_accuracy, infection_rate)

    print('-------------------')
    print(f'Proporção de resultados positivos incorretos: {incorrect_ratio}')

if __name__ == "__main__":
    main()
