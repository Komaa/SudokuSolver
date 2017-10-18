assignments = []
rows = 'ABCDEFGHI'
cols = '123456789'


def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """

    # Don't waste memory appending actions that don't actually change any values
    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values


def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers
    for box in values:
        if len(values[box]) == 2:
            for unit in units[box]:
                for comparing_box in unit:
                    if comparing_box != box and values[box] == values[comparing_box]:
                        # print("naked twins", values[box], box, values[comparing_box], comparing_box)
                        for value in values[box]:
                            for box_to_filter in unit:
                                if box_to_filter != comparing_box and box_to_filter != box:
                                    assign_value(values, box_to_filter, values[box_to_filter].replace(value, ""))

    return values


def cross(a, b):
    "Cross product of elements in A and elements in B."
    return [s + t for s in a for t in b]


boxes = cross(rows, cols)
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
diagonal_units = [[column_units[i][i] for i in range(len(column_units))],
                  [column_units[len(column_units) - 1 - i][i] for i in range(len(column_units) - 1, -1, -1)]]
square_units = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]
unitlist = row_units + column_units + square_units + diagonal_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s], [])) - set([s])) for s in boxes)


def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    grid_dict = {}
    for i in range(0, len(grid)):
        grid_dict[boxes[i]] = grid[i]
        if grid[i] == '.':
            grid_dict[boxes[i]] = '123456789'
    return grid_dict


def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1 + max(len(values[s]) for s in boxes)
    line = '+'.join(['-' * (width * 3)] * 3)
    for r in rows:
        print(''.join(values[r + c].center(width) + ('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return


def eliminate(values):
    for box in values:
        if len(values[box]) == 1:
            for peer in peers[box]:
                assign_value(values, peer, values[peer].replace(values[box], ""))
                # values[peer] = values[peer].replace(values[box], "")
    return values


def only_choice(values):
    for box in values:
        if len(values[box]) > 1:
            for possib in values[box]:
                for unit in units[box]:
                    unique = True
                    for peer in peers[box]:
                        if peer != box and possib in values[peer]:
                            unique = False
                            break
                    if unique:
                        assign_value(values, box, possib)
                        # values[box] = possib
                        break
    return values


def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        # Your code here: Use the Eliminate Strategy
        eliminate(values)
        # Your code here: Use the Only Choice Strategy
        only_choice(values)
        # display(values)
        # print("before-------------")
        naked_twins(values)

        # display(values)
        # print("after-------------")
        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values


def search(values):
    solution = reduce_puzzle(values)
    if not solution:
        return False
    solved = True
    for box in values:
        if len(values[box]) > 1:
            solved = False
    if solved:
        return solution

    min = 10
    for box in values:
        if len(values[box]) < min and len(values[box]) > 1:
            min = len(values[box])
            c_box = box

    for i in values[c_box]:
        candidate = dict(values)
        assign_value(candidate, c_box, i)
        # candidate[c_box] = i
        solution = search(candidate)
        if solution:
            return solution


def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values = grid_values(grid)
    display(values)
    return search(values)


if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments

        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
