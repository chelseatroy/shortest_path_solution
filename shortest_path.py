from collections import namedtuple

class Board():
    rows = []

    def __init__(self, rows):
        self.rows = rows
        
    def columns(self, index):
        return [row[index] for row in self.rows]

    def find_start(self):
        start_row = 0
        start_column = 0
        for index, row in enumerate(self.rows):
            if 'S' in row:
                start_row = index
                start_column = row.index('S')
                break
        return start_row, start_column

def extend(paths, board):
    new_paths = []
    for path in paths:
        last_item = path[-1]

        #north
        if last_item.row > 0:
            new_row = last_item.row - 1
            new_column = last_item.column
            updated_path = path + [Space(new_row, new_column, board.rows[new_row][new_column])]
            new_paths.append(updated_path)
        #west
        if last_item.column > 0:
            new_row = last_item.row
            new_column = last_item.column - 1
            updated_path = path + [Space(new_row, new_column, board.rows[new_row][new_column])]
            new_paths.append(updated_path)
        #south
        if last_item.row + 1 < len(board.rows):
            new_row = last_item.row + 1
            new_column = last_item.column
            updated_path = path + [Space(new_row, new_column, board.rows[new_row][new_column])]
            new_paths.append(updated_path)
        #east
        if last_item.column + 1 < len(board.rows[0]): #assumes a rectangular board
            new_row = last_item.row
            new_column = last_item.column + 1
            updated_path = path + [Space(new_row, new_column, board.rows[new_row][new_column])]
            new_paths.append(updated_path)

    return new_paths

def track_paths(board, steps=999999999):
    start_row, start_column = board.find_start()

    max_steps = steps
    current_steps = 0

    paths = [[Space(start_row, start_column, 'S')]]

    while current_steps < max_steps:
        paths = extend(paths, board)
        current_steps += 1

    return paths

Space = namedtuple('Space', ['row', 'column', 'value'])

def shortest_path(board):
    # Find start
    # go outward from the start and put each result in its own list
    # if the list ends in 1 or an already visited node, discard the list
    # go until all remaining lists end in 'E'
    # select the shortest one

    return 0

##############################


def test_track_paths():
    board = Board([
        [0, 0, 0, 0],
        [1, 1, 0, 'S'],
        [0, 0, 0, 0],
        ['E', 0, 0, 0],
    ])
    result = track_paths(board, steps=1)
    if result == [
        [Space(row=1, column=3, value='S'), Space(0, 3, 0)],
        [Space(row=1, column=3, value='S'), Space(1, 2, 0)],
        [Space(row=1, column=3, value='S'), Space(2, 3, 0)]
    ]:
        print("SUCCESS on TRACKING PATHS!")
    else:
        raise Exception(f"Whoops, track_paths returned {result}.")

test_track_paths()

def test_find_start():
            board = Board([
                [0, 0, 0, 0],
                [1, 1, 0, 'S'],
                [0, 0, 0, 0],
                ['E', 0, 0, 0],

            ])

            result = board.find_start()

            if result == (1, 3):
                print("SUCCESS on FINDING START!")
            else:
                raise Exception(f"Whoops, find_start should have been (1, 3) but was {result}.")


test_find_start()

def test_column():
                    board = Board([
                        ['S', 0, 0, 0],
                        [1, 1, 0, 0],
                        [0, 0, 0, 0],
                        ['E', 0, 0, 0],

                    ])

                    result = board.columns(1)

                    if result == [0, 1, 0, 0]:
                        print("SUCCESS on COLUMN CALCULATION!")
                    else:
                        raise Exception(f"Whoops, columns should have been [0, 1, 0, 0] but was {result}.")

test_column()

def test_shortest_path():
    board = Board([
        ['S', 0, 0, 0],
        [ 1,  1, 0, 0],
        [ 0,  0, 0, 0],
        ['E', 0, 0, 0],

    ])

    result = shortest_path(board)

    if result == 7:
        print("SUCCESS!")
    else:
        raise Exception(f"Whoops, shortest path should have been 7 but was {result}.")

test_shortest_path()

