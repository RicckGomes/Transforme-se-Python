# tupla não permite alteração de valores, ela é imutável
tupla1 = (1,2,3,4,5,6); # Declaramos uma tupla com parenteses
tupla2 = ("a", "b", "c", "d");
tupla3 = (1, "Hello", True);
tupla4 = 1,2,3,4,5,6; # Também podemos declarar uma tupla sem os parenteses, separando somente com virgulas
print(tupla1);
print(tupla2);
print(type(tupla3)); # type nos mostra o tipo de dado
print(type(tupla4));
print();

# Acessando itens especificos em uma tupla com []
print(tupla1[0]);
print(tupla2[2]);
print();

# Fatiamento de itens na tupla
print(tupla1[1:4]);
print();

# Concatenando tuplas
tupla5 = 1,2,3;
tupla6 = 4,5,6;
tupla7 = tupla5 + tupla6;
print("Concatenando tuplas: ", tupla7);
print();

# Criando variáveis novas com os valores de uma tupla
a, b, c = tupla6;
print();
print("Valores das variáveis; ")
print(a);
print(b);
print(c);