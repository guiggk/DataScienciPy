import matplotlib.pyplot as plt
from random import choice

estudante2 = ["joao","guilherme","maria"]
notas = [10,6.5,4]

plt.bar(x = estudante2, height = notas)

estudantes = choice(estudante2)

