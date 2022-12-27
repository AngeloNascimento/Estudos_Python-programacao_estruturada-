nomes = ["python", "ACCER", "java", "Anaconda", "avião"]
def main(lista):
  opacao = 1
  for escolha in lista: 
    print(f'{opacao} - {escolha}')
    opacao += 1
  selecao = int("Escolha uma opçao")


   main(['opaçao1','opçao2', 'opçao3'])

while True:
    #1
    if main == "1":
        procurando = input("digite uma inicial ou 0 para voltar: ")
        if procurando != "0":
            for nome in nomes:
             if nome[0] == procurando.lower() or nome[0] == procurando.upper(): 
              print(nome)
        elif procurando == "0":
            break 
        
        main = input("selecine uma opçao: \n[1]-teste1 \n[2]-teste2 \n[3]-teste3 \n[4]-sair") 
       
         
    #2
    elif main == "2":
         while True:
          inteiros = [1,2,3,4,5,6,7,8,9,10]
          for num in inteiros:
           if num > 5:
            print(num)
          break
 
         main = input("selecine uma opçao: \n[1]-teste1 \n[2]-teste2 \n[3]-teste3 \n[4]-sair") 

    #3  
    elif main == "3":
        while True:
          nomes  = ["creitu", "dougras", "china"]
          for nome in nomes [::2]:
            print(nome)
            nomes [0] = nomes[2]
            print(nomes)
          break
        main = input("selecine uma opçao: \n[1]-teste1 \n[2]-teste2 \n[3]-teste3 \n[4]-sair") 
   
    #4
    elif main == "4":
         print("fim do programa...")
          
    else:
        print("opção invalida!")
        break