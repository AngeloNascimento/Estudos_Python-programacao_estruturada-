
    


main = input("selecine uma opçao: \n[1]-teste1 \n[2]-teste2 \n[3]-teste3 \n[4]-sair") 

main2 = 0

while main != "4":
    if main == "1":
        nomes = ["python", "ACCER", "java", "Anaconda", "avião"]
        procurando = input("digite uma inicial: ")
        for nome in nomes:
         if nome[0] == procurando.lower() or nome[0] == procurando.upper(): 
          print(nome)
        break
    elif main == "2":
        print("teste")
        break
    elif main == "3":
        print("teste2")
        break
    elif main == "4":
        print("fim do programa...")
        break