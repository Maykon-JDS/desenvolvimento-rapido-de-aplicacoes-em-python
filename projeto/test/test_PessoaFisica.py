import pytest

import uuid

from . import InvalidCpfException

from . import PessoaFisica

class TestPessoaFisica:

    def test_getId(self):
        
        pessoaFisica = PessoaFisica("João", 20, "18516803732")

        assert type(pessoaFisica.getId()) is uuid.UUID

    def test_getNome(self):

        pessoaFisica = PessoaFisica("João", 20, "18516803732")

        assert pessoaFisica.getNome() is "João"
        
    def test_getIdade(self):

        pessoaFisica = PessoaFisica("João", 20, "18516803732")

        assert pessoaFisica.getIdade() is 20
    
    def test_getCpf(self):

        pessoaFisica = PessoaFisica("João", 20, "18516803732")

        assert pessoaFisica.getCpf() is "18516803732"
        
    
    def test_setNome(self):

        pessoaFisica = PessoaFisica("João", 20, "18516803732")

        pessoaFisica.setNome("Maykon")

        assert pessoaFisica.getNome() is "Maykon"
        
    def test_setIdade(self):

        pessoaFisica = PessoaFisica("João", 20, "18516803732")

        pessoaFisica.setIdade(23)

        assert pessoaFisica.getIdade() is 23
            
    def test_setCpf_valid(self):

        pessoaFisica = PessoaFisica("João", 20, "18516803732")

        pessoaFisica.setCpf("99999999999")

        assert pessoaFisica.getCpf() is "99999999999"

    def test_setCpf_invalid(self):

        with pytest.raises(InvalidCpfException):

            pessoaFisica = PessoaFisica("João", 20, "18516803732")

            pessoaFisica.setCpf("12345678901")

    # def _verificarCpf(self):
        
    #     cpfSplit = [*cpf]

    #     cpfMultiplicadoPrimeiroDigito = list()

    #     cpfMultiplicadoSegundoDigito = list()

    #     fatorMultiplicador = 11

    #     for caracter in cpfSplit:
                
    #         if(fatorMultiplicador >= 3):

    #             cpfMultiplicadoPrimeiroDigito.append((int(caracter) * (fatorMultiplicador - 1)))

    #         if(fatorMultiplicador >= 2):

    #             cpfMultiplicadoSegundoDigito.append((int(caracter) * fatorMultiplicador))    

    #         fatorMultiplicador -= 1

    #     somatorioCaracterMultiplicadoCpfPrimeiroDigito = sum(cpfMultiplicadoPrimeiroDigito)
        
    #     somatorioCaracterMultiplicadoCpfSegundoDigito = sum(cpfMultiplicadoSegundoDigito)

    #     divisor = 11

    #     restoSomatorioCpfPrimeiroDigito = somatorioCaracterMultiplicadoCpfPrimeiroDigito % divisor

    #     restoSomatorioCpfSegundoDigito = somatorioCaracterMultiplicadoCpfSegundoDigito % divisor

    #     primeiroDigitoVerificador = divisor - restoSomatorioCpfPrimeiroDigito

    #     segundoDigitoVerificador = divisor - restoSomatorioCpfSegundoDigito

    #     if(not (str(primeiroDigitoVerificador) == cpf[9] and str(segundoDigitoVerificador) == cpf[10])):
            
    #         raise Exception("CPF invalido!")