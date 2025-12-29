from collections import deque
class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        self.file_type = example
        self._process_data()

        self.moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                 (1, 2), (-1, 2), (1, -2), (-1, -2)]
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        self.data = [list(map(str, x)) for x in self.file]
        
        return None
    
    def part_one(self):
        total = 0
        starting_location = (0,0)
        visited = []
        turns = 4
        s_locations = []

        for row_index, row in enumerate(self.data):
            for col_index, col in enumerate(row):
                if col == 'D':
                    starting_location = (row_index, col_index)
                elif col == 'S':
                    s_locations.append((row_index, col_index))

        visited.append(starting_location)


        while turns > 0:
            for i in range(len(visited)):
                x, y = visited[i]
                for move_x, move_y in self.moves:
                    next_x = move_x + x
                    next_y = move_y + y
                    if x in range(len(self.data)) and y in range(len(self.data[0])):
                        visited.append((next_x, next_y))
            turns -= 1
        
        total = len(set(visited) & set(s_locations))
                    
        
        return total
    
    def part_one_dfs(self):
        total = 0
        
        row_len = len(self.data)
        col_len = len(self.data[0])
        
        for row_index, row in enumerate(self.data):
            for col_index, col in enumerate(row):
                if col == 'D':
                    start_x, start_y = row_index, col_index

        dq = deque([(0, start_x, start_y)])
        visited = set()
        turns = 4

        while dq:
            distance, x, y = dq.popleft()
            
            if distance > turns:
                continue
            if not (x in range(row_len) and y in range(col_len)):
                continue
            if (x, y) in visited:
                continue
            visited.add((x, y))

            if self.data[x][y] == 'S':
                total += 1
            
            for nx, ny in self.moves:
                dq.append((distance + 1, nx + x, ny + y))

        return total
    
    def part_two(self):
        total = 0
        
        row_len = len(self.data)
        col_len = len(self.data[0])
        sheep = []
        
        for row_index, row in enumerate(self.data):
            for col_index, col in enumerate(row):
                if col == 'D':
                    start_x, start_y = row_index, col_index
                elif col == 'S':
                    sheep.append((row_index, col_index))
        # sheep.sort()

        dq = deque([(0, start_x, start_y)])
        visited = set()
        eaten = set()
        turns = 3 if 'example' in self.file_type else 20

        while dq:
            distance, x, y = dq.popleft()
            
            if distance > turns:
                continue
            if not (x in range(row_len) and y in range(col_len)):
                continue
            if (distance, x, y) in visited:
                continue
            visited.add((distance, x, y))

            if distance > 0:
                for sheep_x, sheep_y in sheep:
                    if (sheep_x + distance, sheep_y) == (x,y) and self.data[x][y] != '#':
                        eaten.add((sheep_x, sheep_y))
                    if (sheep_x + distance - 1, sheep_y) == (x,y) and self.data[x][y] != '#':
                        eaten.add((sheep_x, sheep_y))
            
            for nx, ny in self.moves:
                dq.append((distance + 1, nx + x, ny + y))

        total = len(eaten)
        return total
    
    def part_three(self):
        total = 0

        row_len = len(self.data)
        col_len = len(self.data[0])
        sheep = []
        
        for row_index, row in enumerate(self.data):
            for col_index, col in enumerate(row):
                if col == 'D':
                    start_x, start_y = row_index, col_index
                elif col == 'S':
                    sheep.append((row_index, col_index))

        dq = deque([(0, start_x, start_y)])
        visited = set()
        eaten = set()

        while dq:
            distance, x, y = dq.popleft()
            
            if not (x in range(row_len) and y in range(col_len)):
                continue
            if (distance, x, y) in visited:
                continue
            visited.add((distance, x, y))

            if distance > 0:
                for sheep_x, sheep_y in sheep:
                    if (sheep_x + distance, sheep_y) == (x,y) and self.data[x][y] != '#':
                        eaten.add((sheep_x, sheep_y))
                    if (sheep_x + distance - 1, sheep_y) == (x,y) and self.data[x][y] != '#':
                        eaten.add((sheep_x, sheep_y))
            
            for nx, ny in self.moves:
                dq.append((distance + 1, nx + x, ny + y))

        return total
    


if __name__ == '__main__':
    example1 = AdventDay('example1')
    print('Example Part 1 -', example1.part_one())
    
    example1_dfs = AdventDay('example1')
    print('Example Part 1 DFS -', example1_dfs.part_one_dfs())

    input1 = AdventDay('input1')
    print('Input Part 1 -', input1.part_one())

    example2 = AdventDay('example2')
    print('Example Part 2 -', example2.part_two())
    
    # input2 = AdventDay('input2')
    # print('Input Part 2 -', input2.part_two())

    example3 = AdventDay('example3')
    print('Example Part 3 -', example3.part_three())    

    # input3 = AdventDay('input3')
    # print('Input Part 3 -', input3.part_three())