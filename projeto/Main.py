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

from app import Aluno
from app import Docente
from app import Instituicao
from app import Turma
from app import Turno
from app import Disciplina

aluno1 = Aluno("Maykon", 21, "18516803732")

aluno2 = Aluno("Pedro", 23, "99999999999")

aluno3 = Aluno("Carlos", 22, "99999999999")

aluno4 = Aluno("Luiz", 23, "99999999999")

aluno5 = Aluno("Felipe", 22, "99999999999")

docente1 = Docente("Antonio", 55, "99999999999")

docente2 = Docente("Antonio", 55, "99999999999")

turma1 = Turma(Disciplina.TI.value, docente1,Turno.MANHA.value,
                { "inicio": '07:50:00',"fim": "11:30:00" }, [aluno1, aluno2])

turma1.append_aluno(aluno3)

turma2 = Turma(Disciplina.ADMINISTRACAO.value, docente2,Turno.TARDE.value,
               { "inicio": '12:00:00',"fim": "16:30:00" }, [aluno4, aluno5])

instituicao = Instituicao("Estacio de Sa", [turma1, turma2])

print(docente1.get_nome())
print(docente1.get_idade())
print(docente1.get_id())
print(docente1.get_cpf())
print()

print(aluno1.get_nome())
print(aluno1.get_idade())
print(aluno1.get_id())
print(aluno1.get_cpf())
print()

print(aluno2.get_nome())
print(aluno2.get_idade())
print(aluno2.get_id())
print(aluno2.get_cpf())
print()

print(aluno3.get_nome())
print(aluno3.get_idade())
print(aluno3.get_id())
print(aluno3.get_cpf())
print()

print(turma1.get_id())
print(turma1.get_turno())
print("Inicio:\t" + turma1.get_horario()['inicio'])
print("Fim:\t" + turma1.get_horario()['fim'])
print(turma1.get_disciplina())
print(turma1.get_alunos())
print()

print(instituicao.get_id())
print(instituicao.get_nome())
print(instituicao.get_turmas())
print(instituicao.get_lista_alunos())
print()

for aluno in instituicao.get_lista_alunos():
    print(str(aluno.get_nome())  + " - " + str(aluno.get_idade()) +
    " - " + str(aluno.get_cpf()) + " - " + str(aluno.get_id()))
