notas = []
while True:
    nota= float(input("adicione a nota ou -1 para sair: "))
    if nota == -1:
      break
    notas.append(nota)
print(notas)
