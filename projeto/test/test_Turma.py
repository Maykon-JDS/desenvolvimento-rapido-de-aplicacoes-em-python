"""This module does blah blah."""

import uuid

# import pytest

from . import Aluno

from . import Disciplina

from . import Docente

from . import Turno

from . import Turma

class TestTurma:

    """This module does blah blah."""

    def test_get_id(self):

        """This module does blah blah."""

        turma = Turma(Disciplina("TI"), Docente("Pedro", 44, "99999999999"), Turno('Manha'),
                     {"inicio": '00:00:00', "fim": "00:00:00"}, [Aluno("João", 20, "18516803732")])

        assert isinstance(turma.get_id(), uuid.UUID)

    def test_get_disciplina(self):

        """This module does blah blah."""

        turma = Turma(Disciplina("TI"), Docente("Pedro", 44, "99999999999"), Turno('Manha'),
                     {"inicio": '00:00:00', "fim": "00:00:00"}, [Aluno("João", 20, "18516803732")])

        assert isinstance(turma.get_disciplina(), Disciplina)

        assert turma.get_disciplina().value == Disciplina.TI.value

    def test_get_docente(self):

        """This module does blah blah."""

        turma = Turma(Disciplina("TI"), Docente("Pedro", 44, "99999999999"), Turno('Manha'),
                     {"inicio": '00:00:00', "fim": "00:00:00"}, [Aluno("João", 20, "18516803732")])

        assert isinstance(turma.get_docente(),  Docente)

    def test_get_turno(self):

        """This module does blah blah."""

        turma = Turma(Disciplina("TI"), Docente("Pedro", 44, "99999999999"), Turno('Manha'),
                     {"inicio": '00:00:00', "fim": "00:00:00"}, [Aluno("João", 20, "18516803732")])

        assert isinstance(turma.get_turno(), Turno)

        assert turma.get_turno().value == Turno.MANHA.value

    def test_get_horario(self):

        """This module does blah blah."""

        turma = Turma(Disciplina("TI"), Docente("Pedro", 44, "99999999999"), Turno('Manha'),
                     {"inicio": '00:00:00', "fim": "00:00:00"}, [Aluno("João", 20, "18516803732")])

        assert isinstance(turma.get_horario(), dict)

        assert turma.get_horario() == {"inicio": '00:00:00', "fim": "00:00:00"}


    def test_get_alunos(self):

        """This module does blah blah."""

        aluno = Aluno("João", 20, "18516803732")

        turma = Turma(Disciplina("TI"), Docente("Pedro", 44, "99999999999"), Turno('Manha'),
                     {"inicio": '00:00:00', "fim": "00:00:00"}, [aluno])

        assert isinstance(turma.get_alunos(), list)

        assert turma.get_alunos() == [aluno]

    # def test_setDisciplina(self, disciplina:Disciplina):

        # """This module does blah blah."""

    #     self._disciplina = disciplina

    # def test_setDocente(self, docente:Docente):

        # """This module does blah blah."""

    #     self._docente = docente

    # def test_setTurno(self, turno:Turno):

        # """This module does blah blah."""

    #     self._turno = turno

    # def test_setHorario(self, horario:dict):

        # """This module does blah blah."""

    #     self._horario = horario

    # def test_setAlunos(self, alunos:list[Aluno]):

        # """This module does blah blah."""

    #     self._alunos = alunos

    # def test_appendAluno(self, aluno:Aluno):

        # """This module does blah blah."""

    #     self._alunos.append(aluno)

    # def test_popAluno(self):

        # """This module does blah blah."""

    #     self._alunos.pop()
