"""This module does blah blah."""

import uuid

from . import Aluno

from . import Disciplina

from . import Docente

from . import Turno

from . import Turma

from . import Instituicao

class TestInstituicao:

    """This module does blah blah."""

    def test_get_id(self):

        """This module does blah blah."""

        instituicao = Instituicao("Estácio de Sá", [])

        assert isinstance(instituicao.get_id(), uuid.UUID)

    def test_get_lista_alunos(self):

        """This module does blah blah."""

        aluno1 = Aluno("João", 19, "18516803732")

        aluno2 = Aluno("Maykon", 21, "18516803732")

        aluno3 = Aluno("Pedro", 24, "18516803732")

        turma1 = Turma(
                        Disciplina("TI"),
                        Docente("Pedro", 44, "99999999999", [Disciplina("TI")]),
                        Turno('Manha'),
                        {"inicio": '06:00:00', "fim": "12:00:00"},
                        [aluno1, aluno2, aluno3])

        aluno4 = Aluno("Lucas", 19, "18516803732")

        aluno5 = Aluno("Julia", 21, "18516803732")

        aluno6 = Aluno("Carlos", 24, "18516803732")

        turma2 = Turma(
                        Disciplina("TI"),
                        Docente("Antônio", 50, "99999999999", [Disciplina("TI")]),
                        Turno('Manha'),
                        {"inicio": '06:00:00', "fim": "12:00:00"},
                        [aluno4, aluno5, aluno6])

        instituicao = Instituicao("Estácio de Sá", [turma1, turma2])

        assert  instituicao.get_lista_alunos() == [aluno1, aluno2, aluno3, aluno4, aluno5, aluno6]

    def test_get_nome(self):

        """This module does blah blah."""

        instituicao = Instituicao("Estácio de Sá", [])

        assert  instituicao.get_nome() == "Estácio de Sá"

    def test_get_turmas(self):

        """This module does blah blah."""

        turma1 = Turma(
                        Disciplina("TI"),
                        Docente("Pedro", 44, "99999999999", [Disciplina("TI")]),
                        Turno('Manha'),
                        {"inicio": '06:00:00', "fim": "12:00:00"},
                        [Aluno("Maykon", 21, "18516803732")])

        turma2 = Turma(
                        Disciplina("TI"),
                        Docente("Antônio", 50, "99999999999", [Disciplina("TI")]),
                        Turno('Manha'),
                        {"inicio": '06:00:00', "fim": "12:00:00"},
                        [Aluno("João", 19, "18516803732")])

        instituicao = Instituicao("Estácio de Sá", [turma1, turma2])

        assert  instituicao.get_turmas() == [turma1, turma2]

    def test_set_nome(self):

        """This module does blah blah."""

        instituicao = Instituicao("Estácio de Sá", [])

        instituicao.set_nome("Pedro II")

        assert  instituicao.get_nome() == "Pedro II"


    def test_set_turmas(self):

        """This module does blah blah."""

        turma1 = Turma(
                        Disciplina("Direito"),
                        Docente("Pedro", 44, "99999999999", [Disciplina("Direito")]),
                        Turno('Manha'),
                        {"inicio": '06:00:00', "fim": "12:00:00"},
                        [Aluno("Maykon", 21, "18516803732")])

        turma2 = Turma(
                        Disciplina("TI"),
                        Docente("Antônio", 50, "99999999999", [Disciplina("TI")]),
                        Turno('Manha'),
                        {"inicio": '06:00:00', "fim": "12:00:00"},
                        [Aluno("João", 19, "18516803732")])

        turma3 = Turma(
                        Disciplina("Administracao"),
                        Docente("Antônio", 50, "99999999999", [Disciplina("Administracao")]),
                        Turno('Manha'),
                        {"inicio": '06:00:00', "fim": "12:00:00"},
                        [Aluno("João", 19, "18516803732")])

        instituicao = Instituicao("Estácio de Sá", [turma1])

        instituicao.set_turmas([turma2, turma3])

        assert instituicao.get_turmas() == [turma2, turma3]

    def test_append_turma(self):

        """This module does blah blah."""

        turma1 = Turma(
                        Disciplina("Direito"),
                        Docente("Pedro", 44, "99999999999", [Disciplina("Direito")]),
                        Turno('Manha'),
                        {"inicio": '06:00:00', "fim": "12:00:00"},
                        [Aluno("Maykon", 21, "18516803732")])

        turma2 = Turma(
                        Disciplina("TI"),
                        Docente("Antônio", 50, "99999999999", [Disciplina("TI")]),
                        Turno('Manha'),
                        {"inicio": '06:00:00', "fim": "12:00:00"},
                        [Aluno("João", 19, "18516803732")])

        turma3 = Turma(
                        Disciplina("Administracao"),
                        Docente("Antônio", 50, "99999999999", [Disciplina("Administracao")]),
                        Turno('Manha'),
                        {"inicio": '06:00:00', "fim": "12:00:00"},
                        [Aluno("João", 19, "18516803732")])

        instituicao = Instituicao("Estácio de Sá", [turma1])

        instituicao.append_turma(turma2)

        assert instituicao.get_turmas() == [turma1, turma2]

        instituicao.append_turma(turma3)

        assert instituicao.get_turmas() == [turma1, turma2, turma3]

    def test_pop_turma(self):

        """This module does blah blah."""

        turma1 = Turma(
                        Disciplina("Direito"),
                        Docente("Pedro", 44, "99999999999", [Disciplina("Direito")]),
                        Turno('Manha'),
                        {"inicio": '06:00:00', "fim": "12:00:00"},
                        [Aluno("Maykon", 21, "18516803732")])

        turma2 = Turma(
                        Disciplina("TI"),
                        Docente("Antônio", 50, "99999999999", [Disciplina("TI")]),
                        Turno('Manha'),
                        {"inicio": '06:00:00', "fim": "12:00:00"},
                        [Aluno("João", 19, "18516803732")])

        turma3 = Turma(
                        Disciplina("Administracao"),
                        Docente("Antônio", 50, "99999999999", [Disciplina("Administracao")]),
                        Turno('Manha'),
                        {"inicio": '06:00:00', "fim": "12:00:00"},
                        [Aluno("João", 19, "18516803732")])

        instituicao = Instituicao("Estácio de Sá", [turma1, turma2, turma3])

        instituicao.pop_turma()

        assert instituicao.get_turmas() == [turma1, turma2]

        instituicao.pop_turma()

        assert instituicao.get_turmas() == [turma1]

        instituicao.pop_turma()

        assert instituicao.get_turmas() == []
