#desafio
#num1 = int(input("digite primeiro numero: "))
#num2 = int(input("digite segundo numero: "))
#s = num1 + num2
#print(f'a soma entre {num1} e {num2} = {s}')

num = input('digite alguma coisa: ')

if num.isnumeric:
    print(type(num))
elif num.isalpha:
    print(type(num))
elif num.isalnum:
    print(type(num))    

 