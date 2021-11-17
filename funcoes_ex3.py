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
print(f'triangulo isoceles = {resultado_isoceles}')
resultado_escaleno = triangulo_escaleno(lado1, lado2, lado3)
print(f'triangulo escaleno = {resultado_escaleno}')
resultado_equilatero = triangulo_equilatero(lado1, lado2, lado3)
print(f'triangulo equilatero = {resultado_equilatero}')