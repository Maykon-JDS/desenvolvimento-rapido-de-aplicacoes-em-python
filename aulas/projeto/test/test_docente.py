"""This module does blah blah."""

from . import Docente

from . import Disciplina

class TestDocente:

    """This module does blah blah."""

    def test_get_disciplinas_habilitadas_para_lecionar(self):

        """This module does blah blah."""

        disciplina1 = Disciplina('TI')

        disciplina2 = Disciplina('Administracao')

        docente = Docente("Maykon", 35, "18516803732", [disciplina1, disciplina2])

        assert docente.get_disciplinas_habilitadas_para_lecionar() == [disciplina1, disciplina2]

    def test_set_disciplinas_habilitadas_para_lecionar(self) -> None:

        """This module does blah blah."""

        disciplina1 = Disciplina('TI')

        disciplina2 = Disciplina('Administracao')

        docente = Docente("Maykon", 35, "18516803732", [disciplina1, disciplina2])

        disciplina3  = Disciplina('Direito')

        docente.set_disciplinas_habilitadas_para_lecionar([disciplina3])

        assert docente.get_disciplinas_habilitadas_para_lecionar() == [disciplina3]

        docente.set_disciplinas_habilitadas_para_lecionar([])

        assert docente.get_disciplinas_habilitadas_para_lecionar() == []
