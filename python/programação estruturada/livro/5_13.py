divida = int(input("Divida: "))
taxa = int(input("Taxa de juros: "))
paga = int(input("pagamento mensal: "))
mes = 1
if (divida * (taxa/100) >paga):
    print("Sua divida não sera paga pois, os juros são maiores do que o pagamento mensal")
else:
    saldo = divida
    juros_pag = 0
while saldo >= paga:
    juros = saldo * taxa/100
    saldo = saldo - juros_pag
    juros_pag = juros_pag + juros
    print("Saldo da divida no mês %d e de R$ %d" % (mes, saldo))
    mes= mes + 1
    print("Para pagar uma divida de de R$ %d, a %d de juros "%(divida, taxa))
    print("Você precisará de %d meses, pagando R$ %d de juros" % (mes-1, juros_pag))
    print("No ultimo mes, voce teria que pagar R$ %d" % saldo)
