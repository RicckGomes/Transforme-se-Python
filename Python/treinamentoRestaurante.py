"""
Simulando um caixa de restaurante, onde podemos fazer um pedido, escolher o prato, bebida 
e a forma de pagamento.
"""

# Declarando dados do estabelecimento
nomeEstabelecimento     = "RESTAURANTE DO RICCK";
enderecoEstabelecimento = "AVENIDA PRESIDENTE KENNEDY, 985";
bairroEstabelecimento   = "SÃO BERNARDO DO CAMPO";
cnpjEstabelecimento     = "13.790.883/0001-10";

# Declarando data atual
data = "04/08/2023";

# Definindo variável com o número do pedido
pedido = 221;

# Criando uma lista com o nome dos Atendentes
atendente = ["Ariel", "Diego", "Ricck", "Tati"];

# Criando dicionário com os pratos e valores
prato = {
    '1 - Filé de frango'              : 29.90,
    '2 - Filé de frango a parmegiana' : 34.90,
    '3 - Bife'                        : 35.90,
    '4 - Bife a parmegiana'           : 40.90,
    '5 - Bife de ancho'               : 55.90,
    '6 - Filé mignon'                 : 56.90,
    '7 - Beringela a parmegiana'      : 30.80,
    '8 - Salmão grelhado'             : 51.90,
    '9 - Strogonoff de frango'        : 31.80,
    '10 - Strogonoff de carne'        : 32.80
}

# Criando uma lista com os acompanhamentos
acompanhamento = ["1 - arroz branco", "2 - arroz com brócolis", "3 - feijão", "4 - batata frita",
                  "5 - batata rústica", "6 - purê de batata", "7 - farofa"];

# Criando um dicionário com as bebidas
bebida = {
    'Coca-Cola 250ml'        : 3.90,
    'Fanta laranja 250ml'    : 3.70,
    'Fanta guaraná 250ml'    : 3.70,
    'Guaraná antártica 250ml': 3.90,
    'Suco de laranja 500ml'  : 6.90
}

# Iniciando o funcionamento do sistema

# Escolhendo os itens
print();
print(prato);
print();
escolhaPrato = int(input("Digite o número do prato escolhido: "));
qtdPrato     = int(input("Digite a quantidade: "));
if escolhaPrato == 1:
    print("O prato escolhido foi Filé de frango!");
    escolhaPratoValor = prato["1 - Filé de frango"];
    escolhaPrato = "Filé de frango             ";
    print();
elif escolhaPrato == 2:
    print("O prato escolhido foi Filé de frango a parmegiana!");
    escolhaPratoValor = prato["2 - Filé de frango a parmegiana"];
    escolhaPrato = "Filé de frango a parmegiana";
    print();
elif escolhaPrato == 3:
    print("O prato escolhido foi Bife!");
    escolhaPratoValor = prato["3 - Bife"];
    escolhaPrato = "Bife                       ";
    print();
elif escolhaPrato == 4:
    print("O prato escolhido foi Bife a parmegiana!");
    escolhaPratoValor = prato["4 - Bife a parmegiana"];
    escolhaPrato = "Bife a parmegiana          ";
    print();
elif escolhaPrato == 5:
    print("O prato escolhido foi Bife de ancho!");
    escolhaPratoValor = prato["5 - Bife de ancho"];
    escolhaPrato = "Bife de ancho              ";
    print();
elif escolhaPrato == 6:
    print("O prato escolhido foi Filé mignon!");
    escolhaPratoValor = prato["6 - Filé mignon"];
    escolhaPrato = "Filé mignon                ";
    print();
elif escolhaPrato == 7:
    print("O prato escolhido foi Beringela a parmegiana!");
    escolhaPratoValor = prato["7 - Beringela a parmegiana"];
    escolhaPrato = "Beringela a parmegiana     ";
    print();
elif escolhaPrato == 8:
    print("O prato escolhido foi Salmão grelhado!");
    escolhaPratoValor = prato["8 - Salmão grelhado"];
    escolhaPrato = "Salmão grelhado            ";
    print();
elif escolhaPrato == 9:
    print("O prato escolhido foi Strogonoff de frango!");
    escolhaPratoValor = prato["9 - Strogonoff de frango"];
    escolhaPrato = "Strogonoff de frango       ";
    print();
