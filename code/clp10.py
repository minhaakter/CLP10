def solve():
    N = int(input())
    board = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        if i % 2 == 0:
            board[i][0] = 1
        elif i == N - 1:
            board[i][N - 1] = 1
        else:
            board[i][2] = 1

    for row in board:
        print(' '.join(map(str, row)))


solve()
