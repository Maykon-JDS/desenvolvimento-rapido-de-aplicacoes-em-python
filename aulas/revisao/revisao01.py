i = 10

pi = 3.141592

mensagem = "hey ho lets go"

print("isto é uma mensagem na tela")

# minha_variavel = input("digite algo")
                       
# meu_inteiro = int(input("digite um inteiro"))

print(mensagem)

a = 10

b = 15

print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)
print(a <= b and a < b)
print(a <= b or a >= b)
print(not a == b)

media = 8

if(media  >= 7):
    
    print("passou direto")       

elif(media < 7 and media >= 5):

    print("passou com prova final")    

else:
    
    print("recuperação")      

i = 0           

while(i < 10):
    
    print(i)      

    i += 1

while(i < 10):
    
    print(i)      

    i += 1

    if(i == 5):

        break

for x in range(10):

    print(x)


notas = [9.5, 4.0, 10]

for nota in notas:
    
    print(nota) 

print(notas[0])

print(notas[1])

print(notas[2])

print(4.0 in notas)

notas.append(65565)

print(notas)

notas.insert(4, 1000)

print(notas)

notas.pop()

print(notas)

notas.remove(4)

print(notas)

notas.sort()

print(notas)

notas.reverse()

print(notas)

notas.count(4)

print(sum(notas))

print(len(notas))