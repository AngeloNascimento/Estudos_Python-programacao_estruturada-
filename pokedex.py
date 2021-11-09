from time import sleep
pokedex = ["Bulbassauro", "Charmander", "Charizard", "Pikachu","Raichu"]
nomepok = 0

while True:
  
  main = input("Selecione uma opção \n[1]-Adicionar Pokemon \n[2]-Remover Pokemon \n[3]-Exibir Pokemon \n[4]-Buscar Pokemons \n[5]-Sair: ") 
  if main.isdigit()==True:#verifica se a opção esta entre 1 e 5.   
     if main > "5" or main < "1":
      print("Opção invalida! Escolha somente as opçoes no menu.")#caso a opção não esteja entre 1 e 5 imprime a menssagem e retorna ao menu. 
  elif main.isdigit() == False:#Faz a verificação se é numero ou letra.
    print("Opçao invalida! Digite somente opções numericas!")#caso seja letra imprime essa mensagem e retorna ao menu.
    sleep(2)
#Menu Adicionar pokemon

  if main == "1":
      while True:
          for nomepok in pokedex:
            nomepok = input("insira um nome ou 0 pra sair:")
            if nomepok == "0":
              break

            elif nomepok.isdigit() == True:
             print("Digite apenas nomes!")

            else: 
             pokedex.append(nomepok)# adiciona o nome da variavel nomepok
             print(pokedex)
            break
          if nomepok == "0" :#encerra o loop e pula para o menu principal           
             break
  
#Menu Remover Pokemon
  elif main == "2":
   while True:
        for ordem, pokemon in enumerate(pokedex):#faz a ordenação dos intens da lista
         print(f"[{ordem}]- {pokemon}")#exibe os a ordem e o nome dos intens da lista
        
        delt = input("insira um indice que queira deletar ou . pra sair: ")
        if delt.isdigit()== False:
          print("digite apenas numeros")
          break                   
        elif int(delt) > len(pokedex):
          print("opçao invalida, tente novamente!")
          break
        elif len(pokedex) == 0:
            print("Lista vazia!")
            break
           
        else:
           delete = int(delt)          
           pokedex.pop(delete)
           for ordem, pokemon in enumerate(pokedex):
            print(f"[{ordem}]- {pokemon}")
           break            
         
 #Menu listar Pokemon
  elif main == "3":
   quantidade = len(pokedex)
   print(f"Foram encontrados {quantidade} pokemons!")   
   x = 0
   while x < len(pokedex):
    print(pokedex[x])
    x += 1
    continue
  

#Menu mostra pokemon por letra
  elif main == "4":
       while True:
           procurando = input("inicial do nome que deseja ou . pra sair: ")#insere a inicial do nome que deseja
           if procurando.isdigit() == True:
             print("Digite somente letras")
             continue
           for nome in pokedex:#loop para verificar enqunato for verdadeira as iniciais imprimir a palavra
             if nome[0].lower().startswith(procurando) == True or nome[0].upper().startswith(procurando) == True:#faz a verificaçao das iniciais
              print(nome)#imprime as palavras com as iniciais
              continue                                     
           if procurando == ".":#Se o usuario digitar "." volta ao menu anterior
              break
      
#menu sair
  elif main == "5":#se o usuario digitar 5 encerra o programa
   print("Fechando pokedex...")
   sleep(2)
   break
     
 
    
