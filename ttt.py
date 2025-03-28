import random

def print_board(board):
    for r in range(3):
        print(" " + " | ".join(board[r]))
        if r != 2:
            print("---|---|---")
def check_winner(board, player):
    # 가로, 세로, 대각선 체크
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
def get_empty_positions(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
def computer_move(board):
    empty_positions = get_empty_positions(board)
    if empty_positions:
        x, y = random.choice(empty_positions)
        board[x][y] = 'O'
def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]    
    while True:
        print_board(board)        
        # 사용자 입력 받기
        try:
            x = int(input("다음 수의 x좌표를 입력하시오: "))
            y = int(input("다음 수의 y좌표를 입력하시오: "))
            if board[x][y] != ' ':
                print("잘못된 위치입니다.")
                continue1
        except (ValueError, IndexError):
            print("올바른 좌표를 입력하세요 (0~2 범위의 숫자 두 개).")
            continue      
        board[x][y] = 'X'
        if check_winner(board, 'X'):
            print_board(board)
            print("당신이 이겼습니다.")
            break       
        if not get_empty_positions(board):
            print_board(board)
            print("무승부입니다")
            break        
        print("컴퓨터의 차례...")
        computer_move(board)
        
        if check_winner(board, 'O'):
            print_board(board)
            print("컴퓨터가 이겼습니다.")
            break        
        if not get_empty_positions(board):
            print_board(board)
            print("무승부입니다")
            break
tic_tac_toe()
