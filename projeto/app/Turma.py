"""This module does blah blah."""

import uuid

from .aluno import Aluno #Não sei pq é assim

from .docente import Docente #Não sei pq é assim

from .disciplina import Disciplina

from .turno import Turno

class Turma:

    """This module does blah blah."""

    _id: uuid

    _disciplina: Disciplina

    _turno: Turno

    _horario: dict

    _alunos: list[Aluno]

    _docente: Docente

    def __init__(self, disciplina:Disciplina, docente:Docente, turno:Turno,
                 horario:dict = {"inicio": '00:00:00', "fim": "00:00:00"},
                 alunos:list[Aluno] = []) -> None:

        self._id = uuid.uuid4()

        self._disciplina = disciplina

        self._docente = docente

        self._turno = turno

        self._horario = horario

        self._alunos = alunos

    def get_id(self) -> str:

        """This module does blah blah."""

        return self._id

    def get_disciplina(self) -> Disciplina:

        """This module does blah blah."""

        return self._disciplina

    def get_docente(self) -> Docente:

        """This module does blah blah."""

        return self._docente

    def get_turno(self) -> Turno:

        """This module does blah blah."""

        return self._turno

    def get_horario(self) -> dict:

        """This module does blah blah."""

        return self._horario

    def get_alunos(self) -> list[Aluno]:

        """This module does blah blah."""

        return self._alunos

    def set_disciplina(self, disciplina:Disciplina) -> None:

        """This module does blah blah."""

        self._disciplina = disciplina

    def set_docente(self, docente:Docente) -> None:

        """This module does blah blah."""

        self._docente = docente

    def set_turno(self, turno:Turno) -> None:

        """This module does blah blah."""

        self._turno = turno

    def set_horario(self, horario:dict) -> None:

        """This module does blah blah."""

        self._horario = horario

    def set_alunos(self, alunos:list[Aluno]) -> None:

        """This module does blah blah."""

        self._alunos = alunos

    def append_aluno(self, aluno:Aluno) -> None:

        """This module does blah blah."""

        self._alunos.append(aluno)

    def pop_aluno(self) -> None:

        """This module does blah blah."""

        self._alunos.pop()

    def _verificar_se_docente_habilitado_para_disciplina(self):
        pass
