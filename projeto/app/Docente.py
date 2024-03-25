"""This module does blah blah."""

from .pessoa_fisica import PessoaFisica

from .disciplina import Disciplina

class Docente(PessoaFisica):

    """This module does blah blah."""

    _disciplinas_habilitadas_para_lecionar: [Disciplina] or [None]

    def __init__(   self, # pylint: disable=dangerous-default-value
                    nome: str,
                    idade: int,
                    cpf: str,
                    disciplinas_habilitadas_para_lecionar: [Disciplina] = [None]) -> None:

        super().__init__(nome, idade, cpf)

        self._disciplinas_habilitadas_para_lecionar = disciplinas_habilitadas_para_lecionar

    def get_disciplinas_habilitadas_para_lecionar(self) -> [Disciplina] or [None]:

        """This module does blah blah."""

        return self._disciplinas_habilitadas_para_lecionar

    def set_disciplinas_habilitadas_para_lecionar(  self,
                                                    disciplinas_habilitadas_para_lecionar:
                                                    [Disciplina] or [None]) -> None:

        """This module does blah blah."""

        self._disciplinas_habilitadas_para_lecionar = disciplinas_habilitadas_para_lecionar
