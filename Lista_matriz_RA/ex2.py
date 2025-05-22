matriz = []
maior = 0
linha_maior = 0
coluna_maior = 0

for i in range(4):
    linha = []
    for j in range(4):
        numero = int(input(f"Digite a {i+1}ª linha da matriz (um número por vez): "))
        linha.append(numero)

        if numero > maior:
            maior = numero
            linha_maior = i
            coluna_maior = j
    matriz.append(linha)

for linha in matriz:
    print(linha)

print(f"\nO seu maior elemento é {maior} e está localizado na linha {linha_maior}, coluna {coluna_maior}")