def desconto(valor):
    desconto_total = valor * 0.15
    desconto_t = (valor - desconto_total)
    return desconto_t


valor2 = [100, 200, 300]    
for desconto_tot in valor2:
    desc = desconto(desconto_tot)
    print(f'o valor do produto com 15% desconto = {desc}')
    

    
    