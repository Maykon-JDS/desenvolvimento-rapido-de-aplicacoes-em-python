arquivo = "/workspaces/projeto_rad/exercicios/aula03/exercicio01/arquivo.txt"

def escreverArquivo(texto: str, arquivo: str):
    
    arquivoAberto = open(arquivo, "a")

    arquivoAberto.write(f"{texto}; ")

def loop(arquivo: str):

    for i in range(0,100):
    
        escreverArquivo(str(i+1), arquivo)

loop(arquivo)

