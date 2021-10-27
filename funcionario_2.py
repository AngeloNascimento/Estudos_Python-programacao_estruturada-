funcs = []
for _ in range(3):
    nome = input("nome: ")
    cargo = input("cargo: ")
    salario = float(input("Salario: "))
    funcionario = {
        "nome":nome,
        "cargo":cargo,
        "salario":salario
    }
    funcs.append(funcionario)
    for func in funcs:   

     print("%s - %s recebe = %.2f" % (func["cargo"], func["nome"], func["salario"]))
