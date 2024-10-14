class Pessoa:
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.falando = False
        self.comendo = False
        self.dormindo = False

    def falar(self, lingua):
        if self.falando == False:
            if self.dormindo == False:
                if self.comendo == False:
                    print(f"{self.nome} está falando {lingua}.")
                    self.falando = True
                else:
                    print(f"{self.nome} não pode falar, pois está comendo.")
            else:
                print(f"{self.nome} já está dormindo")
        else:
            print("Já está falando.")
    def parar_falar(self):
        print(f"{self.nome} parou de falar.")
        self.falando = False

    def comer(self, alimento):
        if self.comendo == False:
            if self.falando == False:
                if self.dormindo == False:
                    print(f"{self.nome} está comendo {alimento}")
                    self.comendo = True
                else:
                    print(f"{self.nome} não pode comer, pois está dormindo.")
            else:
                print(f"{self.nome} não pode comer, pois está falando.")
        else:
            print(f"{self.nome} já está comendo.")
    def parar_comer(self):
        print(f"{self.nome} parou de comer.")

    def dormir(self):
        if self.dormindo == False:
            if self.comendo == False:
                if self.falando == False:
                    print(f"{self.nome} está dormindo.")
                    self.comendo = True
                else:
                    print(f"{self.nome} não pode dormir, pois está falando.")
            else:
                print(f"{self.nome} não pode dormir, pois está comendo.")
        else:
            print(f"{self.nome} já está dormindo.")
    def acordar(self):
        print(f"{self.nome} acordou.")

class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"{self.nome}, de cor {self.cor}, está comendo.")
class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def miar(self):
        print(f"O {self.nome} está miando.")
class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def latir(self):
        print(f"O {self.nome} está latindo.")
class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def mugir(self):
        print(f"A {self.nome} está mugindo.")

class Atleta:
    def __init__(self,peso):
        self.aposentado = False
        self.peso = peso
    def aquecer(self):
        print("O atleta está aquecendo.")
    def aposentar(self):
        print("O atleta está se aposentado.")
class Corredor(Atleta):
    def __init__(self, peso):
        super().__init__(peso)

    def correr(self):
        print("O atleta está correndo.")
class Nadador(Atleta):
    def __init__(self, peso):
        super().__init__(peso)
    def nadar(self):
        print("O atleta está nadando.")
class Ciclista(Atleta):
    def __init__(self, peso):
        super().__init__(peso)
    def pedalar(self):
        print("O atleta está pedalando.")
