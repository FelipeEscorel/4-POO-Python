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
    def __init__(self,nome, peso):
        self.aposentado = False
        self.aquecido = False
        self.nome = nome
        self.peso = peso
    def aquecer(self):
        print(f"O atleta {self.nome} aqueceu.")
        self.aquecido = True
    def aposentar(self):
        print(f"O atleta {self.nome} está se aposentando.")
        self.aposentado = True
class Corredor(Atleta):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)

    def correr(self):
        if self.aquecido == True:
            if self.aposentado == False:
                print(f"O corredor {self.nome} está correndo.")
            else:
                print(f"{self.nome} não pode correr pois está aposentado.")
        else:
            print(f"{self.nome} não pode correr porque não aqueceu.")
class Nadador(Atleta):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)
    def nadar(self):
        if self.aquecido == True:
            if self.aposentado == False:
                print(f"O nadador {self.nome} está nadando.")
            else:
                print(f"{self.nome} não pode nadar pois está aposentado.")
        else:
            print(f"{self.nome} não pode nadar porque não aqueceu.")
class Ciclista(Atleta):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)
    def pedalar(self):
        if self.aquecido == True:
            if self.aposentado == False:
                print(f"O ciclista {self.nome} está pedalando.")
            else:
                print(f"{self.nome} não pode pedalar pois está aposentado.")
        else:
            print(f"{self.nome} não pode pedalar porque não aqueceu.")
class Triatleta(Corredor, Nadador, Ciclista):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)

