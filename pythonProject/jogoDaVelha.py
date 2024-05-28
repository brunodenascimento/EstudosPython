def print_board(tabuleiro):
    print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
    print("--+---+--")
    print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
    print("--+---+--")
    print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")


def check_win(tabuleiro):
    condicoes_vitoria = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                         (0, 3, 6), (1, 4, 7), (2, 5, 8),
                         (0, 4, 8), (2, 4, 6)]
    for condicao in condicoes_vitoria:
        if tabuleiro[condicao[0]] == tabuleiro[condicao[1]] == tabuleiro[condicao[2]] != " ":
            return True
    return False


def check_tie(tabuleiro):
    return " " not in tabuleiro


def main():
    tabuleiro = [" "] * 9
    jogador_atual = "X"

    while True:
        print_board(tabuleiro)
        movimento = int(input(f"Jogador {jogador_atual}, escolha uma posição (1-9): ")) - 1

        if movimento not in range(9) or tabuleiro[movimento] != " ":
            print("Posição inválida! Tente novamente.")
            continue

        tabuleiro[movimento] = jogador_atual

        if check_win(tabuleiro):
            print_board(tabuleiro)
            print(f"Parabéns! Jogador {jogador_atual} venceu!")
            break

        if check_tie(tabuleiro):
            print_board(tabuleiro)
            print("Empate!")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"


if __name__ == "__main__":
    main()
