class Aluno:
    def __init__(self):
        self.__nota1 = "nao informado"
        self.__nota2 = "nao informado"
        self.__nome = "nao informado"
    def getnota(self):
        return f"nota1 : {self.__nota1} e nota2 : {self.__nota2}"
    def setnota(self,nota1,nota2):
        self.__nota1 = nota1
        self.__nota2 = nota2
        
    def getnome(self):
        return f"nome : {self.__nome}"
    def setnome(self,nome):
        self.__nome = nome
    def media(self):
        if self.__nota1 == "nao informado" or self.__nota2 == "nao informado":
            return "nao informado"
        else:
            return f"media : {(self.__nota1+self.__nota2)/2}"
        
aluno1=Aluno()
aluno1.setnome("Felipe")
aluno1.setnota(6,4)
print(aluno1.getnome())
print(aluno1.getnota())
print(aluno1.media())