#menu
print("Tabuada Interativa")
operacao = input("[1]-Soma \n[2]-subtração \n[3]-multiplicação \n[4]-divisão \nSelecione uma operaçâo: ")
#tabuada de adição
if operacao == "1":
    num = int(input("Digite o numero que deseja saber a tabuada adição: "))
    soma = 1
    while soma <= 10:
        print(f"{num} + {soma} = %d"%(num + soma))
        soma = soma + 1
#tabuada de subtração
if operacao == "2":
    num = int(input("Digite o numero que deseja saber a tabuada de subtração: "))
    sub = 1
    if num < 10:
     while sub <= 10:
        print(f"{sub} - {num} = %d"%(sub - num))
        sub = sub + 1
    elif num >= 10:
        while sub <= 10:
          print(f"{sub} - {num} = %d"%(num - sub))
          sub = sub + 1
#tabuada de multiplicação
if operacao == "3":
    num = int(input("Digite o numero que deseja saber a tabuada de multiplicação: "))
    mult = 1
    while mult <= 10:
        print(f"{num} x {mult} = %d"%(num * mult))
        mult = mult + 1
#tabuada de divisão
if operacao == "4":
  num = int(input("Digite o numero que deseja saber a tabuada de multiplicação: "))
  div = 1
  while div <= 10:
        print(f"{num} / {div} = %d"%(num / div))
        div = div + 1
   
            
    