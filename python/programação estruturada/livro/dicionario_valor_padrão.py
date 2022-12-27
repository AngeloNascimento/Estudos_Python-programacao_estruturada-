dic={}
for letra in "paralelepipedo":
    if letra in dic:
        dic[letra] = dic[letra] + 1
    else:
        dic[letra] = 1
print(dic)