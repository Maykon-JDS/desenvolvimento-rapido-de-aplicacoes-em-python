import uuid

from Aluno import Aluno #Não sei pq é assim

from Disciplina import Disciplina

from Turno import Turno

class Turma:
        
    _id: uuid
    
    _disciplina: Disciplina 
    
    _turno: Turno

    _horario: dict

    _alunos: list[Aluno]

    def __init__(self, disciplina:Disciplina, turno:Turno, horario:dict = {"inicio": '00:00:00', "fim": "00:00:00"}, alunos:list[Aluno] = list()) -> None:
        
        self._id = uuid.uuid4()

        self._disciplina = disciplina

        self._turno = turno

        self._horario = horario

        self._alunos = alunos
    
    def getId(self) -> str:

        return self._id

    def getDisciplina(self) -> Disciplina:
        
        return self._disciplina

    def getTurno(self) -> Turno:
        
        return self._turno

    def getHorario(self) -> dict:
        
        return self._horario

    def getAlunos(self) -> list[Aluno]:
        
        return self._alunos
    
    def setDisciplina(self, disciplina:Disciplina) -> None:
        
        self._disciplina = disciplina

    def setTurno(self, turno:Turno) -> None:
        
        self._turno = turno

    def setHorario(self, horario:dict) -> None:
        
        self._horario = horario

    def setAlunos(self, alunos:list[Aluno]) -> None:
        
        self._alunos = alunos
    
    def appendAluno(self, aluno:Aluno) -> None:
        
        self._alunos.append(aluno)

    def popAluno(self) -> None:
        
        self._alunos.pop()

    