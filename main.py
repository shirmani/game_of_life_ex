from game_of_life.start_game_func import *
from game_of_life.game_process import *
from game_of_life.multi_func import *

#The_game_of_life.
# building a new board
size_board = input('please enter the size of board:')
size_board = int(MultiFunc.check_digit(size_board))

choice = StartGameFunc.check_input_choice()
# the board filled by the computer

if choice == 3:
    board = StartGameFunc.board_build(size_board)
    full_board = StartGameFunc.random_fill(size_board, board)
    MultiFunc.print_board(full_board)

# the board filled by the user
elif choice == 2:
    board = StartGameFunc.board_build(size_board)
    print('you need to enter ' + str(size_board) + ' number in each raw\n'
          'you need to enter only 0 / 1')
    StartGameFunc.user_fill(size_board, board)
    full_board = board
    MultiFunc.print_board(full_board)



# start the game
print('\nstarting the game')

# file's variable
current = full_board
end_num = 0

while not end_num == 1:
    level_counter = 0
    end_num = MultiFunc.end_the_game()

    while end_num == 0:
        new_generation_list = []
        print('\n')

        y = -1
        for raw in current:
            y += 1
            x = 0
            for cell in raw:
                new_generation_list = GameProcess.check_new_generation(x, y, size_board, current, new_generation_list)
                x += 1

        new_generation = GameProcess.append_board(size_board, new_generation_list)

        MultiFunc.print_board(new_generation)

        if current == new_generation:
            end_num = MultiFunc.end_the_game()
        elif level_counter == 100:
            end_num = MultiFunc.end_the_game()
        else:
            current = new_generation
            level_counter += 1


print('game over')
