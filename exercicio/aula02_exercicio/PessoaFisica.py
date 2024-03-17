import uuid

class PessoaFisica:
    
    _id: uuid
    
    _nome: str
    
    _idade: int 
    
    _cpf: str

    def __init__(self, nome:str, idade:int, cpf:str) -> None:
        
        self._id = uuid.uuid4()

        self._nome = nome
    
        self._idade = idade
    
        self._cpf = cpf

    def getId(self) -> uuid:
        
        return self._id        

    def getNome(self) -> str:
        
        return self._nome
    
    def getIdade(self) -> int:
        
        return self._idade
    
    def getCpf(self) -> str:
        
        return self._cpf
    
    def setNome(self, nome) -> None:
        
        self._nome = nome
    
    def setIdade(self, idade) -> None:
        
        self._idade = idade
    
    def setCpf(self, cpf) -> None:
        
        self._cpf = cpf