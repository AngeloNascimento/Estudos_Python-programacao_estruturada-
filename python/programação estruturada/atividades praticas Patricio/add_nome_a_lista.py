nome = ["nome1", "nome2", "nome3", "nome4","nome5"]
nomes = 0
for nomes in range(len(nome)):
    nomes = input("insira um nome:")
    nome.append(nomes)
    print(nome)
delt = int(input("insira um indece que queira deletar: "))
nome.pop(delt)
print(nome)
