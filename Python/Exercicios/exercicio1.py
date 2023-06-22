"""
1 - Crie duas variáveis, nome e idade, e atribua a elas seus 
próprios valores. Em seguida, use a formatação de strings para 
imprimir a seguinte mensagem: "Olá, meu nome é [nome] e eu 
tenho [idade] anos."
"""

# Criação de variáveis
nome = "Ricck";
idade = 30;

print(f"Olá, meu nome é {nome} e eu tenho {idade} anos.");
print();

"""
2- Crie uma variável chamada frase e atribua a ela uma string. Em 
seguida, use a função len() para imprimir o comprimento da frase.
"""

# Criação da variável
frase = "Eu amo matemática e amo jogar xadrez!";
tamanhoFrase = len(frase);
print(f"O tamanho da minha frase é: {tamanhoFrase} caracteres");
print();

"""
3- Crie duas variáveis, nome e sobrenome, e atribua a elas seus 
próprios valores. Concatene as variáveis para criar uma nova 
variável chamada nome_completo e imprima o resultado.
"""

# Criação de variáveis
nome = "Ricck";
sobrenome = "Gomes";
nomeCompleto = nome + " " + sobrenome;
print(f"Olá, meu nome é {nome}, sobrenome {sobrenome}, ou seja, meu nome completo é {nomeCompleto}");
print();

"""
4- Crie uma variável chamada frase e atribua a ela uma string. Use 
o método upper() para imprimir a frase em letras maiúsculas.
"""

# Criação de variável
frase = "Xadrez é bom para exercitar os neorônios!";
print(frase.upper());
print();

"""
5- Crie uma variável chamada frase e atribua a ela uma string 
contendo uma frase completa. Use o método split() para dividir a 
frase em uma lista de palavras e imprima o resultado.
"""

# Criação de variável
frase = "Santos! O melhor time da história!";
qtdPalavras = frase.split();
print(frase);
print();
print(qtdPalavras);
print();

"""
6- Crie uma variável chamada frase e atribua a ela uma string. Use 
o método replace() para substituir uma palavra específica na 
frase por outra palavra de sua escolha. Imprima a frase 
modificada.
"""

# Criação de variável
frase = "O melhor vingador é o Homem de Ferro!";
print(frase);
print();
modificandoFrase = frase.replace("Homem de Ferro", "Capitão América");
print(modificandoFrase);
print();

"""
7- Crie duas váriaveis, “numero1” e “numero2” e atribua valores 
númerico a elas, depois crie uma váriavel resultado e armazene o 
resultado da soma das váriaveis “numero1” e “numero2”. Ao final 
imprima o resultado.
"""

# Criação de variáveis
numero1 = 10;
numero2 = 20;
resultado = numero1 + numero2;
print("O resultado da soma é: ", resultado);
print();

"""
8- Escreva um programa que solicite ao usuário que digite dois 
números inteiros e exiba a multiplicação desses números
EXTRA
"""

primeiroNumero = int(input("Por gentileza digite um número inteiro: "));
segundoNumero  = int(input("Por gentileza digite mais um número inteiro: "));
multiplicacao = primeiroNumero * segundoNumero;
print("O primeiro número foi ", primeiroNumero);
print("O segundo número foi ", segundoNumero);
print("A multiplicação dos números é: ", multiplicacao);
print();
