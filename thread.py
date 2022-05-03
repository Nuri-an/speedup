import threading
import random

showNone = []


def printMatrix(matrix):
    print("\nMatriz aleatoria:")
    for line in matrix:
        for el in line:
            print(el, end="")
            print("\t", end="")
        print("\n")


def matrixPlays(index, matrix):
    plays = []  # BAIXO,  ESQUERDA, DIREITA, CIMA, NONE

    i = 0
    while i < 4:
        j = 0
        while j < 4:
            # play ESQUERDA
            if (
                j != 0
                and matrix[i][j] != 0
                and (matrix[i][j - 1] == 0 or matrix[i][j - 1] == matrix[i][j])
            ):
                try:
                    plays.index("ESQUERDA")
                except:
                    plays.append("ESQUERDA")

            # play DIREITA
            if (
                j < 3
                and matrix[i][j] != 0
                and (matrix[i][j + 1] == 0 or matrix[i][j + 1] == matrix[i][j])
            ):
                try:
                    plays.index("DIREITA")
                except:
                    plays.append("DIREITA")

            # play BAIXO
            if (
                i != 3
                and matrix[i][j] != 0
                and (matrix[i + 1][j] == 0 or matrix[i + 1][j] == matrix[i][j])
            ):
                try:
                    plays.index("BAIXO")
                except:
                    plays.append("BAIXO")

            # play CIMA
            if (
                i != 0
                and matrix[i][j] != 0
                and (matrix[i - 1][j] == 0 or matrix[i - 1][j] == matrix[i][j])
            ):
                try:
                    plays.index("CIMA")
                except:
                    plays.append("CIMA")

            j += 1
        i += 1

    if len(plays) < 1:
        plays.append("NONE")
        showNone.append(1)

    print(
        "\n_______________________________\n\n(Matriz Thread: "
        + str(index + 1)
        + ")\n\nJogadas possiveis: ",
        end="",
    )

    for el in plays:
        print(el, end="")

        if el != "":
            print("; ", end="")


def createMatrix():
    line = []
    matrix = []

    while len(matrix) != 4:
        n = (random.randint(0, 32)) * 2
        line.append(n)

        if len(line) == 4:
            matrix.append(line)
            line = []

    return matrix


def execute():
    threads = []
    for i in range(6):
        matrix = createMatrix()
        # printMatrix(matrix)
        thread = threading.Thread(
            target=matrixPlays,
            args=(
                i,
                matrix,
            ),
        )
        threads.append(thread)
        thread.start()

    for i in threads:
        i.join()

    print(
        "\n_______________________________\n\nQuantidade de jogadas vazias: "
        + str(len(showNone))
        + "\n_______________________________\n"
    )


if __name__ == "__main__":
    execute()
