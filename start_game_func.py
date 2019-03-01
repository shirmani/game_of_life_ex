from random import *
from game_of_life.multi_func import *


class StartGameFunc(MultiFunc):

    # one- time func
    # check who the user want to fill the start board
    @staticmethod
    def check_input_choice():
        user_choice = 0
        while not (user_choice == 2 or user_choice == 3):
            user_choice = input('if you want to fill the board alon enter 2\n'
                                'if you want to get full board enter 3\n'
                                ':')
            user_choice = int(StartGameFunc.check_digit(user_choice))
        return user_choice

    # start board
    @staticmethod
    def board_build(size_board):
        board = []
        for raw in range(0, size_board):
            board.append([])

        return board

    # main func
    @staticmethod
    def random_fill(size_board, board):
        for raw in board:
            for cell in range(0, size_board):
                num = randint(0, 1)
                raw.append(num)

        return board

    # user fill & checking funcs start

    # Internal function # check_len_of_num
    # do list from user filled
    @staticmethod
    def do_list_from_num(num):
        num_list = []
        for i in num:
            i = int(i)
            num_list.append(i)

        return num_list

    # Internal function # check_user_fill
    # check if len of user fill == size_board
    @staticmethod
    def check_len_of_num(num_list, size_board):
        try:
            assert len(num_list) == size_board, 'wrong option'
        except AssertionError:
            while len(num_list) != size_board:
                print('you need to give {} numbers'.format(size_board))
                num_str = input('enter the raw again:')
                num_str = StartGameFunc.check_digit(num_str)
                num_list = StartGameFunc.do_list_from_num(num_str)
            return num_list  # num_list_2
        else:
            num_list = StartGameFunc.check_digit(num_list)
            num_list = StartGameFunc.do_list_from_num(num_list)
            return num_list  # num_list_2

    # Internal function # check_user_fill
    # check if user fill only 0 / 1
    @staticmethod
    def check_option_of_number(num_list):
        counter = -1
        for i in num_list:
            counter += 1

            while not (i == 0 or i == 1):
                print('number need to be 1 or 0')
                print(num_list)
                del num_list[counter]
                i = input('enter number into {} place:'.format(counter + 1))
                i = StartGameFunc.check_digit(i)
                i = int(i)
                num_list.insert(counter, i)

        return num_list  # num_list_3

    # Internal function # user_fill
    # check user fill
    @staticmethod
    def check_user_fill(num_list, size_board):
        num_list_1 = StartGameFunc.check_digit(num_list)
        num_list_2 = StartGameFunc.check_len_of_num(num_list_1, size_board)
        num_list_3 = StartGameFunc.check_option_of_number(num_list_2)
        return num_list_3

    # user fill func
    @staticmethod
    def user_fill(size_board, board):
        raw_count = 1
        for raw in board:
            num = input('to raw {} enter {} numbers:'.format(str(raw_count), str(size_board)))
            num = StartGameFunc.check_user_fill(num, size_board)
            raw_count += 1
            for i in num:
                raw.append(i)
