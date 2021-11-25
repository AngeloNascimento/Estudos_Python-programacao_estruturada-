arq = open("teste/wirite2.txt","w")
texto = input("insira alguma coisa")
arq.write(texto)
arq.close()

arq2 = open("teste/wirite2.txt","w") #adicionar elementos um atras do outro
