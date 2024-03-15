import uuid

from .Aluno import Aluno #Não sei pq é assim

class Turma:
        
    _id: str
    
    _disciplina: str 
    
    _turno: str

    _horario: dict

    _alunos: list[Aluno]

    def __init__(self, disciplina:str, turno:str, horario:dict = {"inicio": '00:00:00', "fim": "00:00:00"}, alunos:list[Aluno] = list()) -> None:
        
        self._id = uuid.uuid4()

        self._disciplina = disciplina

        self._turno = turno

        self._horario = horario

        self._alunos = alunos

    
    
    def getId(self) -> str:
        pass

    def getDisciplina(self) -> str:
        pass

    def getTurno(self) -> str:
        pass

    def getHorario(self) -> dict:
        pass

    def getAlunos(self) -> list[Aluno]:
        pass
    
    def setDisciplina(self, disciplina:str) -> str:
        pass

    def setTurno(self, turno:str) -> str:
        pass

    def setHorario(self, horario:dict) -> dict:
        pass

    def setAlunos(self, alunos:list[Aluno]) -> list[Aluno]:
        pass

    