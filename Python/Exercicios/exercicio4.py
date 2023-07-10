# 1-Utilizando um loop "while", imprima os números de 1 a 10.
print();
print("Número 1");
print("---------------------------------------------------");
print("Vamos imprimir os números de 1 a 10 usando o laço While.");
numero = 1;
while numero <= 10:
    print(numero);
    numero += 1;
print("---------------------------------------------------");
print();

# 2- Utilizando um loop "for", imprima os números de 1 a 10.
print("Número 2");
print("---------------------------------------------------");
print("Vamos imprimir os números de 1 a 10 usando o laço For.");
for numero in range(1, 11):
    print(numero);
print("---------------------------------------------------");
print();

# 3- Utilizando um loop "while", calcule a soma dos números de 1 a 100.
print("Número 3");
print("---------------------------------------------------");
print("Vamos fazer a soma dos numeros de 1 a 100 usando o laço While.");
soma   = 0;
numero = 1;
while numero <= 100:
    soma += numero;
    numero += 1;
print("A soma dos números de 1 a 100 é: ", soma);
print("---------------------------------------------------");
print();

# 4- Utilizando um loop "for", calcule a soma dos números de 1 a 100.
print("Número 4");
print("---------------------------------------------------");
print("Vamos fazer a soma dos numeros de 1 a 100 usando o laço For.");
soma = 0;
for numero in range(1, 101):
    soma += numero;
print("A soma dos números de 1 a 100 é: ", soma);
print("---------------------------------------------------");
print();

# 5- Utilizando um loop "while", imprima os números pares de 1 a 20.
print("Número 5");
print("---------------------------------------------------");
print("Os números pares de 1 a 20 são: ");
numero = 1;
while numero <= 20:
    if numero % 2 == 0:
        print(numero);
    numero += 1;
print("---------------------------------------------------");
print();

# 6- Utilizando um loop "for", imprima os números pares de 1 a 20.
print("Número 6");
print("---------------------------------------------------");
print("Os números ímpares de 1 a 20 são: ");
for numero in range(2, 21, 2):
    print(numero);
print("---------------------------------------------------");
print();


# 7- Utilizando um loop "while", inverta uma string digitada pelo usuário.
print("Número 7");
print("---------------------------------------------------");
print("Invertendo uma string: ");
string = input("Por gentileza digite uma palavra: ");
inversa = "";
indice = len(string) - 1;
while indice >= 0:
    inversa += string[indice];
    indice -= 1;
print("String invertida:", inversa);
print("---------------------------------------------------");
print();

# 8- Utilizando um loop "for", verifique se uma palavra digitada pelo usuário é 
# um palíndromo (lê-se da mesma forma de trás para frente).
print("Número 8");
print("---------------------------------------------------");
print("Verificando se uma palavra é um palindromo: ");
palavra = input("Digite uma palavra: ");
palindromo = True;
for indice in range(len(palavra) // 2):
    if palavra[indice] != palavra[-indice - 1]:
        palindromo = False;
        break;
if palindromo:
    print("A palavra é um palíndromo.");
else:
    print("A palavra não é um palíndromo.");
print("---------------------------------------------------");
print();

# 9- Utilizando um loop "while", encontre o menor número inteiro cujo quadrado seja maior do que 1000.
print("Número 9");
print("---------------------------------------------------");
print("Encontrando o menor número inteiro cujo quadrado seja maior que 1000: ");
numero = 1
while numero**2 <= 1000:
    numero += 1
print("O menor número inteiro cujo quadrado é maior do que 1000 é:", numero)
print("---------------------------------------------------");
print();

# **DESAFIO**
# 10- Utilizando um loop "for", imprima os elementos de uma lista em
# ordem inversa.
print("Número 10");
print("---------------------------------------------------");
print("Imprimindo uma lista de forma inversa: ");
lista = ["Ricck", "Gabriel", "Diego", "Ariel", "Tati"];
print("Essa é a lista antes da inversão: ", lista);
for elemento in reversed(lista):
    print(elemento);
print("---------------------------------------------------");
print();