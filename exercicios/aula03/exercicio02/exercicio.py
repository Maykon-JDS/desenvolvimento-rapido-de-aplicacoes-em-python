import json
import os

class Aluno:

    def __init__(self,  nome: str, email: str, curso: str) -> None:
        self._nome  = nome 
        self._email = email 
        self._curso = curso 

    def getAluno(self) -> dict:

        return dict(nome = self._nome, email = self._email, curso = self._curso)
    
    def __str__(self) -> str:
        
        return str(self.getAluno())

class Arquivo: 

    def __init__(self, arquivo: str) -> None:
        
        self._arquivo = arquivo

    def escreverArquivo(self, dados: dict) -> None:
    
        arquivoAberto = open(self._arquivo, "+tr")

        qtdLinhas = len(arquivoAberto.readlines())

        dadosJson = json.dumps(dados, indent=4)

# TODO: Resolver problema de contagem de linhas do arquivo
        print(qtdLinhas)

        ajuste = ""

        if(qtdLinhas != 0):
            ajuste = ","
            

        arquivoAberto.write(f"{ajuste}{dadosJson}\n")

    def showArquivo(self) -> None:

        print(self.getArquivo())

    def getArquivo(self) -> str:

        arquivoAberto = open(self._arquivo, "r")

        return arquivoAberto.read()


class Main():

    def __init__(self) -> None:

        self.arquivo = Arquivo("/workspaces/projeto_rad/exercicios/aula03/exercicio02/arquivo.txt")

        self.loop()

    def loop(self) -> None:

        while True:

            print("1 - Cadastrar Aluno\n")
            print("2 - Listar Aluno\n")
            print("3 - Pesquisar Aluno\n")
            print("4 - Encerrar Programa\n\n")

            opcao = int(input(f"Informe o número da opção desejada: "))

            match opcao:
                case 1:
                    self.loopCadastarAluno()
                case 2:
                    self.showAlunos()
                case 3:
                    pass
                case 4:
                    print("Programa finalizado!")
                    break
                case _:
                    print(f"\nValor \"{opcao}\" inválido!\n")

    def cadastrarAluno(self):  
        
        nomeAluno = input(f"Digite o nome do novo aluno: ")
        emailAluno = input(f"Digite o email do novo aluno: ")
        cursoAluno = input(f"Digite o curso do novo aluno: ")

        novoAluno = Aluno(nomeAluno, emailAluno, cursoAluno)

        self.arquivo.escreverArquivo(novoAluno.getAluno())

    def loopCadastarAluno(self):

        resposta = 0

        while True:

            match resposta:
                case 0 | "s":
                    self.cadastrarAluno()
                case 'n':
                    print("Programa finalizado!")
                    break
                case _:
                    print(f"Valor {resposta} inválido!")

            resposta = input(f"Deseja cadastrar outro usuário? (s/n)\n")

    def showAlunos(self):

       os.system('clear')

       alunosJson = str(f"{self.arquivo.getArquivo()}")

       alunos = json.loads(str(f"[{alunosJson}]"))

       print(f"\nLista de Alunos:\n")
       
       for index, aluno in enumerate(alunos, start=1):
           
           print(f"Aluno {index} | Nome: {aluno['nome']}, Email: {aluno['email']}, Curso: {aluno['curso']}")

       print(f"\n")

       input("Voltar para Menu! (Aperte qualquer tecla)")

        
Main()

