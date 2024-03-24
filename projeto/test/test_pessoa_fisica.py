"""This module does blah blah."""

import uuid

import pytest

from . import InvalidCpfException

from . import PessoaFisica

class TestPessoaFisica:

    """This module does blah blah."""

    def test_get_id(self):

        """This module does blah blah."""

        pessoa_fisica = PessoaFisica("João", 20, "18516803732")

        assert isinstance(pessoa_fisica.get_id(), uuid.UUID)

    def test_get_nome(self):

        """This module does blah blah."""

        pessoa_fisica = PessoaFisica("João", 20, "18516803732")

        assert pessoa_fisica.get_nome() == "João"

    def test_get_idade(self):

        """This module does blah blah."""

        pessoa_fisica = PessoaFisica("João", 20, "18516803732")

        assert pessoa_fisica.get_idade() == 20

    def test_get_cpf(self):

        """This module does blah blah."""

        pessoa_fisica = PessoaFisica("João", 20, "18516803732")

        assert pessoa_fisica.get_cpf() == "18516803732"


    def test_set_nome(self):

        """This module does blah blah."""

        pessoa_fisica = PessoaFisica("João", 20, "18516803732")

        pessoa_fisica.set_nome("Maykon")

        assert pessoa_fisica.get_nome() == "Maykon"

    def test_set_idade(self):

        """This module does blah blah."""

        pessoa_fisica = PessoaFisica("João", 20, "18516803732")

        pessoa_fisica.set_idade(23)

        assert pessoa_fisica.get_idade() == 23

    def test_set_cpf_valid(self):

        """This module does blah blah."""

        pessoa_fisica = PessoaFisica("João", 20, "18516803732")

        pessoa_fisica.set_cpf("99999999999")

        assert pessoa_fisica.get_cpf() == "99999999999"

    def test_set_cpf_invalid(self):

        """This module does blah blah."""

        with pytest.raises(InvalidCpfException):

            pessoa_fisica = PessoaFisica("João", 20, "18516803732")

            pessoa_fisica.set_cpf("12345678901")

    def test_verificar_cpf_invalid(self):

        """This module does blah blah."""

        with pytest.raises(InvalidCpfException):

            pessoa_fisica = PessoaFisica("João", 20, "12345678901") # pylint: disable=unused-variable
