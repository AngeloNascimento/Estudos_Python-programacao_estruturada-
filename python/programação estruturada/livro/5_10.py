quest = 1
pont = 0
while quest <= 3:
    resp = input("resposta da questão %d: " % quest)
    if quest == 1 and (resp == "b" or resp =="B"):
        pont = pont + 1
    if quest == 2 and (resp == "a" or resp =="A"):
        pont = pont + 1
    if quest == 3 and (resp == "c" or resp =="C"):
        pont = pont + 1
    quest += 1
    print("O aluno fez %d ponto(s)" % pont)