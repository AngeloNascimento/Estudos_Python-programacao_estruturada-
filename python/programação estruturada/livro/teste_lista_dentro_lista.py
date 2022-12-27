#L = ["maças", "peras", "kiwis"]
#for s in L:
#    for letra in s:
#        print(letra)

#lista de compras vazia.
compras = []
while True:
    produto = input("produto: ")
    if produto == "fim":
        break
    quantidade = float(input("Quantidade: "))
    preco = float(input("Preço: "))
    compras.append([produto, quantidade, preco])
soma = 0.0
for e in compras:
    print(f"{e[0]:20s} x {e[1]:5.3f} {e[2]:5.2f} {e[1] * e[2]:6.2f}")
    soma += e[1] * e[2]
print(f"Total: R${soma:7.2f}")