import uuid

from .Turma import Turma #Não sei pq é assim

from .Aluno import Aluno #Não sei pq é assim

class Instituicao:
    
    _id: uuid

    _nome: str
    
    _turmas: list[Turma]

    def __init__(self, nome:str, tumas:list[Turma] = list()) -> None:
        
        self._id = uuid.uuid4()

        self._nome = nome

        self._turmas = tumas

    def getId(self) -> uuid:

        return self._id  

    def getListaAlunos(self) -> list[Aluno]:

        alunos = list()

        for turma in self._turmas:
            
            for aluno in turma.getAlunos():
                
                alunos.append(aluno)
        
        return alunos
    
    def getNome(self) -> str:

        return self._nome  

    def getTurmas(self) -> list[Turma]:
        
        return self._turmas
    
    def setNome(self, nome:str) -> None:

        self._nome = nome  

    def setTurmas(self, tumas:list[Turma]) -> None:
        
        self._turmas = tumas
    
    def appendTurma(self, turma:Turma) -> None:
        
        self._turmas.append(turma)
         
    def popTurma(self) -> None:
        
        self._turmas.pop()

    def clearTurmas(self) -> None:

        self._turmas.clear()
