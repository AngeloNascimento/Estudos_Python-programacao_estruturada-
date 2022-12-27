from tkinter import *
dic=Tk()
dic.title("teste")

dic.configure(dic, text="teste", bg="#106", foregrounde="#000")


dic={}
for letra in "paralelepipedo":
    if letra in dic:
        dic[letra] = dic[letra] + 1
    else:
        dic[letra] = 1
print(dic)
dic.mainloop()