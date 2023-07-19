class MinhaClasse:
    def __init__(self):
        self._atributo_protected = 42;
        
    def __metodo_private(self):
        print("Esse método é private!");
        
    def acessarMetodoPrivate(self):
        self.__metodo_private();
        
objeto = MinhaClasse();
#objeto.__metodo_private(); # Acesso NÃO é permitido diretamente

objeto.acessarMetodoPrivate(); # Permite o acesso ao método privado, mas não diretamente
    