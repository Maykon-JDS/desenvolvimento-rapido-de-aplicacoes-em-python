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

from Aluno import Aluno

from Disciplina import Disciplina

from Docente import Docente

from Instituicao import Instituicao

from Turma import Turma

from Turno import Turno

aluno1 = Aluno("Maykon", 21, "18516803732")
aluno2 = Aluno("Pedro", 23, "99999999999")

turma = Turma(Disciplina.TI.value, Turno.Manha.value, { "inicio": '07:50:00',"fim": "11:30:00" }, [aluno1, aluno2])

print(aluno1.getNome())
print(aluno1.getIdade())
print(aluno1.getId())
print(aluno1.getCpf())
print(aluno2.getNome())
print(aluno2.getIdade())
print(aluno2.getId())
print(aluno2.getCpf())
print(turma.getId())
print(turma.getTurno())
print(turma.getHorario())
print(turma.getDisciplina())
print(turma.getAlunos())
print()

