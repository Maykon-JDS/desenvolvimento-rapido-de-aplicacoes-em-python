class Aluno:
    
    _nome: str
    
    _idade: int 
    
    _cpf: str

    _matricula: str

    def __init__(self, nome:str, idade:int, cpf:str, matricula:str) -> None:
        
        self._nome = nome
    
        self._idade = idade
    
        self._cpf = cpf

        self._matricula = matricula

    def getNome(self) -> str:
        
        return self._nome
    
    def getIdade(self) -> int:
        
        return self._idade
    
    def getCpf(self) -> str:
        
        return self._cpf
    
    def getMatricula(self) -> str:
        
        return self._matricula
    
    def setNome(self, nome) -> None:
        
         self._nome = nome
    
    def setIdade(self, idade) -> None:
        
         self._idade = idade
    
    def setCpf(self, cpf) -> None:
        
         self._cpf = cpf
    
    def setMatricula(self, matricula) -> None:
        
         self._matricula = matricula