"""This module does blah blah."""

import uuid

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

    def test_set_disciplina(self):

        """This module does blah blah."""

        aluno = Aluno("João", 20, "18516803732")

        turma = Turma(Disciplina("TI"), Docente("Pedro", 44, "99999999999"), Turno('Manha'),
                     {"inicio": '00:00:00', "fim": "00:00:00"}, [aluno])

        turma.set_disciplina(Disciplina("Administracao"))

        assert isinstance(turma.get_disciplina(), Disciplina)

        assert turma.get_disciplina().value == Disciplina.ADMINISTRACAO.value

    def test_set_docente(self):

        """This module does blah blah."""

        turma = Turma(Disciplina("TI"), Docente("Pedro", 44, "99999999999"), Turno('Manha'),
                     {"inicio": '00:00:00', "fim": "00:00:00"}, [Aluno("João", 20, "18516803732")])

        docente = Docente("Carlos", 39, "99999999999")

        turma.set_docente(docente)

        assert isinstance(turma.get_docente(), Docente)

        assert turma.get_docente() == docente


    def test_set_turno(self):

        """This module does blah blah."""

        turma = Turma(Disciplina("TI"), Docente("Pedro", 44, "99999999999"), Turno('Manha'),
                     {"inicio": '00:00:00', "fim": "00:00:00"}, [Aluno("João", 20, "18516803732")])

        turma.set_turno(Turno("Tarde"))

        assert isinstance(turma.get_turno(), Turno)

        assert turma.get_turno().value == Turno.TARDE.value

    def test_set_horario(self):

        """This module does blah blah."""

        turma = Turma(Disciplina("TI"), Docente("Pedro", 44, "99999999999"), Turno('Manha'),
                     {"inicio": '00:00:00', "fim": "00:00:00"}, [Aluno("João", 20, "18516803732")])

        turma.set_horario({"inicio": '7:50:00', "fim": "11:30:00"})

        assert isinstance(turma.get_horario(), dict)

        assert turma.get_horario() == {"inicio": '7:50:00', "fim": "11:30:00"}

    def test_set_alunos(self):

        """This module does blah blah."""

        aluno1 = Aluno("João", 20, "18516803732")

        aluno2 = Aluno("João", 30, "18516803732")

        aluno3 = Aluno("João", 40, "18516803732")

        turma = Turma(Disciplina("TI"), Docente("Pedro", 44, "99999999999"), Turno('Manha'),
                     {"inicio": '00:00:00', "fim": "00:00:00"}, [aluno1, aluno2, aluno3])

        aluno4 = Aluno("João", 50, "18516803732")

        aluno5 = Aluno("João", 35, "18516803732")

        aluno6 = Aluno("João", 25, "18516803732")

        turma.set_alunos([aluno4, aluno5, aluno6])

        assert turma.get_alunos() == [aluno4, aluno5, aluno6]

    def test_append_aluno(self):

        """This module does blah blah."""

        aluno1 = Aluno("João", 20, "18516803732")

        turma = Turma(Disciplina("TI"), Docente("Pedro", 44, "99999999999"), Turno('Manha'),
                     {"inicio": '00:00:00', "fim": "00:00:00"}, [aluno1])

        aluno2 = Aluno("João", 30, "18516803732")

        assert turma.get_alunos() == [aluno1]

        turma.append_aluno(aluno2)

        assert turma.get_alunos() == [aluno1, aluno2]

        aluno3 = Aluno("João", 40, "18516803732")

        turma.append_aluno(aluno3)

        assert turma.get_alunos() == [aluno1, aluno2, aluno3]

    def test_pop_aluno(self):

        """This module does blah blah."""

        aluno1 = Aluno("João", 20, "18516803732")

        aluno2 = Aluno("João", 30, "18516803732")

        aluno3 = Aluno("João", 40, "18516803732")

        turma = Turma(Disciplina("TI"), Docente("Pedro", 44, "99999999999"), Turno('Manha'),
                     {"inicio": '00:00:00', "fim": "00:00:00"}, [aluno1, aluno2, aluno3])

        turma.pop_aluno()

        assert turma.get_alunos() == [aluno1, aluno2]

        turma.pop_aluno()

        assert turma.get_alunos() == [aluno1]

        turma.pop_aluno()

        assert turma.get_alunos() == []
