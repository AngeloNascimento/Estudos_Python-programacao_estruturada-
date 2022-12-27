ultimo = 10 
fila = list(range(1, ultimo + 1))
while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print("Digite F para adcionar um cliente ao fim da fila,")
    print("ou A para relizar o atendimento, S para sair")
    operacao = input("Operaçao(F, A ou S): ")
    if operacao == "A"  :
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f"Cliente {atendido} atendido")
        else:
            print("Fila Vazia! Ninguem para atender")
    elif operacao == "F" :
        ultimo += 1 #incrementa o ticket do novo cliente
        fila.append(ultimo)
    elif operacao == "S":
        print("Operação finalizada!")
        break
    else:
        print("Operação Invalida! Digite apenas F, A ou S!")