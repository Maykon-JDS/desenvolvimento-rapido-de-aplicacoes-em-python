import json
import os

class Aluno:

    def __init__(self,  nome: str, email: str, curso: str) -> None:
        """
        Inicializa um novo aluno com nome, email e curso.

        Parameters
        ----------
        nome : str
            O nome do aluno.
        email : str
            O email do aluno.
        curso : str
            O curso do aluno.
        """

        self._nome  = nome
        self._email = email
        self._curso = curso

    def getAluno(self) -> dict:

        """
        Retorna um dicionario com os dados do aluno.

        Returns
        -------
        dict
            Um dicionario com chaves 'nome', 'email' e 'curso'.
        """
        return dict(nome = self._nome, email = self._email, curso = self._curso)

    def __str__(self) -> str:

        """
        Retorna um dicionario com os dados do aluno.

        Returns
        -------
        dict
            Um dicionario com chaves 'nome', 'email' e 'curso'.
        """
        return str(self.getAluno())

class Arquivo:

    def __init__(self, arquivo: str) -> None:

        self._arquivo = arquivo

    def escreverArquivo(self, dados: dict) -> None:

        """
        Escreve os dados em um arquivo no formato JSON.

        Parameters
        ----------
        dados : dict
            Os dados a serem escritos no arquivo.

        Returns
        -------
        None
        """
        arquivoAberto = open(self._arquivo, "+tr")

        qtdLinhas = len(arquivoAberto.readlines())

        dadosJson = json.dumps(dados, indent=4)

        ajuste = ""

        if(qtdLinhas != 0):
            ajuste = ","


        arquivoAberto.write(f"{ajuste}{dadosJson}\n")

    def showArquivo(self) -> None:

        """
        Mostra o conteudo do arquivo.

        Returns
        -------
        None
        """
        print(self.getArquivo())

    def getArquivo(self) -> str:

        """
        Retorna o conteudo do arquivo.

        Returns
        -------
        str
            O conteudo do arquivo.
        """
        arquivoAberto = open(self._arquivo, "r")

        return arquivoAberto.read()


class Main():

    def __init__(self) -> None:

        self.arquivo = Arquivo("exercicios/aula03/exercicio02/arquivo.txt")

        self.loop()

    def loop(self) -> None:

        """
        Realiza um loop infinito para que o usuario possa realizar as ações de:
        - Cadastrar Aluno
        - Listar Aluno
        - Pesquisar Aluno
        - Encerrar Programa

        Returns
        -------
        None
        """
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
                    self.loopPesquisarAluno()
                case 4:
                    os.system('cls')
                    print("Programa finalizado!")
                    break
                case _:
                    print(f"\nValor \"{opcao}\" inválido!\n")

            os.system('cls')

    def cadastrarAluno(self):

        """
        Responsável por cadastrar um novo aluno no arquivo de texto.

        Pedirá para o usuário informar o nome, email e curso do novo aluno.
        Em seguida, criará um novo objeto do tipo Aluno e chamará o método
        escreverArquivo para adicionar as informações do novo aluno no
        arquivo de texto.

        Returns
        -------
        None
        """
        nomeAluno = input(f"Digite o nome do novo aluno: ")
        emailAluno = input(f"Digite o email do novo aluno: ")
        cursoAluno = input(f"Digite o curso do novo aluno: ")

        novoAluno = Aluno(nomeAluno, emailAluno, cursoAluno)

        self.arquivo.escreverArquivo(novoAluno.getAluno())

    def loopCadastarAluno(self):

        """
        Realiza um loop para que o usuario possa realizar o cadastro de
        vários alunos seguidos. O loop somente é encerrado quando o usuario
        digita 'n' como resposta.

        Returns
        -------
        None
        """
        resposta = 0

        while True:

            match resposta:
                case 0 | "s":
                    self.cadastrarAluno()
                case 'n':
                    break
                case _:
                    print(f"Valor {resposta} inválido!")

            resposta = input(f"Deseja cadastrar outro usuário? (s/n)\n")

    def showAlunos(self):

        """
        Mostra a lista de alunos cadastrados.

        A lista de alunos é carregada do arquivo de dados em formato JSON.
        Os dados são mostrados na tela em uma lista com o nome, email e curso
        de cada aluno.

        Após a lista ser mostrada, o programa aguarda a entrada do usuario,
        e logo em seguida, volta para o menu principal.

        Returns
        -------
        None
        """
        os.system('cls')

        alunosJson = str(f"{self.arquivo.getArquivo()}")

        alunos = json.loads(str(f"[{alunosJson}]"))

        print(f"\nLista de Alunos:\n")

        for index, aluno in enumerate(alunos, start=1):

            print(f"Aluno {index} | Nome: {aluno['nome']}, Email: {aluno['email']}, Curso: {aluno['curso']}")

        print(f"\n")

        input("Voltar para Menu! (Aperte qualquer tecla)")

        os.system('cls')

    def loopPesquisarAluno(self):

        """
        Realiza um loop para que o usuario possa realizar a pesquisa de
        vários alunos seguidos. O loop somente é encerrado quando o usuario
        digita 'n' como resposta.

        Returns
        -------
        None
        """

        resposta = 0

        while True:

            os.system('cls')

            match resposta:
                case 0 | "s":
                    campo = input(f"Qual campo deseja pesquisar? (nome, email ou curso)\n")
                    valor = input(f"Qual valor deseja pesquisar?\n")

                    alunosFiltrados = self.pesquisarAluno(campo, valor)

                    if alunosFiltrados:

                        for index, aluno in enumerate(alunosFiltrados, start=1):

                            print(f"\nAluno {index} | Nome: {aluno['nome']}, Email: {aluno['email']}, Curso: {aluno['curso']}\n")

                case 'n':
                    break

                case _:
                    print(f"Valor {resposta} inválido!")

            resposta = input(f"Deseja pesquisar novamente? (s/n)\n")


    def pesquisarAluno(self, campo, valor):

        alunosJson = str(f"{self.arquivo.getArquivo()}")

        alunos = json.loads(str(f"[{alunosJson}]"))

        match campo:
            case 'nome':
                resultados = [aluno for aluno in alunos if valor in aluno['nome']]
            case 'email':
                resultados = [aluno for aluno in alunos if valor in aluno['email']]
            case 'curso':
                resultados = [aluno for aluno in alunos if valor in aluno['curso']]
            case _:
                print(f"Campo {campo} inválido!")
                return False

        if resultados:
            return resultados
        else:
            print(f"Aluno com o {campo} '{valor}' não encontrado.")
            return False

Main()
