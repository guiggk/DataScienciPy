
def media():
    calculo = 2+5
    print(calculo)

media()

def media2(n1,n2):
    calculo = (n1+n2)/2
    return calculo

media2(5,10)

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))


qualitativo = lambda x: x+0.5

print(qualitativo(n1))


notas = [8.5, 6.5, 4,3,6.5]

qualitativo2 = 0.5

notasAtualizadas = map(lambda x: x + qualitativo2, notas)
print(list(notasAtualizadas))

