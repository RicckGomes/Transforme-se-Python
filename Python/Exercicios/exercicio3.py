"""
1-Escreva um programa que solicite ao usuário dois números
inteiros e exiba a soma, subtração, multiplicação e divisão entre
esses números.
"""
print();
print("Número 1");
print("---------------------------------------------------");
num1 = int(input(" Por gentileza digite o primeiro número inteiro: "));
num2 = int(input(" Por gentileza digite o segundo número inteiro: "));
print("---------------------------------------------------");
soma          = num1 + num2;
subtracao     = num1 - num2;
multiplicacao = num1 * num2;
divisao       = num1 / num2;
print();
print("------------------------------------");
print("A soma dos números é:", soma);
print("A subtração dos números é:", subtracao);
print("A multiplicação dos números é:", multiplicacao);
print("A divisão dos números é:", divisao);
print("------------------------------------");
print();

"""
2- Escreva um programa que solicite ao usuário uma temperatura
em graus Celsius e verifique se ela está acima do ponto de
ebulição da água (100°C). Caso positivo, exiba a mensagem "A
água está fervendo!".
"""
print("Número 2");
print("---------------------------------------------------");
temperatura = float(input("Por gentileza digite a temperatura informada no termômetro: "));

if temperatura > 100:
    print(f"A temperatura informada é {temperatura}°c. A água está fervendo!");
    print("---------------------------------------------------");
    print();
else:
    print(f"A temperatura informada é {temperatura}°c. A água não está fervendo!");
    print("---------------------------------------------------");
    print();

"""
3- Escreva um programa que solicite ao usuário um número
inteiro e verifique se ele é par ou ímpar.
"""
print("Número 3");
print("---------------------------------------------------");
numeroInt = int(input("Por gentileza, digite um número inteiro: "));

if numeroInt % 2 == 0:
    print(f"O número informado foi {numeroInt}, ele é par!")
    print("---------------------------------------------------");
    print();
else:
    print(f"O número informado foi {numeroInt}, ele é ímpar!")
    print("---------------------------------------------------");
    print();

"""
4- Escreva um programa que solicite uma senha ao usuário e
verifique se a senha está correta. Considere a senha correta como
"123456".
"""
print("Número 4");
print("---------------------------------------------------");
senha = input("Digite sua senha: ");
senhaCorreta = "123456";
if senha == senhaCorreta:
    print("A senha está correta, usuário logado com sucesso!");
    print("---------------------------------------------------");
    print();
else:
    print("A senha informada está incorreta!");
    print("---------------------------------------------------");
    print();

"""
5- Escreva um programa que solicite ao usuário uma idade e
verifique se ela está entre 18 e 30 anos (inclusive).
"""
print("Número 5");
print("---------------------------------------------------");
idade = int(input("Digite a sua idade: "));

if idade >= 18 and idade <= 30:
    print("A idade está no intervalo solicitado.");
    print("---------------------------------------------------");
    print();
else:
    print("A idade não está dentro do intervalo solicitado.");
    print("---------------------------------------------------");
    print();

"""
6- Escreva um programa que solicite ao usuário três números
inteiros e verifique se pelo menos um deles é positivo.
"""
print("Número 6");
print("---------------------------------------------------");
numero1 = int(input("Digite o primeiro número inteiro: "));
numero2 = int(input("Digite o segundo número inteiro: "));
numero3 = int(input("Digite o terceiro número inteiro: "));

if numero1 > 0 and numero2 <= 0 and numero3 <= 0:
    print("O primeiro número é positivo e os outros dois são não positivos.");
    print("---------------------------------------------------");
    print();
elif numero1 <= 0 and numero2 > 0 and numero3 <= 0:
    print("O segundo número é positivo e os outros dois são não positivos.");
    print("---------------------------------------------------");
    print();
elif numero1 <= 0 and numero2 <= 0 and numero3 > 0:
    print("O terceiro número é positivo e os outros dois são não positivos.");
    print("---------------------------------------------------");
    print();
elif numero1 > 0 and numero2 > 0 and numero3 <= 0:
    print("O primeiro e o segundo números são positivos e o terceiro é não positivo.");
    print("---------------------------------------------------");
    print();
elif numero1 > 0 and numero2 <= 0 and numero3 > 0:
    print("O primeiro e o terceiro números são positivos e o segundo é não positivo.");
    print("---------------------------------------------------");
    print();
elif numero1 <= 0 and numero2 > 0 and numero3 > 0:
    print("O segundo e o terceiro números são positivos e o primeiro é não positivo.");
    print("---------------------------------------------------");
    print();
elif numero1 > 0 and numero2 > 0 and numero3 > 0:
    print("Todos os três números são positivos.");
    print("---------------------------------------------------");
    print();
else:
    print("Nenhum dos números é positivo.");
    print("---------------------------------------------------");
    print();


"""
7- Escreva um programa que solicite ao usuário uma letra e
verifique se ela é uma vogal (a, e, i, o, u).
"""
print("Número 7");
print("---------------------------------------------------");
letra = input("Digite uma letra: ");

if letra.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("A letra digitada é uma vogal.");
    print("---------------------------------------------------");
    print();
else:
    print("A letra digitada não é uma vogal.");
    print("---------------------------------------------------");
    print();

"""
8- Escreva um programa que solicite ao usuário um número
inteiro e verifique se ele é positivo, negativo ou zero.
"""
print("Número 8");
print("---------------------------------------------------");
numero = int(input("Por gentileza, digite um número inteiro: "));

if numero > 0:
    print(f"O número digitado é {numero} e ele é positivo.");
    print("---------------------------------------------------");
    print();
elif numero < 0:
    print(f"O número digitado é {numero} e ele é negativo.");
    print("---------------------------------------------------");
    print();
else:
    print(f"O número digitado é {numero}.");
    print("---------------------------------------------------");
    print();

"""
9- Escreva um programa que solicite ao usuário três números e
verifique se eles estão em ordem crescente.
"""
print("Número 9");
print("---------------------------------------------------");
numero1 = float(input("Digite o primeiro número: "));
numero2 = float(input("Digite o segundo número: "));
numero3 = float(input("Digite o terceiro número: "));

if numero1 < numero2 < numero3:
    print(f"Os números informados são {numero1, numero2, numero3} e eles estão em ordem crescente.");
    print("---------------------------------------------------");
    print();
else:
    print(f"Os números informados são {numero1, numero2, numero3} e eles não estão em ordem crescente.");
    print("---------------------------------------------------");
    print();


"""
10- Escreva um programa que solicite ao usuário um número
inteiro e verifique se ele é um múltiplo de 3 e 5 ao mesmo tempo.
"""
print("Número 10");
print("---------------------------------------------------");
numInteiro = int(input("Por gentileza digite um número inteiro: "));

if numInteiro % 3 == 0 and numInteiro % 5 == 0:
    print("O número é um múltiplo de 3 e 5 ao mesmo tempo.");
    print("---------------------------------------------------");
    print();
else:
    print("O número não é um múltiplo de 3 e 5 ao mesmo tempo.");
    print("---------------------------------------------------");
    print();

