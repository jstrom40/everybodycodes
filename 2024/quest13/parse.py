from heapq import heappop, heappush

class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        self.grid = [list(x) for x in self.file]
    
    def part_one(self):
        total = 0

        self._process_data()

        start = (0, self.grid[0].index('.'))
        end_character = 'H'

        td, end = self.dfs(start, end_character)
        bd, start = self.dfs(end, start)

        total = td + bd
        
        
        return total

    def part_two(self):
        total = 0

        self._process_data()

        start = (0, self.grid[0].index('.'))

        return total
    
    def part_three(self):
        total = 0

        return total
    
    def part_2(self, start, end):
        hq = []
        heappush(hq, (0, start))
        visited = set()

        while hq:
            distance, (x, y) = heappop(hq)

            
            if (x, y) in visited:
                continue
            visited.add((x, y))

            for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if nx in range(len(self.grid)) and ny in range(len(self.grid[0])):
                    if self.grid[nx][ny] == '#':
                        continue
                    heappush(hq, (distance + 1, (nx, ny)))
        return None, None
    
    def dfs(self, start, end):
        hq = []
        heappush(hq, (0, start))
        visited = set()

        while hq:
            distance, (x, y) = heappop(hq)

            if isinstance(end, tuple):
                if end == (x, y):
                    return distance, (x, y)
            else:
                if end == self.grid[x][y]:
                    return distance, (x, y)
            
            if (x, y) in visited:
                continue
            visited.add((x, y))

            for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if nx in range(len(self.grid)) and ny in range(len(self.grid[0])):
                    if self.grid[nx][ny] == '#':
                        continue
                    heappush(hq, (distance + 1, (nx, ny)))
        return None, None


if __name__ == '__main__':
    example1 = AdventDay('example1')
    print('Example Part 1 -', example1.part_one())
    
    input1 = AdventDay('input1')
    print('Input Part 1 -', input1.part_one())
    
    example2 = AdventDay('example2')
    print('Example Part 2 -', example2.part_two())
    
    # input2 = AdventDay('input2')
    # print('Input Part 2 -', input2.part_two())

    # example3 = AdventDay('example3')
    # print('Example Part 3 -', example3.part_three())    

    # input3 = AdventDay('input3')
    # print('Input Part 3 -', input3.part_three())