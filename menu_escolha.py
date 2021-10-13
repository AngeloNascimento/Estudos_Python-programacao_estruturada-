#adição de elemntos
nome = ["nome1", "nome2", "nome3", "nome4","nome5"]
opcao= int(input("[1]Adicionar \n[2]Remover:\n"))
if opcao == 1:
    for nomes in range(len(nome)):
      nomes = input("insira um nome:")
      nome.append(nomes)
    print(nome)
#remover elemento
elif opcao == 2:
 delt = int(input("insira um indece que queira deletar: "))
nome.pop(delt)
print(nome)
