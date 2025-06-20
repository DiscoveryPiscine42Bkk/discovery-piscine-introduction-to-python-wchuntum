def checkmate(board_str):
    board = board_str.strip().split('\n')
    size = len(board)

    # หาตำแหน่งของ King
    king_pos = None
    for i in range(size):
        for j in range(len(board[i])):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos:
        return  # ไม่เจอ King เลย

    ki, kj = king_pos

    # Directions
    rook_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    bishop_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    pawn_dirs = [(-1, -1), (-1, 1)]  # Pawn โจมตีเฉียงขึ้น

    # ตรวจ Rook และ Queen (แนวตรง)
    for dx, dy in rook_dirs:
        x, y = ki + dx, kj + dy
        while 0 <= x < size and 0 <= y < len(board[x]):
            ch = board[x][y]
            if ch != '.':
                if ch in 'RQ':
                    print("Success")
                    return
                break
            x += dx
            y += dy

    # ตรวจ Bishop และ Queen (แนวทแยง)
    for dx, dy in bishop_dirs:
        x, y = ki + dx, kj + dy
        while 0 <= x < size and 0 <= y < len(board[x]):
            ch = board[x][y]
            if ch != '.':
                if ch in 'BQ':
                    print("Success")
                    return
                break
            x += dx
            y += dy

    # ตรวจ Pawn
    for dx, dy in pawn_dirs:
        x, y = ki + dx, kj + dy
        if 0 <= x < size and 0 <= y < len(board[x]):
            if board[x][y] == 'P':
                print("Success")
                return