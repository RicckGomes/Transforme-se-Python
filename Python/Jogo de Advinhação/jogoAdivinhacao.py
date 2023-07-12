import random

# Criei a função abaixo para obrigar que o usuário digite um valor válido
def obterInputInteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem));
            return valor;
        except ValueError:
            print("Valor inválido. Digite um número inteiro.");
            print();

def adivinhacao():
    print("----------------------------------------------------------");
    print(" Antes de começarmos, vamos definir o limite dos números.");
    print(" Escolha o valor máximo para o número secreto.");
    print("----------------------------------------------------------");
    
    print();
    limite = obterInputInteiro("Digite o valor máximo desejado: ");
    print();
    numeroSecreto = random.randint(1, limite);
    tentativas = 0;
    print();

    print("====================================================");
    print(" Bem-vindo ao jogo de adivinhação!");
    print(" Neste jogo, você deve adivinhar um número secreto.");
    print(f" Estou pensando em um número entre 1 e {limite}.")
    print(" Você deverá escolher a quantidade de tentativas.");
    print(" Boa sorte!!!");
    print("====================================================");

    escolhaTentativas = obterInputInteiro("Infome a quantidade de tentativas: ");
    print("==================================================");

    while True:
        tentativas += 1;
        print(f"Tentativa {tentativas}!");
        palpite = obterInputInteiro("Digite o seu palpite: ");
        
        if palpite < numeroSecreto:
            if tentativas == escolhaTentativas:
                print("=========================================================");
                print(f"Não foi dessa vez, você atingiu o limite de {escolhaTentativas} tentativas!");
                print("=========================================================");
                break;
            print("Tente um número maior!");
            print("=============================================");
        elif palpite > numeroSecreto:
            if tentativas == escolhaTentativas:
                print("=========================================================");
                print(f"Não foi dessa vez, você atingiu o limite de {escolhaTentativas} tentativas!");
                print("=========================================================");
                break;
            print("Tente um número menor!");
            print("=============================================");
        else:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas!");
            print("=============================================");
            break;
    print();
    
    jogarNovamente = obterInputInteiro("Deseja jogar novamente? 1. SIM - 2. NÃO: ");  
    if jogarNovamente == 1:
        adivinhacao();
    # O código abaixo também funcionaria, porém por questão de desempenho vou com o IF
    # while jogarNovamente == 1:
    #     adivinhacao();
    
adivinhacao();