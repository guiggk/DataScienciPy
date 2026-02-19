notasTurma = ["joao",8,9,10,"maria",6.5,7.5,8,"guilherme",4,5,6]
nomes = []
notasJuntas= []

for i in range(len(notasTurma)):
    if i % 4 == 0:
        nomes.append(notasTurma[i])
    else:
        notasJuntas.append(notasTurma[i])

print(nomes)
print(notasJuntas)


notas = []

for i in range(0,len(notasJuntas),3):
    notas.append([notasJuntas[i],notasJuntas[i+1],notasJuntas[i+2]])

print(notas)