else: 
    escolhaPrato == 10;
    print("O prato escolhido foi Strogonoff de carne!");
    escolhaPratoValor = prato["10 - Strogonoff de carne"];
    escolhaPrato = "Strogonoff de carne        ";
    print();

print("Escolha três acompanhamentos:")
print(acompanhamento);
escolhaAcompanhamento1 = int(input("Digite o número do primeiro acompanhamento: "));
escolhaAcompanhamento2 = int(input("Digite o número do segundo acompanhamento: "));
escolhaAcompanhamento3 = int(input("Digite o número do terceiro acompanhamento: "));

# Salvando o acompanhamento 1 em uma variável
if escolhaAcompanhamento1 == 1:
    escolhaAcompanhamento1 = acompanhamento[0];
elif escolhaAcompanhamento1 == 2:
    escolhaAcompanhamento1 = acompanhamento[1];
elif escolhaAcompanhamento1 == 3:
    escolhaAcompanhamento1 = acompanhamento[2];
elif escolhaAcompanhamento1 == 4:
    escolhaAcompanhamento1 = acompanhamento[3];
elif escolhaAcompanhamento1 == 5:
    escolhaAcompanhamento1 = acompanhamento[4];
elif escolhaAcompanhamento1 == 6:
    escolhaAcompanhamento1 = acompanhamento[5];
elif escolhaAcompanhamento1 == 7:
    escolhaAcompanhamento1 = acompanhamento[6];
    
# Salvando o acompanhamento 2 em uma variável
if escolhaAcompanhamento2 == 1:
    escolhaAcompanhamento2 = acompanhamento[0];
elif escolhaAcompanhamento2 == 2:
    escolhaAcompanhamento2 = acompanhamento[1];
elif escolhaAcompanhamento2 == 3:
    escolhaAcompanhamento2 = acompanhamento[2];
elif escolhaAcompanhamento2 == 4:
    escolhaAcompanhamento2 = acompanhamento[3];
elif escolhaAcompanhamento2 == 5:
    escolhaAcompanhamento2 = acompanhamento[4];
elif escolhaAcompanhamento2 == 6:
    escolhaAcompanhamento2 = acompanhamento[5];
elif escolhaAcompanhamento2 == 7:
    escolhaAcompanhamento2 = acompanhamento[6];
    
# Salvando o acompanhamento 3 em uma variável
if escolhaAcompanhamento3 == 1:
    escolhaAcompanhamento3 = acompanhamento[0];
elif escolhaAcompanhamento3 == 2:
    escolhaAcompanhamento3 = acompanhamento[1];
elif escolhaAcompanhamento3 == 3:
    escolhaAcompanhamento3 = acompanhamento[2];
elif escolhaAcompanhamento3 == 4:
    escolhaAcompanhamento3 = acompanhamento[3];
elif escolhaAcompanhamento3 == 5:
    escolhaAcompanhamento3 = acompanhamento[4];
elif escolhaAcompanhamento3 == 6:
    escolhaAcompanhamento3 = acompanhamento[5];
elif escolhaAcompanhamento3 == 7:
    escolhaAcompanhamento3 = acompanhamento[6];
    
print();

qtd = qtdPrato
valorTotal = escolhaPratoValor * qtdPrato;

# Simulando a impressão do pedido para o cliente
print();
print("---------------------------------------------------------------------------------");
print("                           ", nomeEstabelecimento);
print("---------------------------------------------------------------------------------");
print(enderecoEstabelecimento);
print(bairroEstabelecimento);
print("CNPJ:", cnpjEstabelecimento);
print("DATA:", data);
print("Operador:", atendente[2]);
print("----------------------------------------------------------------------------------");
print(" Qtd.  Descrição                                         Valor Unit.  Valor Total");
print(" ", qtd, "  ", escolhaPrato, "                           ", escolhaPratoValor, "       ", valorTotal);
print("----------------------------------------------------------------------------------");


print("==================================================================================");
print(f"Acompanhamentos: {escolhaAcompanhamento1}, {escolhaAcompanhamento2} e {escolhaAcompanhamento3}");
print("==================================================================================");
print();