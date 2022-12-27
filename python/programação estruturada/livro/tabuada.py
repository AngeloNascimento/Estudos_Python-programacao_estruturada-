n = int(input("Tabuada de: "))
x = int(input("digite o multiplicador: "))
while x <= 10:
    result = n * x
    print("%d * %d = %d"%(n,x,result))
    x = x + 1