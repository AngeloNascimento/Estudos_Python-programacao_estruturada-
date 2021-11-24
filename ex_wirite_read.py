arq2 = open("teste/teste2.txt","r")
texto2 = arq2.read()
arq2.close()
print(texto2)

#
arq = open("teste/wirite.txt","w")
texto = texto2
arq.write(texto)
arq.close()


