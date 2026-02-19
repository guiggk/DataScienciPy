notas = {"1° trimestre":8.5, "2° trimestre":6.5, "3° trimestre":4}

soma = 0

for nota in notas.values():
    soma +=nota

print(soma)


somatorio = sum(notas.values())
print(somatorio)


