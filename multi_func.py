
class MultiFunc:

    # check if user fill only digit
    @staticmethod
    def check_digit(num_str):
        while not num_str.isdigit():
            num_str = input('please enter only number :')
        return num_str

    @staticmethod
    def print_board(board):
        for raw in board:
            print(raw, )

    @staticmethod
    def end_the_game():
        end_num = input('if you want to end the game press 1 \n'
                        'you want to continue ? press 0 \n'
                        ':')

        end_num = MultiFunc.check_digit(end_num)
        end_num = int(end_num)

        while not (end_num == 0 or end_num == 1):
            print('number need to be 1 or 0')
            end_num = input('if you want to end the game press 1\n'
                            'you want to continue ? press 0\n'
                            ':')
            end_num = int(MultiFunc.check_digit(end_num))

        return end_num

