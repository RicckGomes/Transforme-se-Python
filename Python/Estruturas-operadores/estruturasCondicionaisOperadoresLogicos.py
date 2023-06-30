"""
Estruturas condicionais
"""

# Verificação de idade para entrada em um clube noturno
idade = int(input("Digite sua idade:"));
if idade >= 18:
    print("Seja bem-vindo(a), curta nossa festa!");
    print();
else:
    print("Desculpe, não é permitido a entrada de menores de idade em nosso estabelecimento!");
    print();
    
# Verifica se um número está dentro de um intervalo, entre 10 e 20
numero = 15;
if numero >= 10 and numero <= 20:
    print("O número está dentro do intervalo.");
    print();
else:
    print("O número não está dentro do intervalo.")
    print();
    
# Comparar o tamanho de duas listas
lista1 = [1,2,3,4,5];
lista2 = [1,2,3,4,5];
if len(lista1) > len(lista2):
    print("A lista 1 é maior que a lista 2!");
    print();
elif len(lista2) > len(lista1):
    print("A lista 2 é maior que a lista 1!");
    print();
else:
    print("As listas tem o mesmo tamanho.");
    print();
    
# Verificação de acesso em um sistema
senha = input("Digite sua senha:");
senhaCorreta = "123456";
if senha == senhaCorreta:
    print("Usuário logado com sucesso!");
    print();
else:
    print("A senha informada está incorreta!");
    print();