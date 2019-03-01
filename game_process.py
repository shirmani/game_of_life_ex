from multi_func import *

# start check neighbors and make next level


class GameProcess(MultiFunc):

    # Internal function # check_place_cell_neighbors
    # check the neighbors of one cell
    @staticmethod
    def neighbor_list(x, y, current):  # you need to right x and y by list index 0,1...
        neighbors = list()
        neighbors.append(current[y - 1][x + 1])
        neighbors.append(current[y][x + 1])
        neighbors.append(current[y + 1][x + 1])
        neighbors.append(current[y + 1][x])
        neighbors.append(current[y + 1][x - 1])
        neighbors.append(current[y][x - 1])
        neighbors.append(current[y - 1][x - 1])
        neighbors.append(current[y - 1][x])
        return neighbors

    # Internal function # check_neighbors_in_live
    # the func take care to spcial cell
    @staticmethod
    def check_place_cell_neighbors(x, y, current, size_board):  # you need to right x and y by list index 0,1...
        size_board -= 1
        if y == 0 and x == 0:
            neighbors = GameProcess.x_y_0(x, y, current)
            return neighbors

        elif x == size_board and y == 0:
            neighbors = GameProcess.x_size_board_y_0(x, y, current)
            return neighbors

        elif x == 0 and y == size_board:
            neighbors = GameProcess.y_size_board(x, y, current)
            del neighbors[2:4]
            return neighbors

        elif x == size_board and y == size_board:
            return GameProcess.y_x_size_board(x, y, current)

        elif x == 0:
            neighbors = GameProcess.neighbor_list(x, y, current)
            del neighbors[4:7]
            return neighbors

        elif y == 0:
            neighbors = GameProcess.neighbor_list(x, y, current)
            return neighbors[1:6]

        elif x == size_board:
            neighbors = GameProcess.x_size_board(x, y, current)
            return neighbors

        elif y == size_board:
            neighbors = GameProcess.y_size_board(x, y, current)
            return neighbors
        else:
            neighbors = GameProcess.neighbor_list(x, y, current)
            return neighbors

    # Internal function # of  check_place_cell start
    # in case y = size_board
    @staticmethod
    def y_size_board(x, y, current):  # you need to right x and y by list index 0,1...
        neighbors = list()
        neighbors.append(current[y - 1][x + 1])
        neighbors.append(current[y][x + 1])
        neighbors.append(current[y][x - 1])
        neighbors.append(current[y - 1][x - 1])
        neighbors.append(current[y - 1][x])
        return neighbors

    # Internal function # of check_place_cell start
    # in case x  = size_board
    @staticmethod
    def x_size_board(x, y, current):  # you need to right x and y by list index 0,1...
        neighbors = list()
        neighbors.append(current[y + 1][x])
        neighbors.append(current[y + 1][x - 1])
        neighbors.append(current[y][x - 1])
        neighbors.append(current[y - 1][x - 1])
        neighbors.append(current[y - 1][x])
        return neighbors

    # Internal function # of check_place_cell start
    # in case y = x = size_board
    @staticmethod
    def y_x_size_board(x, y, current):  # you need to right x and y by list index 0,1...
        neighbors = list()
        neighbors.append(current[y][x - 1])
        neighbors.append(current[y - 1][x - 1])
        neighbors.append(current[y - 1][x])
        return neighbors

    @staticmethod
    def x_y_0(x, y, current):
        neighbors = list()
        neighbors.append(current[y][x + 1])
        neighbors.append(current[y + 1][x + 1])
        neighbors.append(current[y + 1][x])
        return neighbors

    @staticmethod
    def x_size_board_y_0(x, y, current):
        neighbors = list()
        neighbors.append(current[y + 1][x])
        neighbors.append(current[y + 1][x - 1])
        neighbors.append(current[y][x - 1])
        return neighbors

    # Internal function # of check_place_cell start
    # check_place_cell end

    # check_new_generation
    # Internal function # check_new_generation
    @staticmethod
    def check_neighbors_in_live(x, y, size_board, current):
        live_neighbor = 0
        for neighbor in GameProcess.check_place_cell_neighbors(x, y, current, size_board):
            if neighbor == 1:
                live_neighbor += 1
        return live_neighbor

    # final func
    @staticmethod
    def check_new_generation(x, y, size_board, current, new_generation_list):
        live_neighbor = GameProcess.check_neighbors_in_live(x, y, size_board, current)
        cell = current[y][x]
        if live_neighbor <= 1:
            new_generation_list.append(0)
        elif live_neighbor == 2:
            new_generation_list.append(cell)
        elif live_neighbor == 3:
            new_generation_list.append(1)
        elif live_neighbor > 3:
            new_generation_list.append(0)
        return new_generation_list

    @staticmethod
    def append_board(size_board, list_board):
        counter = 0
        finish_board = []

        while counter != size_board:
            first_slicer = size_board * counter
            final_slicer = size_board * (counter + 1)
            a = list_board[first_slicer:final_slicer]
            finish_board.append(a)
            counter += 1
        return finish_board
