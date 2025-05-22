matriz = []
maior_nota = None
matricula_maior = None

print("Digite as informações dos alunos:")

for i in range(5):
    print(f"\nAluno {i+1}:")
    matricula = int(input("Número de matricula: "))
    media_provas = float(input("Média das provas: ").replace(",","."))
    media_trabalhos = float(input("Média dos trabalhos: ").replace(",","."))

    nota_final = media_provas + media_trabalhos

    matriz.append([matricula, media_provas, media_trabalhos, nota_final])

    if (maior_nota is None) or nota_final > maior_nota:
        maior_nota = nota_final
        matricula_maior = matricula

print("\nMatriz com dados dos alunos (matrícula, provas, trabalhos, nota final): ")
for aluno in matriz:
    print(aluno)

print(f"\nA maior nota final foi {maior_nota}, do aluno com matrícula {matricula_maior}")