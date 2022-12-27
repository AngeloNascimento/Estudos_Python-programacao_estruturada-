dep = int(input("Digite valor de deposito: "))
juros = int(input("Digite taxa de juros: "))
depMS = int(input("Digite valor de deposito: "))
mes = 1
saldo = dep
while mes <= 24:
   saldo = saldo +(saldo*(juros/100)+depMS)
   print("saldo do mes %d é de R$ %.2f" %(mes, saldo))
   mes = mes + 1
   print("ganho obtido com os juros e de: %d"%(saldo-dep))