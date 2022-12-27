#tabela = {"Alface": 0.45,
#          "batata": 1.20,
#          "Tomate": 2.30,
#          "Feijão": 1.50}
#print(tabela["Tomate"])
#print(tabela)
#tabela["Tomate"]=2.50
#print(tabela["Tomate"])
#tabela["Cebola"]=1.20
#print(tabela)

#exibibir preço de um produto
#tabela = {"Alface": 0.45,
#          "Batata": 1.20,
#          "Tomate": 2.30,
#          "Feijão": 1.50}
#while True:
#    produto = input("Digite o nome do produto, FIM para terminar: ")
#    if produto == "fim":
#        print("obrigado pela preferencia!")
#        break
#    if produto in tabela:
#        print(f"Preço {tabela[produto]:5.2f}")
#    else:
#        print("produto não encontrado!")
        

#Apagando uma chave
tabela = {"Alface": 0.45,
          "Batata": 1.20,
          "Tomate": 2.30,
          "Feijão": 1.50}
print(tabela)          
del tabela["Tomate"]
print(tabela)