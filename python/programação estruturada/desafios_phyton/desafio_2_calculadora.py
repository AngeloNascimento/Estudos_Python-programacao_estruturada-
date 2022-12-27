while True:
   menu = input("escolha uma opção: \n[1]-soma \n[2]-subtração \n[3]-multiplicação \n[4]-divisão")
   if menu.isdigit()==True:   
    if menu > "5" or menu < "1":
      print("Opção invalida! Escolha somente as opçoes no menu.") 
    elif menu.isdigit() == False:
      print("Opçao invalida! Digite somente opções numericas!")

   if menu == "1":
       numeros = []
       
       while True:
         numeros = []  
         num = input("Digite o numero ou = para somar: ")
         if num != "=":
          continue
         elif num =="=":
          num2 = float(num)  
          numeros.append(num2)   
          soma = sum(numeros)   
          print(soma)
          break
         
         
           
        
          



        
          
        

        
        


