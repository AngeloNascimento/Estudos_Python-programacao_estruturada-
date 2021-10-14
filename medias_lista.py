notas = []
soma = 0
while True:
    nota= float(input("adicione a nota ou -1 para sair: "))
    if nota == -1:
      break
    notas.append(nota)
for nota in notas:
    soma += nota
    media = soma / 2
print(notas)
print("media do aluno é: %s" % media)
if media >= 7:
    print("aprovado")
elif media < 7:
    print("reprovado")