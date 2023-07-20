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
    '1 - Coca-Cola 250ml'        : 3.90,
    '2 - Fanta laranja 250ml'    : 3.70,
    '3 - Fanta guaraná 250ml'    : 3.70,
    '4 - Guaraná antártica 250ml': 3.90,
    '5 - Suco de laranja 500ml'  : 6.90
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
 
 # Escolhendo a bebida   
print();
print(bebida);
print();
escolhaBebida = int(input("Digite o número da bebida escolhida: "));
qtdBebidas    = int(input("Digite a quantidade: "));
if escolhaBebida == 1:
    print("A bebida escolhida foi Coca-Cola 250ml!");
    escolhaBebidaValor = bebida["1 - Coca-Cola 250ml"];
    escolhaBebida = "Coca-Cola 250ml            ";
    print();
elif escolhaBebida == 2:
    print("A bebida escolhida foi Fanta laranja 250ml!");
    escolhaBebidaValor = bebida["2 - Fanta laranja 250ml"];
    escolhaBebida = "Fanta laranja 250ml        ";
    print();
elif escolhaBebida == 3:
    print("A bebida escolhida foi Fanta guaraná 250ml!");
    escolhaBebidaValor = bebida["3 - Fanta guaraná 250ml"];
    escolhaBebida = "Fanta guaraná 250ml        ";
    print();
elif escolhaBebida == 4:
    print("A bebida escolhida foi Guaraná antártica 250ml!");
    escolhaBebidaValor = bebida["4 - Guaraná antártica 250ml"];
    escolhaBebida = "Guaraná antártica 250ml    ";
    print();
elif escolhaBebida == 5:
    print("A bebida escolhida foi Suco de laranja 500ml!");
    escolhaBebidaValor = bebida["5 - Suco de laranja 500ml"];
    escolhaBebida = "Suco de laranja 500ml      ";
    print();

print();

qtd = qtdPrato;
valorTotalPrato = escolhaPratoValor * qtdPrato;
qtd2 = qtdBebidas;
valorTotalBebidas = escolhaBebidaValor * qtdBebidas;

qtdTotal = qtd ++ qtd2;
valorTotal = valorTotalPrato ++ valorTotalBebidas;

print(f"O total é: {valorTotal:.2f}");
valorPago = float(input("Informe o valor pago: "));

while valorPago < valorTotal:
    print("O valor informado é inferior ao valor total.");
    valorPago = float(input("Informe o valor pago: "));
    if valorPago == valorTotal:
        break

# Simulando a impressão do pedido para o cliente
print();
print("==================================================================================");
print("                           ", nomeEstabelecimento);
print("==================================================================================");
print(enderecoEstabelecimento);
print(bairroEstabelecimento);
print("CNPJ:", cnpjEstabelecimento);
print("DATA:", data);
print("Operador:", atendente[1]);
print("==================================================================================");
print(" Qtd.  Descrição                                         Valor Unit.  Valor Total");
print(f"  {qtd}    {escolhaPrato}                             {escolhaPratoValor:.2f}        {valorTotalPrato:.2f}");
print(f"  {qtd2}    {escolhaBebida}                              {escolhaBebidaValor:.2f}        {valorTotalBebidas:.2f}");
print()
print("==================================================================================");
print(f"Acompanhamentos: {escolhaAcompanhamento1}, {escolhaAcompanhamento2} e {escolhaAcompanhamento3}");
print("==================================================================================");
print("Quantidade de itens lançados: ", qtdTotal);
print();
print(f"                                      VALOR TOTAL: {valorTotal:.2f}");
print("                                     ----------------------");
print(f"                                       VALOR PAGO: {valorPago:.2f}");
print();
print("==================================================================================");
print("                             NÃO É DOCUMENTO FISCAL");
print("==================================================================================");
print();