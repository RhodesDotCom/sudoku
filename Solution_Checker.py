def split_rows(solution):
    list_of_rows = []
    for row in solution:
        list_of_rows.append(row)
    return list_of_rows


def split_columns(solution):
    list_of_columns = [[] for _ in range(9)]
    for row in solution:
        for column, number in enumerate(row):
            list_of_columns[column].append(number)
    return list_of_columns


def split_boxes(solution):
    list_of_boxes = [[] for _ in range(9)]
    for row_number, row in enumerate(solution):
        for column_number, number in enumerate(row):
            box_number = (row_number // 3) * 3 + (column_number // 3)
            list_of_boxes[box_number].append(number)
    return list_of_boxes


def check_list(list_of_list):
    number_check = [[False] * 9 for _ in range(9)]
    for index, list_of_numbers in enumerate(list_of_list):
        for number in list_of_numbers:
            number_check[index][number - 1] = True
    return not any(False in sublist for sublist in number_check)


def check_solution(solution):
    criteria = {'rows': False,
                'columns': False,
                'boxes': False
                }
    rows = split_rows(solution)
    columns = split_columns(solution)
    boxes = split_boxes(solution)
    criteria['rows'] = check_list(rows)
    criteria['columns'] = check_list(columns)
    criteria['boxes'] = check_list(boxes)
    return all(criteria.values())


validSolution = \
    [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]

invalidSolution = \
    [
        [5, 3, 4, 6, 7, 8, 9, 2, 2],
        [6, 7, 2, 1, 9, 0, 3, 4, 8],
        [1, 0, 0, 3, 4, 2, 5, 6, 0],
        [8, 5, 9, 7, 6, 1, 0, 2, 0],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 0, 1, 5, 3, 7, 2, 1, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 0, 0, 4, 8, 1, 1, 7, 9]
    ]


