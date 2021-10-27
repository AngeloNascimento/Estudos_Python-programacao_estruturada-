funcs = [
    {"nome": "joao", "cargo": "dev", "sal" : 3125},
    {"nome": "maria", "cargo": "gerente", "sal" : 5125},
    {"nome": "paulo", "cargo": "ceo", "sal" : 10126}
]

for func in funcs:
    print("%s - %s recebe = %.2f" % (func["cargo"], func["nome"], func["sal"]))