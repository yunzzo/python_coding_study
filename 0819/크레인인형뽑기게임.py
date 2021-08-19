board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [
    0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]


def solution(board, moves):
    answer = 0
    basket = []
    board = list(map(list, zip(*board)))
    for move in moves:
        for i in range(len(board)):
            if board[move-1][i] != 0:
                basket.append(board[move-1][i])
                board[move-1][i] = 0
                break

        if len(basket) >= 2:
            for k in range(1, len(basket)):
                if basket[k-1] == basket[k]:
                    del basket[k-1]
                    del basket[k-1]
                    answer += 2
    return answer


print(solution(board, moves))
