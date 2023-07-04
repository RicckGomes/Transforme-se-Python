print("-----------------------------------------------");
print(" Obrigado por usar minha primeira calculadora!");
print("-----------------------------------------------");

# Solicita o primeiro número ao usuário
num1 = float(input("Digite o primeiro número: "));
print("-----------------------------------------------");

print("Escolha uma operação:");
print("1 - Somar");
print("2 - Subtrair");
print("3 - Multiplicar");
print("4 - Dividir");
print("-----------------------------------------------");

# Solicita a operação desejada ao usuário
operacao1 = int(input("Digite o número correspondente à operação desejada: "));
print("-----------------------------------------------");

# Solicita o segundo número ao usuário
num2 = float(input("Digite o segundo número: "));
print("-----------------------------------------------");

# Pergunta ao usuário se deseja adicionar mais um número à operação
novoNum1 = int(input("Deseja adicionar mais algum número em sua operação? 1 - Sim | 2 - Não: "));
print("-----------------------------------------------");

if novoNum1 == 1:
    # Se o usuário deseja adicionar mais um número, solicita o terceiro número
    num3 = float(input("Digite o terceiro número: "));
    print("-----------------------------------------------");
    print("Escolha uma operação:");
    print("1 - Somar");
    print("2 - Subtrair");
    print("3 - Multiplicar");
    print("4 - Dividir");
    print("-----------------------------------------------");

# Solicita a segunda operação desejada ao usuário
    operacao2 = int(input("Digite o número correspondente à operação desejada: "));
    print("-----------------------------------------------");

# Realiza a primeira operação selecionada
if operacao1 == 1:
    resultado = num1 + num2;
elif operacao1 == 2:
    resultado = num1 - num2;
elif operacao1 == 3:
    resultado = num1 * num2;
elif operacao1 == 4:
    resultado = num1 / num2;

"""
Se o usuário adicionou mais um número à operação, realiza a segunda operação
Nesse caso usarei os operadores compostos para simplificar a visualização do código
resultado += num3 é o mesmo que resultado = resultado + num3
"""
if novoNum1 == 1:
    if operacao2 == 1:
        resultado += num3;
    elif operacao2 == 2:
        resultado -= num3;
    elif operacao2 == 3:
        resultado *= num3;
    elif operacao2 == 4:
        resultado /= num3;

# Exibe o resultado final
print("O resultado da sua operação é:", resultado);
print("-----------------------------------------------");
print();


