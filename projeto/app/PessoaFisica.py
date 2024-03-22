print("tetsetetet")

import uuid

from .InvalidCpfException import InvalidCpfException

class PessoaFisica:
    
    _id: uuid
    
    _nome: str
    
    _idade: int 
    
    _cpf: str

    def __init__(self, nome:str, idade:int, cpf:str) -> None:
        
        self._id = uuid.uuid4()

        self._nome = nome
    
        self._idade = idade
    
        self._verificarCpf(cpf)

        self._cpf = cpf

    def getId(self) -> uuid:
        
        return self._id        

    def getNome(self) -> str:
        
        return self._nome
    
    def getIdade(self) -> int:
        
        return self._idade
    
    def getCpf(self) -> str:
        
        return self._cpf
    
    def setNome(self, nome) -> None:
        
        self._nome = nome
    
    def setIdade(self, idade) -> None:
        
        self._idade = idade
    
    def setCpf(self, cpf) -> None:

        self._verificarCpf(cpf)
        
        self._cpf = cpf

    def _verificarCpf(self, cpf:str) -> None:
        
        cpfSplit = [*cpf]

        cpfMultiplicadoPrimeiroDigito = list()

        cpfMultiplicadoSegundoDigito = list()

        fatorMultiplicador = 11

        for caracter in cpfSplit:
                
            if(fatorMultiplicador >= 3):

                cpfMultiplicadoPrimeiroDigito.append((int(caracter) * (fatorMultiplicador - 1)))

            if(fatorMultiplicador >= 2):

                cpfMultiplicadoSegundoDigito.append((int(caracter) * fatorMultiplicador))    

            fatorMultiplicador -= 1

        somatorioCaracterMultiplicadoCpfPrimeiroDigito = sum(cpfMultiplicadoPrimeiroDigito)
        
        somatorioCaracterMultiplicadoCpfSegundoDigito = sum(cpfMultiplicadoSegundoDigito)

        # print(cpf)
        
        # print(cpfMultiplicadoPrimeiroDigito)
        
        # print(somatorioCaracterMultiplicadoCpfPrimeiroDigito)

        # print(cpfMultiplicadoSegundoDigito)

        # print(somatorioCaracterMultiplicadoCpfSegundoDigito)

        divisor = 11

        restoSomatorioCpfPrimeiroDigito = somatorioCaracterMultiplicadoCpfPrimeiroDigito % divisor

        restoSomatorioCpfSegundoDigito = somatorioCaracterMultiplicadoCpfSegundoDigito % divisor

        primeiroDigitoVerificador = divisor - restoSomatorioCpfPrimeiroDigito

        segundoDigitoVerificador = divisor - restoSomatorioCpfSegundoDigito

        # print(str(primeiroDigitoVerificador))
        # print(cpf[9])
        # print(str(segundoDigitoVerificador))
        # print(cpf[10])

        if(not (str(primeiroDigitoVerificador) == cpf[9] and str(segundoDigitoVerificador) == cpf[10])):
            
            raise InvalidCpfException("CPF invalido!")

        





