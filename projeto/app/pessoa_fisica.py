"""This module does blah blah."""

import uuid

from .invalid_cpf_exception import InvalidCpfException

class PessoaFisica:

    """This module does blah blah."""

    _id: uuid

    _nome: str

    _idade: int

    _cpf: str

    def __init__(self, nome:str, idade:int, cpf:str) -> None:

        self._id = uuid.uuid4()

        self._nome = nome

        self._idade = idade

        self._verificar_cpf(cpf)

        self._cpf = cpf

    def get_id(self) -> uuid:

        """This module does blah blah."""

        return self._id

    def get_nome(self) -> str:

        """This module does blah blah."""

        return self._nome

    def get_idade(self) -> int:

        """This module does blah blah."""

        return self._idade

    def get_cpf(self) -> str:

        """This module does blah blah."""

        return self._cpf

    def set_nome(self, nome) -> None:

        """This module does blah blah."""

        self._nome = nome

    def set_idade(self, idade) -> None:

        """This module does blah blah."""

        self._idade = idade

    def set_cpf(self, cpf) -> None:

        """This module does blah blah."""

        self._verificar_cpf(cpf)

        self._cpf = cpf

    def _verificar_cpf(self, cpf:str) -> None:

        """This module does blah blah."""

        cpf_split = [*cpf]

        cpf_multiplicado_primeiro_digito = []

        cpf_multiplicado_segundo_digito = []

        fator_multiplicador = 11

        for caracter in cpf_split:

            if fator_multiplicador >= 3:

                cpf_multiplicado_primeiro_digito.append((int(caracter) * (fator_multiplicador - 1)))

            if fator_multiplicador >= 2:

                cpf_multiplicado_segundo_digito.append((int(caracter) * fator_multiplicador))

            fator_multiplicador -= 1

        somatorio_caracter_multiplicado_cpf_primeiro_digito = sum(cpf_multiplicado_primeiro_digito)

        somatorio_caracter_multiplicado_cpf_segundo_digito = sum(cpf_multiplicado_segundo_digito)

        # print(cpf)

        # print(cpf_multiplicado_primeiro_digito)

        # print(somatorio_caracter_multiplicado_cpf_primeiro_digito)

        # print(cpf_multiplicado_segundo_digito)

        # print(somatorio_caracter_multiplicado_cpf_segundo_digito)

        divisor = 11

        resto_somatorio_cpf_primeiro_digito = \
        somatorio_caracter_multiplicado_cpf_primeiro_digito % divisor

        resto_somatorio_cpf_segundo_digito = \
        somatorio_caracter_multiplicado_cpf_segundo_digito % divisor

        primeiro_digito_verificador = \
        divisor - resto_somatorio_cpf_primeiro_digito

        segundo_digito_verificador = \
        divisor - resto_somatorio_cpf_segundo_digito

        # print(str(primeiro_digito_verificador))
        # print(cpf[9])
        # print(str(segundo_digito_verificador))
        # print(cpf[10])

        if not (str(primeiro_digito_verificador) == cpf[9] and
                str(segundo_digito_verificador) == cpf[10]):

            raise InvalidCpfException("CPF invalido!")

print("tetset_etet")
