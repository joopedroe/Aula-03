class Evento:
    def __init__(self,nome,local,data,horario):
        self.nome=nome
        self.local=local
        self.data=data
        self.horario=horario
    def __str__(self):
        return "Evento: {}   Local: {}   Data: {}".format(self.nome,self.local,self.data) 
class Pessoa:
    def __init__(self,nome, rg,data_nascimento,evento):
        self.nome=nome
        self.rg=rg
        self.data_nascimento=data_nascimento
        self.evento=evento
    def __str__(self):
        return "Nome: {}  RG: {}   Data de Nascimento; {}  \n {}".format(self.nome,self.rg,self.data_nascimento,self.evento)
    
class PessoaFisica(Pessoa):
    def __init__(self,cpf,nome, rg,data_nascimento,evento):
        super().__init__(nome, rg,data_nascimento,evento)
        self.cpf=cpf
        

class PessoaJuridica(Pessoa):
    def __init__(self,cnpj):
        super().__init__(nome, rg,data_nascimento,evento)
        self.cnpj=cnpj

class Autor(Pessoa):
    def __init__(self,nome, rg,data_nascimento,evento):
        super().__init__(nome, rg,data_nascimento,evento)
    

class Artigo:
    def __init__(self,titulo,data,instituto):
        self.titulo=titulo
        self.data=data
        self.instituto=instituto
class ArtigoAutor:
    def __init__(self,artigo,autor):
        self.artigo=artigo
        self.autor=autor

evento=Evento("ENCOINFO","CEULP","21/02/19","19:05")
autor=Autor("João Pedro","415115","03/09/18",evento)
print(autor)
