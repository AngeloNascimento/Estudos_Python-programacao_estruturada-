dep = int(input("Digite valor de deposito: "))
juros = int(input("Digite taxa de juros: "))
mes = 1
saldo = dep
while mes <= 24:
   saldo = saldo +(saldo*(juros/100))
   print("saldo do mes %d é de R$ %.2f" %(mes, saldo))
   mes = mes + 1