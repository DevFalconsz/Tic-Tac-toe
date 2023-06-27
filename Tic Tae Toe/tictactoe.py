# Jogo da Velha

board = [' ' for x in range(10)]

def insert_letter(letter, position):
    board[position] = letter

def space_is_free(position):
    return board[position] == ' '

def print_board(board):
    print("   |   |")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |")

def is_winner(board, letter):
    return ((board[1] == letter and board[2] == letter and board[3] == letter) or
            (board[4] == letter and board[5] == letter and board[6] == letter) or
            (board[7] == letter and board[8] == letter and board[9] == letter) or
            (board[1] == letter and board[4] == letter and board[7] == letter) or
            (board[2] == letter and board[5] == letter and board[8] == letter) or
            (board[3] == letter and board[6] == letter and board[9] == letter) or
            (board[1] == letter and board[5] == letter and board[9] == letter) or
            (board[3] == letter and board[5] == letter and board[7] == letter))

def player_move():
    run = True
    while run:
        move = input("Digite o número da posição que deseja jogar de 1 a 9: ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if space_is_free(move):
                    run = False
                    insert_letter('X', move)
                else:
                    print("Este espaço já está ocupado!")
            else:
                print("Digite um número entre 1 e 9!")
        except:
            print("Digite um número válido!")

def computer_move():
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = let
            if is_winner(board_copy, let):
                move = i
                return move

    corners_open = []
    for i in possible_moves:
        if i in [1,3,7,9]:
            corners_open.append(i)
    if len(corners_open) > 0:
        move = select_random(corners_open)
        return move

    if 5 in possible_moves:
        move = 5
        return move

    edges_open = []
    for i in possible_moves:
        if i in [2,4,6,8]:
            edges_open.append(i)
    if len(edges_open) > 0:
        move = select_random(edges_open)

    return move

def select_random(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def is_board_full(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    print("JOGO DA VELHA")
    print_board(board)

    while not(is_board_full(board)):
        if not(is_winner(board, 'O')):
            player_move()
            print_board(board)
        else:
            print("Infelizmente você perdeu!")
            break

        if not(is_winner(board, 'X')):
            move = computer_move()
            if move == 0:
                print("Empate!")
            else:
                insert_letter('O', move)
                print("O jogou na posição ", move , ":")
                print_board(board)
        else:
            print("Você ganhou! Parabéns!")
            break

    if is_board_full(board):
        print("Empate!")

main()
