from time import sleep

#Funçoes
def imposto1(salario):
    desconto = (salario)* 7.5 / 100
    liquido = salario - desconto
    print(f'Seu salario bruto: {salario: .2f}')
    print(f'Desconto de 7.5%: {desconto: .2f}\n')
    print(f'Seu salario liquido: {liquido: .2f}\n')

def imposto2(salario):
    desconto = (salario)* 15 / 100
    liquido = salario - desconto
    print(f'Seu salario bruto: {salario: .2f}')
    print(f'Desconto 15%: {desconto: .2f}\n')
    print(f'Seu salario liquido: {liquido: .2f}\n')

def imposto3(salario):
    desconto = (salario)* 22.5 / 100
    liquido = salario - desconto
    print(f'Seu salario bruto: {salario: .2f}')
    print(f'Desconto de 22.5%: {desconto: .2f}\n')
    print(f'Seu salario liquido: {liquido: .2f}\n')

def imposto4(salario):
    desconto = (salario)* 27.5 / 100
    liquido = salario - desconto
    print(f'Seu salario bruto: {salario: .2f}')
    print(f'Desconto de 27.5%: {desconto: .2f}\n')
    print(f'Seu salario liquido: {liquido: .2f}\n')
    

def titulo(txt):
    print("="*30)
    print(txt.center(30))
    print("="*30) 

while True:
    sleep(2)
    try:
        titulo("CALCULO IMPOSTO DE RENDA")
        print("""selecione uma opção:
[1]-Calcular IR
[2]-sair
        """)
        opcao = int(input("Digite a opção: "))

    except (ValueError, TypeError):
            print("Opção invalida!")
            continue
    
    if opcao == 1 :   
       salario = float(input("Digite Salario: "))
       if salario <= 1903.98 and salario >= 0:
             print("livre de imposto de renda!")
             continue

       elif salario >= 1903.99 and salario <= 2826.65:
             titulo("Imposto Calculado")
             imposto1(salario)
             continue
   
       elif salario >= 2826.66 and salario <= 3751.06:
            titulo("Imposto Calculado")
            imposto2(salario)
            continue
    
       elif salario >= 3751.07 and salario <= 4664.68:
            titulo("Imposto Calculado")
            imposto3(salario)
            continue
    
       elif salario >= 4664.69:
            titulo("Imposto Calculado")
            imposto4(salario)
            continue

       elif salario < 0:
            print("Valor Invalido!")
            continue
    
    elif opcao == 2:
        print("Saindo...")
        sleep(2)
        break  



