meuDicionario = {
    'nome'     : 'Ricck', 
    'sobrenome': 'Gomes',
    'idade'    : 30
};
print();
print(meuDicionario);

# Acessando valores em um dicionário, usamos a palavra chave
frutaDicionario = {
    'maçã'  : 3,
    'banana': 6,
    'uva'   : 8,
};
print();
print("Localizando o significado no dicionário:");
print(frutaDicionario);
print("Significado encontrado no dicionário: ", frutaDicionario['maçã']);
print();

# Alterando valores das chaves
print("A quantidade de maçã será alterada!");
frutaDicionario["maçã"] = 5;
print("A nova quantidade de maçãs é: ", frutaDicionario["maçã"]);
print(frutaDicionario);
print();

# Adicionando valores no dicionário
frutaDicionario["goiaba"] = 9;
print("Fruta adicionada: ");
print(frutaDicionario);
print();

# Criando um dicionário vazio e em seguida atribuindo valores com []
animaisDicionario = {
    
};
animaisDicionario['cachorro'] = "Melissa";
print("Animal adicionado ao dicionário:")
print(animaisDicionario);
print();

# Adicionando uma lista em um dicionário
alunoDicionario = {
    'nome'   : 'Ricck',
    'idade'  : 30,
    'hobbies': ['jogar xadrez', 'jogar vôlei']
};
print(alunoDicionario);
print();

# Adicionando um dicionário dentro de outro dicionário e acessando o valor dentro dele
jogadorDicionario = {
    'nome'   : 'Ricck',
    'posicao': {'posicao1': 'libero',
                'posicao2': 'levantador'
                }
};
print("Acessando o dicionário dentro do dicionário:");
print(jogadorDicionario["posicao"]["posicao2"]);
print();

# Usando o método get() para acessar valores do dicionário
frutaDicionario = {
    'maçã'  : 3,
    'banana': 6,
    'uva'   : 8,
    'goiaba': 9,
};
print("Acessando uma fruta do dicionário:");
print("Quantidade de maçãs:", frutaDicionario.get("maçã"));
print("Quantidade de bananas:", frutaDicionario.get("banana"));

# Ao tentar acessar um valor que não temos em nosso dicionário com o método get() ele retorna NONE
print("Quantidade de morangos:", frutaDicionario.get("morando"));
# Com o método get() é possível deixar uma mensagem para sinalizar que não tem o valor no dicionário, e não retorna NONE
print("Quantidade de morangos:", frutaDicionario.get("morando", "Não foi encontrado a definição de morango."));
print();

# Removendo valores do nosso dicionário com o método pop()
frutaDicionario.pop("goiaba");
print("Dicionário atualizado:");
print(frutaDicionario);
print();

# Acessando chave com o método keys()
frutaDicionario = {
    'maçã'  : 3,
    'banana': 6,
    'uva'   : 8,
    'goiaba': 9,
};
print("Acessando as chaves:");
print(frutaDicionario.keys());
print();
# Acessando os valores das chaves com o método values()
print("Valores encontrados no dicionário:");
print(frutaDicionario.values());
print();
# Retorna uma lista com as chaves e seus valores com o método items()
print("Retornando as chaves e os valores:")
print(frutaDicionario.items());
print();