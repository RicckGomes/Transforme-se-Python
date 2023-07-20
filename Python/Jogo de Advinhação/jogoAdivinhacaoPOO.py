import random

class JogoAdivinhacao:
    def __init__(self):
        print("----------------------------------------------------------");
        print(" Antes de começarmos, vamos definir o limite dos números.");
        print(" Escolha o valor máximo para o número secreto.");
        print("----------------------------------------------------------");
        self.nomeJogador = input("Digite o seu nome: ");
        self.limite = self.obterInputInteiro("Digite o limite desejado: ");
        self.numeroSecreto = random.randint(1, self.limite);
        self.escolhaTentativas = self.obterInputInteiro("Informe a quantidade de tentativas: ");

    def obterInputInteiro(self, mensagem):
        while True:
            try:
                valor = int(input(mensagem));
                return valor;
            except ValueError:
                print("Valor inválido. Digite um número inteiro.");
                print();

    def jogar(self):
        print("=========================================================");
        print(f" {self.nomeJogador}, bem-vindo ao jogo de adivinhação!");
        print(" Neste jogo, você deve adivinhar um número secreto.");
        print(f" Estou pensando em um número entre 1 e {self.limite}.");
        print(f" Você tem {self.escolhaTentativas} tentativas!");
        print(" Boa sorte!!!");
        print("=========================================================");
        
        self.tentativas = 0;

        while True:
            self.tentativas += 1;
            print(f"Tentativa {self.tentativas}!");
            palpite = self.obterInputInteiro("Digite o seu palpite: ");

            if palpite < self.numeroSecreto:
                if self.tentativas == self.escolhaTentativas:
                    print("=========================================================");
                    print(f"{self.nomeJogador}, não foi dessa vez, você atingiu o limite de {self.escolhaTentativas} tentativas!");
                    print("O número secreto era:", self.numeroSecreto);
                    print("=========================================================");
                    break;
                print("Não foi dessa vez. Tente um número maior!");
                print("=========================================================");
            elif palpite > self.numeroSecreto:
                if self.tentativas == self.escolhaTentativas:
                    print("=========================================================");
                    print(f"{self.nomeJogador}, não foi dessa vez, você atingiu o limite de {self.escolhaTentativas} tentativas!");
                    print("O número secreto era:", self.numeroSecreto);
                    print("=========================================================");
                    break;
                print("Não foi dessa vez. Tente um número menor!");
                print("=========================================================");
            else:
                print(f"Parabéns, {self.nomeJogador}! Você acertou o número em {self.tentativas} tentativas!");
                print("=========================================================");
                break;
            
        self.jogarNovamente();

    def jogarNovamente(self):
        jogarNovamente = self.obterInputInteiro("Deseja jogar novamente? 1. SIM | 2. NÃO: ");
        print("=========================================================");
        if jogarNovamente == 1:
            self.limite = self.obterInputInteiro("Digite o limite desejado: ");
            self.numeroSecreto = random.randint(1, self.limite);
            self.escolhaTentativas = self.obterInputInteiro("Informe a quantidade de tentativas: ");
            
            while self.escolhaTentativas > self.limite:
                print(f"O número máximo de tentativas não pode ser maior do que o limite ({self.limite}).");
                self.escolhaTentativas = self.obterInputInteiro("Informe a quantidade de tentativas: ");
            self.jogar();
        
        else:
            print(f"{self.nomeJogador}, obrigado por jogar! Espero que tenha gostado da experiência!");
            print("=========================================================");

jogo = JogoAdivinhacao();
jogo.jogar();