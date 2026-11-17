from collections import deque

class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        self._process_data()
        
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        self.sulphur = {}
        self.start = (0,0)
        self.end = (0,0)
        self.walls = []
        for x, row in enumerate(self.file):
            for y, col in enumerate(row):
                if col == '@':
                    self.sulphur[(x, y)] = len(self.sulphur)
                elif col == 'S':
                    self.start = (x, y)
                elif col == '#':
                    self.walls.append((x, y))
                elif col == 'E':
                    self.end = (x, y)
        self.x_len =len(self.file)
        self.y_len = len(self.file[0])
    
    def part_one(self):
        total = self.bfs()    
        
        return total

    def part_two(self):
        total = self.bfs(2026)

        return total
    
    def part_three(self):
        total = 0
        total = self.bfs(202620262026)

        return total

    def bfs(self, target=0, exact=False):

        # x, y, dir, current mask, dist
        dq = deque([(self.start[0], self.start[1], 'R', 0, 0)])
        visited = {(self.start[0], self.start[1], 'R', 0)}

        while dq:
            x, y, d, cnt, dist = dq.popleft()

            if (x, y) == self.end:
                if target:
                    if not exact:
                        if cnt >= target:
                            return dist
                    if exact:
                        if cnt == target:
                            return dist
                else:
                    if cnt.bit_count() == len(self.sulphur):
                        return dist

            for nx, ny, nd in self.moves(x, y, d):
                if (nx, ny) not in self.walls and nx in range(self.x_len) and ny in range(self.y_len):
                    next_cnt = cnt

                    if (nx, ny) in self.sulphur:
                        if target:
                            next_cnt += 1
                        else:
                            next_cnt |= (1 << self.sulphur[(nx, ny)])
                    state = (nx, ny, nd, next_cnt)
                    if state not in visited:
                        visited.add(state)
                        dq.append((nx, ny, nd, next_cnt, dist + 1))

    def moves(self,x,y,d):
        if d == 'R':
            return [(x,y+1,'R'),(x+1,y,'D'),(x-1,y,'U')]
        elif d == 'L':
            return [(x,y-1,'L'),(x+1,y,'D'),(x-1,y,'U')]
        elif d == 'U':
            return [(x-1,y,'U'),(x,y-1,'L'),(x,y+1,'R')]
        elif d == 'D':
            return [(x+1,y,'D'),(x,y-1,'L'),(x,y+1,'R')]
        else:
            assert False

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

    # input3 = AdventDay('input3')
    # print('Input Part 3 -', input3.part_three())