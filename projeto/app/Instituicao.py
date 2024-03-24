"""This module does blah blah."""

import uuid

from .turma import Turma #Não sei pq é assim

from .aluno import Aluno #Não sei pq é assim

class Instituicao:

    """This module does blah blah."""

    _id: uuid

    _nome: str

    _turmas: list[Turma]

    def __init__(self, nome:str, tumas:list[Turma] = [None]) -> None:  # pylint: disable=dangerous-default-value


        self._id = uuid.uuid4()

        self._nome = nome

        self._turmas = tumas

    def get_id(self) -> uuid:

        """This module does blah blah."""

        return self._id

    def get_lista_alunos(self) -> list[Aluno]:

        """This module does blah blah."""

        alunos = []

        for turma in self._turmas:

            for aluno in turma.get_alunos():

                alunos.append(aluno)

        return alunos

    def get_nome(self) -> str:

        """This module does blah blah."""

        return self._nome

    def get_turmas(self) -> list[Turma]:

        """This module does blah blah."""

        return self._turmas

    def set_nome(self, nome:str) -> None:

        """This module does blah blah."""

        self._nome = nome

    def set_turmas(self, tumas:list[Turma]) -> None:

        """This module does blah blah."""

        self._turmas = tumas

    def append_turma(self, turma:Turma) -> None:

        """This module does blah blah."""

        self._turmas.append(turma)

    def pop_turma(self) -> None:

        """This module does blah blah."""

        self._turmas.pop()
