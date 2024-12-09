# The elves are playing with a magical train 🚂 that carries gifts. This train moves on a board represented by an array of strings.

# The train consists of an engine (@), followed by its carriages (o), and must collect magical fruits (*) which serve as fuel. The movement of the train follows these rules:

# You will receive two parameters board and mov.

# board is an array of strings that represents the board:

# @ is the train's engine.
# o are the train's carriages.
# * is a magical fruit.
# · are empty spaces.
# mov is a string that indicates the next movement of the train from the train's head @:

# 'L': left
# 'R': right
# 'U': up
# 'D': down.
# With this information, you must return a string:

# 'crash': If the train crashes into the edges of the board or itself.
# 'eat': If the train collects a magical fruit (*).
# 'none': If it moves without crashing or collecting any magical fruit.

from typing import List, Literal

board1 = ["·····", "*····", "@····", "o····", "o····"]


def move_train(
    board: List[str], mov: Literal["U", "D", "R", "L"]
) -> Literal["none", "crash", "eat"]:

    position = [0, 0]
    len_board = -1
    for i, b in enumerate(board):
        if "@" in b:
            position = [i, b.index("@")]
            len_board = len(b)
            break

    if mov == "U":
        position = [x + y for x, y in zip(position, [-1, 0])]
    if mov == "D":
        position = [x + y for x, y in zip(position, [1, 0])]
    if mov == "R":
        position = [x + y for x, y in zip(position, [0, 1])]
    if mov == "L":
        position = [x + y for x, y in zip(position, [0, -1])]

    if (
        position[0] < 0
        or position[1] < 0
        or position[0] >= len_board
        or position[1] >= len_board
    ):
        return "crash"

    if board[position[0]][position[1]] == "o":
        return "crash"

    if board[position[0]][position[1]] == "*":
        return "eat"

    return "none"


print(move_train(board1, "R"))
