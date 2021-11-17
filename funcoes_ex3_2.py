def triangulo_equilatero(lado1, lado2, lado3):
    if lado1 == lado2 and lado1 == lado3 :
        return True
    else:
        return False

def triangulo_isocele(lado1, lado2, lado3):
    if lado1 == lado2 and lado1 != lado3 :
        return True
    else:
        return False

def triangulo_escaleno(lado1, lado2, lado3):
    if lado1 != lado2 and lado1 !=lado3 and lado2 != lado3:
        return True
    else: 
        return False



lado1 = int(input("Digite lado 1 : "))
lado2 = int(input("Digite lado 2 : "))
lado3 = int(input("Digite lado 3 : "))

resultado_isoceles = triangulo_isocele(lado1, lado2, lado3)
resultado_escaleno = triangulo_escaleno(lado1, lado2, lado3)
resultado_equilatero = triangulo_equilatero(lado1, lado2, lado3)

if resultado_equilatero == True:
 print(f'triangulo isoceles')
elif resultado_escaleno == True:
 print(f'triangulo escaleno ')
elif resultado_equilatero:
 print(f'triangulo equilatero ')