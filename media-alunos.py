print("Insira o nome do aluno: ")
nomeDoUsuário = input()
print("Insira a nota 1: ")
nota1 = float(input())
print("Insira a nota 2: ")
nota2 = float(input())
print("Insira a nota 3: ")
nota3 = float(input())
media = (nota1+nota2+nota3)/3

print("Nome do aluno: ", nomeDoUsuário)
print("Média do aluno: ", media)

if(media>=60):
    print("Aluno APROVADO")
else:
    print("Aluno REPROVADO")
