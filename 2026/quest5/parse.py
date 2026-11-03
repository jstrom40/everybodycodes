import copy
class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        self.data = [list(x) for x in self.file]
        self.x_len = len(self.data)
        self.y_len = len(self.data[0])
        self.neighbors = ((0,1),(-1,0),(0,-1),(1,0),(1,1),(-1,1),(-1,-1),(1,-1))
    
    def part_one(self):
        total = 0

        self._process_data()

        self.find_land()
        total = self.fill_water()
        
        return total

    def part_two(self):
        total = 0

        self._process_data()
        self.find_land()
        _ = self.fill_water()

        self.fill_sand()
        self.grow_sand()

        total = sum(x.count('=') for x in self.data)

        return total
    
    def part_three(self):
        total = 0

        self._process_data()
        self.find_land()
        _ = self.fill_water()

        self.fill_sand()
        self.grow_sand()

        self.stamp_trees()

        self.grow_trees()
        self.grow_trees()

        total = sum(x.count('@') for x in self.data)

        return total

    def print_grid(self):
        for row in self.data:
            print(''.join(x for x in row))
        print()
            

    def find_land(self):
        start_x, start_y = self.x_len // 2, self.y_len // 2

        self.data[start_x][start_y] = '#'

        count, neighbors = self.get_neighbors(start_x, start_y, '#1', '01')
        queue = set(neighbors)

        while queue:
            x, y = queue.pop()
            count, neighbors = self.get_neighbors(x, y, '#1', '01')
            if count >= 5:
                self.data[x][y] = '#'
                queue.update(neighbors)

    def get_neighbors(self, x, y, chk_val, nei_val, bad_val = ''):
        neighbors = []
        count = 0
        invalid = False
        for dx, dy in self.neighbors:
            nx, ny = x + dx, y + dy
            if nx in range(self.x_len) and ny in range(self.y_len):
                ch = self.data[nx][ny]
                if ch in chk_val:
                    count += 1
                if ch in bad_val:
                    invalid = True
                    break
                if ch in nei_val:
                    neighbors.append((nx, ny))
        if invalid:
            count = 0
        return count, neighbors

    def fill_water(self):
        count = 0
        for x, row in enumerate(self.data):
            for y, col in enumerate(row):
                if col in '01':
                    self.data[x][y] = '.'
                else:
                    count += 1
        return count
    
    def fill_sand(self):
        for x, row in enumerate(self.data):
            for y, col in enumerate(row):
                if col == '#':
                    count, neighbors = self.get_neighbors(x, y, '#=', '')
                    if count < 8:
                        self.data[x][y] = '='
    
    def grow_sand(self):
        queue = set()
        for x, row in enumerate(self.data):
            for y, col in enumerate(row):
                if col == '#':
                    queue.add((x, y))
        while queue:
            x, y = queue.pop()
            if self.data[x][y] == '=':
                continue
            count, neighbors = self.get_neighbors(x, y, '=', '#')
            if count >= 5:
                self.data[x][y] = '='
                queue.update(neighbors)
    
    def stamp_trees(self):
        for x, row in enumerate(self.data):
            for y, col in enumerate(row):
                if col == '#':
                    is_valid = True
                    for nx, ny in ((x-1, y-2), (x, y-2), (x+1, y-2),
                                   (x-2, y-1), (x-1, y-1), (x, y-1), (x+1, y-1), (x+2, y-1),
                                   (x-2, y), (x-1, y), (x+1, y), (x+2, y),
                                   (x-2, y+1), (x-1, y+1), (x, y+1), (x+1, y+1), (x+2, y+1),
                                   (x-1, y+2), (x, y+2), (x+1, y+2)):
                        if nx in range(self.x_len) and ny in range(self.y_len):
                            if self.data[nx][ny] not in '@#':
                                is_valid = False
                                break
                    if is_valid:
                        self.data[x][y] = '@'
    def grow_trees(self):
        new_data = copy.deepcopy(self.data)
        for x, row in enumerate(self.data):
            for y, col in enumerate(row):
                if col == '#':
                    count_t, _ = self.get_neighbors(x,y,'@','','=')
                    if count_t >= 4:
                        new_data[x][y] = '@'
        self.data = new_data




if __name__ == '__main__':
    example1 = AdventDay('example1')
    print('Example Part 1 -', example1.part_one())
    
    input1 = AdventDay('input1')
    print('Input Part 1 -', input1.part_one())
    
    example2 = AdventDay('example2')
    print('Example Part 2 -', example2.part_two())
    
    input2 = AdventDay('input2')
    print('Input Part 2 -', input2.part_two())

    example3 = AdventDay('example3')
    print('Example Part 3 -', example3.part_three())    

    input3 = AdventDay('input3')
    print('Input Part 3 -', input3.part_three())