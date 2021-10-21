
    

nomes = ["python", "ACCER", "java", "Anaconda", "avião"]
main = input("selecine uma opçao: \n[1]-teste1 \n[2]-teste2 \n[3]-teste3 \n[4]-sair") 

main2 = 0

while main != "4":
    #1
    if main == "1":
        while True:
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
      inteiros = [1,2,3,4,5,6,7,8,9,10]
      for num in inteiros:
       if num > 5:
        print(num)
      break

    #3  
    elif main == "3":
        print("teste2")
        break
    #4
    elif main == "4":
       print("fim do programa...")
       break
  
    else:
        print("opção invalida!")