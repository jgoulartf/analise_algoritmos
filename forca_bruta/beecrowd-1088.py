# Bubble sort
def swapValue(P):
    swap = False
    for i in range(len(P) - 1):
        if P[i] > P[i + 1] and not swap:
            P[i], P[i + 1] = P[i + 1], P[i]
            swap = True
    return P


def jogo(n, P):
    # Jogador fica True quando está em sua vez de jogar, se finalizar em true, ele é o vencedor
    marcelo = False
    carlos = False

    mov = True
    ctrl = 0

    if P == sorted(P):
        mov = False
        print("Carlos")

    # Laço principal do jogo
    while mov:

        # Marcelo jogando
        if ctrl == 0 and mov:
            P = swapValue(P)
            ctrl = 1

            # Se ordenado, marcelo vence
            if P == sorted(P):
                print("Marcelo")
                mov = False

        # Carlos jogando
        if ctrl == 1 and mov:
            P = swapValue(P)
            ctrl = 0

            # Se ordenado, carlos vence
            if P == sorted(P):
                print("Carlos")
                mov = False


entrada = input()

# entrada = """5 1 5 3 4 2 5 5 1 3 4 2 5 1 2 3 4 5 6 3 5 2 1 4 6 5 5 4 3 2 1 6 6 5 4 3 2 1 0"""

P = []
P.append(entrada)  # Colocando entrada em uma lista
P = P[0].split()  # Transformando lista de ca

# Laço principal para ler entrada e separar jogos ate o zero
for i in range(0, len(entrada)):

    P_Atual = []  # Lista do jogo atual

    # Verifica se lista está vazia
    if (len(P) > 0):
        n = int(P.pop(0))

    # Laço interno para construir e executar cada jogo
    for i in range(0, n):

        # Verifica se lista está vazia
        if (len(P) > 0):
            valor = int(P.pop(0))

        P_Atual.append(valor)  # Adiciona e constroi jogo atuali

    # Se n for diferente de zero, executa rodada do jogo, quando zero o jogo para
    if n > 0:
        jogo(n, P_Atual)
