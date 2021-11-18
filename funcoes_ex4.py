produto = input("digite o produto: ")
valor = int(input("digite o valor: "))
def desconto(valor):
    desconto_total = valor * 0.15
    desconto_t = (valor - desconto_total)
    return desconto_t
desconto_t = desconto(valor)
print(f'o valor do produto {produto} com 15% desconto = {desconto_t}')
    

    
    