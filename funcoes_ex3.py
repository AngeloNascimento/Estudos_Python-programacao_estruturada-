lado1 = int(input("Digite lado 1: "))
lado2 = int(input("Digite lado 2: "))
base = int(input("Digite base: "))
def triangulo(lado1, lado2, base):
    if lado1 == lado2 and lado1 != base:
        return True
    else:
        return False

resultado = triangulo(lado1, lado2, base)
print(resultado)
