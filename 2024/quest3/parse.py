from collections import deque
class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        self._process_data()
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        self.data = [list(x) for x in self.file]
        self.search_area = [(1,0), #D 
                            (0,-1),#L
                            (-1,0),#U
                            (0,1)  #R
                            ] 
        self.search_area_part_3 = [(1,0), #D
                                   (1,-1), 
                                   (0,-1),#L
                                   (-1,-1),
                                   (-1,0),#U
                                   (-1,1),
                                   (0,1), #R
                                   (1,1)
                                  ] 
    
    def part_one(self):
        total = 0
        row_len = len(self.data)
        col_len = len(self.data[0])
        grid = [[0] * col_len for _ in range(row_len)]
        safe, not_safe = [],[]

        for row_index, row in enumerate(self.data):
            for col_index, col in enumerate(row):
                if col == '#':
                    grid[row_index][col_index] = 1
                    safe.append((row_index, col_index))
        
        for x in grid:
            total += sum(x)

        while safe:
            x, y = safe.pop(0)
            status = True
            for mx, my in self.search_area:
                nx, ny = mx + x, my + y
                if (nx in range(row_len) and ny in range(col_len)):
                    test = grid[nx][ny]
                    if grid[nx][ny] >= grid[x][y]:
                        continue
                    else:
                        status = False
                        break
            if status:
                total += 1
                grid[x][y] += 1
                safe.append((x, y))
        
        
        return total

    def part_two(self):
        total = 0
        row_len = len(self.data)
        col_len = len(self.data[0])
        grid = [[0] * col_len for _ in range(row_len)]
        safe, not_safe = [],[]

        for row_index, row in enumerate(self.data):
            for col_index, col in enumerate(row):
                if col == '#':
                    grid[row_index][col_index] = 1
                    safe.append((row_index, col_index))
        
        for x in grid:
            total += sum(x)

        while safe:
            x, y = safe.pop(0)
            status = True
            for mx, my in self.search_area:
                nx, ny = mx + x, my + y
                if (nx in range(row_len) and ny in range(col_len)):
                    test = grid[nx][ny]
                    if grid[nx][ny] >= grid[x][y]:
                        continue
                    else:
                        status = False
                        break
                    
            if status:
                total += 1
                grid[x][y] += 1
                safe.append((x, y))
        return total
    
    def part_three(self):
        total = 0
        row_len = len(self.data)
        col_len = len(self.data[0])
        grid = [[0] * col_len for _ in range(row_len)]
        safe, not_safe = [],[]

        for row_index, row in enumerate(self.data):
            for col_index, col in enumerate(row):
                if col == '#':
                    grid[row_index][col_index] = 1
                    safe.append((row_index, col_index))
        
        for x in grid:
            total += sum(x)

        while safe:
            x, y = safe.pop(0)
            status = True
            for mx, my in self.search_area_part_3:
                nx, ny = mx + x, my + y
                if (nx in range(row_len) and ny in range(col_len)):
                    if (grid[nx][ny] >= grid[x][y]) and (grid[nx][ny] > 0):
                        continue
                    else:
                        status = False
                        break
                else:
                    status = False
                    break
            if status:
                total += 1
                grid[x][y] += 1
                safe.append((x, y))
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

    input3 = AdventDay('input3')
    print('Input Part 3 -', input3.part_three())