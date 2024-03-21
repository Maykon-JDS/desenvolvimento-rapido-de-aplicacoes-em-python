'''Aula 02 - exemplo01a.py
função : Sistema de registro de notas de alunos - 
Instituição pequena (i)
Vantagens do RAD : Entregar o sistema através dos processos gerando
protótipos que serão gradativamente atualizados. O conjunto de dados
será menor do que o cenário (ii).
Desvantagens do RAD : Exige uma equipe de desenvolvimento bem qualificada
 o que neste cenário será viável pois o porte do sistema será pequeno em
relação ao cenário (ii).
Modelo de negócio : A instituição ministra aulas em turmas de alunos de
 algumas áreas : TI, Administração e Direito. Cada aluno deve ser
matriculado em uma turma de cada curso. As disciplinas serão ministradas
por poucos docentes em suas respectivas áreas.
'''

from projeto.app import *

aluno1 = Aluno("Maykon", 21, "18516803732")

aluno2 = Aluno("Pedro", 23, "99999999999")

aluno3 = Aluno("Carlos", 22, "99999999999")

aluno4 = Aluno("Luiz", 23, "99999999999")

aluno5 = Aluno("Felipe", 22, "99999999999")

docente1 = Docente("Antonio", 55, "99999999999")

docente2 = Docente("Antonio", 55, "99999999999")

turma1 = Turma(Disciplina.TI.value, docente1,Turno.Manha.value, { "inicio": '07:50:00',"fim": "11:30:00" }, [aluno1, aluno2])

turma1.appendAluno(aluno3)

turma2 = Turma(Disciplina.Administracao.value, docente2,Turno.Tarde.value, { "inicio": '12:00:00',"fim": "16:30:00" }, [aluno4, aluno5])

instituicao = Instituicao("Estacio de Sa", [turma1, turma2])

print(docente1.getNome())
print(docente1.getIdade())
print(docente1.getId())
print(docente1.getCpf())
print()

print(aluno1.getNome())
print(aluno1.getIdade())
print(aluno1.getId())
print(aluno1.getCpf())
print()

print(aluno2.getNome())
print(aluno2.getIdade())
print(aluno2.getId())
print(aluno2.getCpf())
print()

print(aluno3.getNome())
print(aluno3.getIdade())
print(aluno3.getId())
print(aluno3.getCpf())
print()

print(turma1.getId())
print(turma1.getTurno())
print("Inicio:\t" + turma1.getHorario()['inicio'])
print("Fim:\t" + turma1.getHorario()['fim'])
print(turma1.getDisciplina())
print(turma1.getAlunos())
print()

print(instituicao.getId())
print(instituicao.getNome())
print(instituicao.getTurmas())
print(instituicao.getListaAlunos())
print()

for aluno in instituicao.getListaAlunos(): 
    print(str(aluno.getNome())  + " - " + str(aluno.getIdade()) + " - " + str(aluno.getCpf()) + " - " + str(aluno.getId()))


