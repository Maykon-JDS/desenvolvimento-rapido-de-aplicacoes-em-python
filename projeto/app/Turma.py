"""This module does blah blah."""

import uuid

from datetime import datetime

from .aluno import Aluno #Não sei pq é assim

from .docente import Docente #Não sei pq é assim

from .disciplina import Disciplina

from .turno import Turno

from .without_permission_to_teach_the_subject import WithoutPermissionToTeachTheSubject

from .class_time_outside_the_defined_shift import ClassTimeOutsideTheDefinedShift

class Turma:

    """This module does blah blah."""

    _id: uuid

    _disciplina: Disciplina

    _turno: Turno

    _horario: dict

    _alunos: list[Aluno]

    _docente: Docente

    def __init__(   self,   # pylint: disable=dangerous-default-value, too-many-arguments
                    disciplina:Disciplina, docente:Docente, turno:Turno,
                    horario:dict = {"inicio": '00:00:00', "fim": "00:00:00"},
                    alunos:list[Aluno] = []) -> None:

        self._verificar_se_docente_habilitado_para_disciplina(disciplina, docente)

        self._verificar_turno(turno, horario)

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

        self._verificar_se_docente_habilitado_para_disciplina(disciplina, self._docente)

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

    def _verificar_se_docente_habilitado_para_disciplina(self,
                                                         disciplina: Disciplina,
                                                         docente: Docente) -> None:

        """This module does blah blah."""

        if not disciplina in docente.get_disciplinas_habilitadas_para_lecionar():

            raise WithoutPermissionToTeachTheSubject("O docente não tem permissão para lecionar essa disciplina") # pylint: disable=line-too-long

    def get_duracao_aula(self) -> str:

        """This module does blah blah."""

        tempo_inicio = datetime.strptime(self._horario['inicio'], "%H:%M:%S")

        tempo_fim = datetime.strptime(self._horario['fim'], "%H:%M:%S")

        tempo_delta = tempo_fim - tempo_inicio

        return  str(tempo_delta)

    def _verificar_turno(self, turno: Turno, horario: dict) -> None:

        """This module does blah blah."""

        tempo_inicio = datetime.strptime(horario['inicio'], "%H:%M:%S")

        tempo_fim = datetime.strptime(horario['fim'], "%H:%M:%S")

        tempo_inicio_manha = datetime.strptime("06:00:00", "%H:%M:%S")

        tempo_fim_manha = datetime.strptime("12:00:00", "%H:%M:%S")

        tempo_inicio_tarde = datetime.strptime("12:00:00", "%H:%M:%S")

        tempo_fim_tarde = datetime.strptime("18:00:00", "%H:%M:%S")

        tempo_inicio_noite = datetime.strptime("18:00:00", "%H:%M:%S")

        tempo_fim_noite = datetime.strptime("00:00:00", "%H:%M:%S")

        if turno == Turno.MANHA and not (tempo_inicio >= tempo_inicio_manha and tempo_fim <= tempo_fim_manha):

            raise ClassTimeOutsideTheDefinedShift("Horário fora do período de aula do turno da Manhã | (06:00:00 - 12:00:00)")

        elif turno == Turno.TARDE and not (tempo_inicio >= tempo_inicio_tarde and tempo_fim <= tempo_fim_tarde):

            raise ClassTimeOutsideTheDefinedShift("Horário fora do período de aula de Tarde | (12:00:00 - 18:00:00)")

        elif turno == Turno.NOITE and not (tempo_inicio >= tempo_inicio_noite and tempo_fim <= tempo_fim_noite):

            raise ClassTimeOutsideTheDefinedShift("Horário fora do período de aula de Noite | (18:00:00 - 00:00:00)")

    # def _verificar_duracao_aula(self, horario:dict) -> None:

    #     pass
