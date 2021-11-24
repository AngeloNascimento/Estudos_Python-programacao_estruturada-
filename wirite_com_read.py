arq = open("teste/teste2.txt","w")
texto = input("Digite um aluma coisa: ")
arq.write(texto)
arq.close()

arq2 = open("teste/teste2.txt","r")
texto2 = arq2.read()
arq2.close()
print(texto2)
