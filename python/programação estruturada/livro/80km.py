vel = float(input("digite a velocidade do carro: "))
multa = vel + 5
if vel > 80 :
   print("seu carro foi multado")
   print("valor da multa R$%.2f" % multa)

if vel <= 80:
    print("velocidade normal")