print('##### Desafio: “Controle de Pontos do Jogador” 🎮 #####')

""" 
Você vai criar um programa de terminal que simula a pontuação de um jogador ao longo 
de várias fases de um jogo.

Regras do desafio
O programa deve perguntar:
nome do jogador
quantas fases ele jogou (número inteiro)
Para cada fase (usando for in):
Pergunte quantos pontos o jogador fez naquela fase (inteiro).
Se os pontos forem:
menor que 0 → considere como trapaça e zere os pontos dessa fase.
entre 0 e 99 → fase “normal”
100 ou mais → fase “bonus”
O programa deve calcular:
total de pontos
média de pontos por fase
quantas fases foram “bonus”
quantas fases foram “normal”
quantas fases tiveram trapaça (pontos negativos)
No final, classifique o jogador com if/else:
média >= 120 → LENDÁRIO
média >= 80 → VETERANO
média >= 40 → APRENDIZ
senão → INICIANTE
Saída final esperada (exemplo)
Nome
Total de fases
Total de pontos
Média
Contagem de normal/bonus/trapaça
Rank final 
"""

nome_jogador = input('Digite seu nome: ')
fases_jogadas = int(input('número de fases jogadas: '))
total_pontos = 0
cont_bonus = 0
cont_normal = 0
cont_trapaca = 0

# ===== Loop pelas fases =====
for fase in range(1, fases_jogadas + 1):
    pontos_str = input(f"Pontos na fase {fase}: ")
    pontos = int(pontos_str)

    # Se for negativo, zera e conta como trapaça
    if pontos < 0:
        cont_trapaca += 1
        pontos = 0

    # Classifica a fase
    if pontos >= 100:
        cont_bonus += 1
    else:
        cont_normal += 1

    # Soma no total
    total_pontos += pontos

# ===== Cálculos finais =====
media = total_pontos / fases_jogadas

# ===== Rank do jogador =====
if media >= 120:
    rank = "LENDÁRIO"
elif media >= 80:
    rank = "VETERANO"
elif media >= 40:
    rank = "APRENDIZ"
else:
    rank = "INICIANTE"

# ===== Saída =====
print("\n===== RESULTADO FINAL =====")
print(f"Jogador: {nome_jogador}")
print(f"Fases jogadas: {fases_jogadas}")
print(f"Total de pontos: {total_pontos}")
print(f"Média por fase: {media:.2f}")
print(f"Fases BONUS (>=100): {cont_bonus}")
print(f"Fases NORMAL (<100): {cont_normal}")
print(f"Fases com TRAPAÇA (negativo): {cont_trapaca}")
print(f"RANK: {rank}")