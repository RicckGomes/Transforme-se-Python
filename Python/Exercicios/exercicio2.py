"""
1 - Crie uma lista chamada "frutas" contendo as seguintes frutas:
maçã, banana, laranja, abacaxi e melancia. Em seguida, exiba a
lista completa na tela.
"""

# Criando lista com as frutas solicitadas
frutas = ["maçã", "banana", "laranja", "abacaxi", "melancia"];
print();
print("Olá, temos as seguintes frutas:", frutas);
print();

"""
2- Adicione a fruta "uva" à lista "frutas" utilizando o método
append(). Exiba a lista atualizada na tela.
"""

frutas.append("graviola");
print("Olá, temos novidade no nosso catálogo de frutas:", frutas);
print();

"""
3- emova a fruta "banana" da lista "frutas" utilizando o método
remove(). Exiba a lista atualizada na tela.
"""

frutaRemovida = frutas.remove("banana");
print("Nosso estoque de frutas foi atualizado:", frutas);
print();

"""
4- Acesse o segundo elemento da lista "frutas" e armazene-o em
uma variável chamada "fruta_selecionada". Em seguida, exiba o
valor armazenado na variável.
"""

frutaSelecionada = frutas[1];
print("A fruta selecionada é:", frutaSelecionada);
print();

"""
5- Crie uma tupla chamada "cores" contendo as seguintes cores:
vermelho, azul, verde, amarelo e roxo. Em seguida, exiba a tupla
completa na tela.
"""

cores = ("vermelho", "azul", "verde", "amarelo", "roxo");
print("Aqui estão as cores:", cores);
print();

"""
6- Acesse o terceiro elemento da tupla "cores" e armazene-o em
uma variável chamada "cor_selecionada". Em seguida, exiba o
valor armazenado na variável.
"""

corSelecionada = cores[2];
print("A cor selecionada foi:" , corSelecionada)
print();

"""
7- Tente adicionar a cor "laranja" à tupla "cores" e observe o
resultado. Explique o motivo pelo qual ocorreu um erro fazendo
um comentário no código.
"""

# O erro aconteceu porque não é possível adicionar valores em uma tupla, ela é imutável!
#adicionarCor = cores.append("laranja");
#print(adicionarCor);

"""
8- Crie um dicionário chamado "aluno" contendo as seguintes
informações: nome, idade e cidade. Utilize as chaves "nome",
"idade" e "cidade" para representar cada informação. Em seguida,
exiba o dicionário completo na tela.
"""

aluno = {
    'nome'  : 'Ricck',
    'idade' : 31,
    'cidade': 'Embu das Artes',
};
print("Os dados do aluno é:");
print(aluno);
print();

"""
9- Acesse a idade do aluno no dicionário "aluno" e armazene-o em
uma variável chamada "idade_aluno". Em seguida, exiba o valor
armazenado na variável.
"""

idadeAluno = aluno["idade"];
print(f"O aluno tem {idadeAluno} anos.");
print();

"""
10- Adicione a informação do gênero do aluno ao dicionário
"aluno" utilizando a chave "gênero" e o valor correspondente. Exiba
o dicionário atualizado na tela.
"""

aluno['gênero'] = "masculino";
print("Os dados do aluno foram atualizados.");
print(aluno);
print();

"""
11- Remova a informação da cidade do dicionário "aluno"
utilizando o método pop() e a chave correspondente. Exiba o
dicionário atualizado na tela.
"""

aluno.pop("cidade");
print("Dicionário atualizado.");
print(aluno);
print();