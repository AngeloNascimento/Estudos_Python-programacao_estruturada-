#função com print.
#def soma(a,b):
#    print(a+b)
#soma(2,9)

#função com return.
#def soma(a,b):
#    return a+b
#print(soma(1,2))

#função reutilizando funçoes e com if ou else.
#def epar(x):
#    return x % 2==0
#def par_ou_impar(x):
#    if epar(x):
#       return "par"
#    else:
#       return "impar"
#print(par_ou_impar(4))
#print(par_ou_impar(5))

######################################Exercicios funções#####################################
#ex8.1=maoir que ou menor que
#def mario_menor(a,b):
#    if a>b:
#        return a
#    else:
#        return b
#print(mario_menor(5,6))
#print(mario_menor(2,1))
#print(mario_menor(7,7))

#ex8.2=multiplos ou não

#def multiplo(a,b):
#    if a % b == 0:
#       return True
#    else:
#        return False
#print(multiplo(8,4))
#print(multiplo(7,3))
#print(multiplo(5,5))

#ex8.3=area do quadrado
#def area_quadrada(a):
#    area= a*a
#    return area
#print(area_quadrada(4))
#print(area_quadrada(9))

#ex8.4=Area do triangulo
#def area_triangulo(b,h):
#    area = (b*h)/2
#    return area
#print(area_triangulo(6, 9))
#print(area_triangulo(5, 8))

####################################################Exemplos#################################
#pesquisa em uma lista
#def pesquise(lista, valor):
#    for x, e in enumerate(lista):
#        if e == valor:
#            return x
#    return None
#L = [10, 20, 25, 30]
#print(pesquise(L, 25))
#print(pesquise(L, 27))

def soma(L):
    total = 0
    for e in L:
        total += e
    return total
def media(L):
    return soma(L) / len(L)
