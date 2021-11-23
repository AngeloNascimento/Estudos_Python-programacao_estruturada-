arq = open("teste/wirite.txt","r")
texto = arq.read()
if texto.startswith("a"):
 arq.close()
 print(texto)
