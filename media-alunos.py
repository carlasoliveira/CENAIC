print("Insira o nome do aluno: ")
nomeDoUsuário = input()

notas = [0,0,0] 

for contador in range(3):
    print("Insira a nota ", (contador+1), ": ")
    while True:
        notas[contador] = float(input())
        'print("Valor negativo. Insira uma nota válida!")'
        if(notas[contador]>0):
            break

media = (notas[0]+notas[1]+notas[2])/3

print("Nome do aluno: ", nomeDoUsuário)
print("Média do aluno: ", media)

if(media>=60):
    print("Aluno APROVADO")
else:
    print("Aluno REPROVADO")
