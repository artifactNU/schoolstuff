# # --------------------------
# x = type(5)
# print(x)

# s = "hejsan hoppsan"
# l = [100, 200, 300, 400, 500, 600]

# s_tre = s[:3]
# s_tre_sista = s[-3:]

# l_tre = l[:3]
# l_tre_sista = l[-3:]

# # refeerence by value
# a = ["a", "b", "c"]
# b = a[:]
# e = a.copy()

# spara = b.pop()

# c = 1
# d = c
# d += 1
# # list with different types
# lst = [1, "hej", 3.14, [1, 2, 3]]


# # rensa lista
# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# # letters[:] = []
# letters.clear()

# # --------------------------
# # tic tac toe

# # tic tac toe nested list
# board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


# # print board
# def print_board(board):
#     for row in board:
#         print(row)


# # promt player to make a move
# def make_move(board, player, row, col):
#     if board[row][col] == 0:
#         board[row][col] = player
#         return True
#     else:
#         return False


# print_board(board)


# # check if a player has won
# def has_won(board, player):
#     # check rows
#     for row in board:
#         if row.count(player) == 3:
#             return True

#     # check columns
#     for i in range(3):
#         if board[0][i] == player and board[1][i] == player and board[2][i] == player:
#             return True

#     # check diagonals
#     if board[0][0] == player and board[1][1] == player and board[2][2] == player:
#         return True

#     if board[0][2] == player and board[1][1] == player and board[2][0] == player:
#         return True

#     return False


# # --------------------------
# # Fibonacci sequence
# a = 0
# b = 1

# while a < 10:

#     print(a)

#     a, b = b, a + b

# # --------------------------
# Create a sample collection
users = {"Hans": "active", "Éléonore": "inactive", "景太郎": "active"}

# Strategy:  Iterate over a copy
active_users = users.copy()
to_delete = []
for user, status in active_users.items():
    if status == "inactive":
        to_delete.append(user)

for user in to_delete:
    del active_users[user]
    # print(f"deletet {user}")
    # del active_users[user]

# Strategy:  Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == "active":
#         active_users[user] = status
