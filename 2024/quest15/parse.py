from collections import deque
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
    
    def part_one(self):
        total = 0

        self._process_data()
        sx, sy = self.find_start()

        total = self.dfs(sx, sy) * 2
        
        return total

    def part_two(self):
        total = 0

        self._process_data()
        sx, sy = self.find_start()

        return total
    
    def part_three(self):
        total = 0

        return total

    def dfs(self, sx, sy):

        dq = deque([(0,sx, sy)])
        seen = set()
        

        while dq:
            dist, x, y = dq.popleft()

            if self.data[x][y] == 'H':
                return dist
            
            if (x, y) in seen:
                continue

            seen.add((x, y))

            for nx, ny in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                if nx in range(self.x_len) and ny in range(self.y_len):
                    if self.data[x][y] == '.':
                        dq.append((dist+1, nx, ny))
        

    def find_start(self):
        for x, row in enumerate(self.data):
            for y, col in enumerate(row):
                if x == 0 or y == 0 or x == self.x_len or y == self.y_len:
                    if col == '.':
                        return x, y


if __name__ == '__main__':
    example1 = AdventDay('example1')
    print('Example Part 1 -', example1.part_one())
    
    input1 = AdventDay('input1')
    print('Input Part 1 -', input1.part_one())
    
    # example2 = AdventDay('example2')
    # print('Example Part 2 -', example2.part_two())
    
    # input2 = AdventDay('input2')
    # print('Input Part 2 -', input2.part_two())

    # example3 = AdventDay('example3')
    # print('Example Part 3 -', example3.part_three())    

    # input3 = AdventDay('input3')
    # print('Input Part 3 -', input3.part_three())