# Classe base animal

class Animal:
    def __init__(self, nome):
        self.nome = nome;
    
    def emitirSom(self):
        pass

# Classe derivada: Cachorro (herda de Animal)

class Cachorro(Animal):
    def emitirSom(self):
        return "Au Au!";
    
# Classe derivada: Gato (herda de Animal)
class Gato(Animal):
    def emitirSom(self):
        return "Miau!";
    
# Classe derivada: Vaca (herda de Animal)
class Vaca(Animal):
    def emitirSom(self):
        return "Mooo!";
    
# Fução para emitir o som de um animal
def emitirSomAnimal(animal):
    print(animal.emitirSom());

# Criando objetos das classes derivadas
cachorro = Cachorro("Rex");
gato     = Gato("Tagarela");
vaca     = Vaca("Mimosa");

# Chamada do método emitir som para cada objeto (animal)

emitirSomAnimal(cachorro);
emitirSomAnimal(gato);
emitirSomAnimal(vaca);