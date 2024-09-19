class Empregado:
    def __init__(self,nome,salario_base):
        self.nome = nome
        self.salario_base = salario_base
class Gerente(Empregado):
    def __init__(self,nome,salario_base,bonus):
        super().__init__(nome,salario_base)
        self.bonus = bonus
    def getsalario(self):
        return f"{self.nome} = {self.salario_base+self.bonus}"
class Vendedor(Empregado):
    def __init__(self,nome,salario_base,vendas):
        super().__init__(nome,salario_base)
        self.vendas = vendas
    def getsalario(self):
        return f"{self.nome} = {self.salario_base+self.vendas*0.1}"
func=Vendedor("pedro",1000,5000)
print(func.getsalario())
gere=Gerente("maria",2000,1500)
print(gere.getsalario())