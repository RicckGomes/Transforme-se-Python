class Cachorro:
    def __init__(self, nome, idade):
        self.nome  = nome;
        self.idade = idade;
        
    def latir(self):
        print(f"{self.nome} está latindo!");
        
    def anos(self):
        print(f"{self.nome} tem {self.idade} anos!");
        
# Criação de objetos da Classe Cachorro
cachorro1 = Cachorro("Max", 3);
cachorro2 = Cachorro("Melissa", 9);

# Chamada de métodos dos objetos
print();
cachorro1.latir();
print();
cachorro2.latir();
print();
cachorro1.anos();
print();