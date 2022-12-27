nomes  = ["creitu", "dougras", "china"]
for nome in nomes [::2]:
    print(nome)
    nomes [0] = nomes[2]
    print(nomes)
