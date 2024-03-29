def get_playing_board(star):
    row = ' *' * ((star + 2) // 2)
    board = ''
    for i in range(star):
        board += row[i % 2:star + i % 2] + '\n'
    return board

print(get_playing_board(5))
print(get_playing_board(10))
board_of_5 = "  * *  \n" "* * * \n" "  * *  \n" "* * * \n" "  * *  \n"
board_of_10 = (
    " * * * * *\n"
    "* * * * * \n"
    " * * * * *\n"
    "* * * * * \n"
    " * * * * *\n"
    "* * * * * \n"
    " * * * * *\n"
    "* * * * * \n"
    " * * * * *\n"
    "* * * * * \n"
)


print(get_playing_board(7))