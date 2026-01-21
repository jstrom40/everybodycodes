class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        self.data = self._process_data()
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        data = [list(x) for x in self.file]

        self.moves = [(1,1),(1,-1),(-1,-1),(-1,1)]
        return data
    
    def part_one(self):
        total = 0

        grid = self.data
        
        row_len = len(grid)
        col_len = len(grid[0])

        for _ in range(10):
            grid = self.parse_grid(grid, row_len, col_len)
            for row in grid:
                total += row.count('#')
        
        return total
    
    def parse_grid(self, grid, row_len, col_len):
        new_grid = [['.'] * col_len for _ in range(row_len)]
        for x, row in enumerate(grid):
            for y, col in enumerate(row):
                active_total = 0
                inactive_total = 0
                for move_x, move_y in self.moves:
                    next_x, next_y = move_x + x, move_y + y
                    if (next_x in range(row_len) and next_y in range(col_len)):
                        if grid[next_x][next_y] == '.':
                            inactive_total += 1
                        else:
                            active_total += 1
                if col == '#':
                    if (active_total % 2 == 0):
                        new_grid[x][y] = '.'
                    else:
                        new_grid[x][y] = '#'
                elif col == '.':
                    if (active_total % 2 == 0):
                        new_grid[x][y] = '#'
                    else:
                        new_grid[x][y] = '.'

        return new_grid

    def part_two(self):
        total = 0

        grid = self.data
        
        row_len = len(grid)
        col_len = len(grid[0])

        for _ in range(2025):
            grid = self.parse_grid(grid, row_len, col_len)
            for row in grid:
                total += row.count('#')
        
        return total
    
    def part_three(self):
        total = 0
        
        row_len = 34
        col_len = 34

        grid = [['.'] * col_len for _ in range(row_len)]

        for _ in range(1000000000):
            grid = self.parse_grid(grid, row_len, col_len)
            check_grid = [row[13:21] for row in grid[13:21]]
            if check_grid == self.data:
                for row in grid:
                    total += row.count('#')
        
        return total


if __name__ == '__main__':
    example1 = AdventDay('example1')
    print('Example Part 1 -', example1.part_one())
    
    input1 = AdventDay('input1')
    print('Input Part 1 -', input1.part_one())
    
    # example2 = AdventDay('example2')
    # print('Example Part 2 -', example2.part_two())
    
    input2 = AdventDay('input2')
    print('Input Part 2 -', input2.part_two())

    example3 = AdventDay('example3')
    print('Example Part 3 -', example3.part_three())

    # input3 = AdventDay('input3')
    # print('Input Part 3 -', input3.part_three())