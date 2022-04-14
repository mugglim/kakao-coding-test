def solution(board, moves):
    n = len(board)
    doll_stack = []
    doll_board = [*board]
    cnt = 0
    
    
    def get_doll(col):
        doll = -1
        
        for row in range(n):
            if board[row][col] != 0:
                doll = board[row][col]
                board[row][col] = 0
                break
        return doll
    
    def add_doll(doll):
        # 같은 타입의 인형이 스택 마지막에 있는 경우
        nonlocal cnt
        if doll_stack and doll_stack[-1] == doll:
            doll_stack.pop()
            cnt += 2
            return
        
        doll_stack.append(doll)
    
    
    for col in moves:
        doll = get_doll(col-1)
        
        if doll != -1:
            add_doll(doll)
    
    return cnt
            