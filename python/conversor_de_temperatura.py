from time import sleep

#funçoes
def fahrenheitC(celsius):
    converterc = (celsius *9/5)+32
    print(f"Sua temperatura em Fahrenheit é: {converterc:.2f} °F")
    
def fahrenheitK(kelvin):
    converterk = (kelvin - 273.15) * 9/5 + 32 
    print(f"Sua temperatura em Fahrenheit é: {converterk:.2f} °F")

def kelvinc(celsius):
    converterc = celsius + 273.15
    print(f"Sua temperatura em Kelvin é: {converterc:.2f}°K")

def kelvinf(fahrenheit):
    converterf = (fahrenheit - 32)* 5/9+273.15
    print(f"Sua temperatura em Kelvin é: {converterf:.2f}°K")

def celsiusf(fahrenheit):
    converterf =(fahrenheit-32) * 5/9
    print(f"Sua temperatura em Celsius é: {converterf:.2f}°C") 

def celsiusk(kelvin):
    converterk = kelvin - 273.15
    print(f"Sua temperatura em Celsius é: {converterk:.2f}°C")

def titulo(txt):
    print("-"*30)
    print(txt.center(30))
    print("-"*30)


#Conversor
while True:
    sleep(2)
    try: 
        titulo("MENU PRINCIPAL")
        print("""selecine uma opçao: 
[1]-Celsius 
[2]-Kelvin
[3]-Fahrenheit 
[4]-sair""")
        opcao = int(input("Escolha uma opçao: "))     
    except (ValueError, TypeError):
        print("Digite somente as opçoes do menu!")
        continue
    
    if opcao == 1:
        titulo("Conversao Celsius")
        try:
            converter1 = float(input("Digite a temperatura em °C: "))
            fahrenheitC(converter1)
            kelvinc(converter1)
        except (ValueError, TypeError):
            print("Digite somente numeros!")                      
            continue
         

    elif opcao == 2:
        titulo("Conversão Kelvin")
        try:
            converter2 = float(input("Digite a temperatura em °K: "))
            fahrenheitK(converter2)
            celsiusk(converter2)
        except (ValueError, TypeError):
            print("Digite somente numeros!")
            continue

    elif opcao == 3:
        titulo("Conversão Fahrenheit")
        try:
            converter3 = float(input("Digite a temperatura em °F: "))
            celsiusf(converter3)
            kelvinf(converter3)
        except (ValueError, TypeError):
            print("Digite somente numeros!")
            continue
    
    elif opcao == 4:
        print("Finalizando programa...")
        sleep(2)
        break
   
    elif opcao > 4 or opcao < 1 :
        print("Digite somente as opçoes do menu!")
        continue

    
    
   
    
    
    
    







    





