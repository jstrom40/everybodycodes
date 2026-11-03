from collections import deque, Counter
class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        self.cells, self.palms, self.starts = set(), set(), set()
        x_len = len(self.file)
        y_len = len(self.file[0])
        for x, line in enumerate(self.file):
            for y, col in enumerate(line):
                if (x == 0 or y == 0 or x == x_len - 1 or y == y_len - 1) and col == '.':
                    self.starts.add((x, y))
                if col == 'P':
                    self.palms.add((x, y))
                    self.cells.add((x, y))
                if col == '.':
                    self.cells.add((x, y))
    
    def part_one(self):
        total = 0

        self._process_data()
        distances = self.dfs(self.starts)
        
        total = max(distances[p] for p in self.palms)

        
        return total

    def part_two(self):
        total = 0

        self._process_data()

        distances = self.dfs(self.starts)
                
        total = max(distances[p] for p in self.palms)

        return total
    
    def part_three(self):
        total = 0

        self._process_data()
        total_dist = Counter()

        for sp in self.palms:
            total_dist += self.dfs([sp])
        total = min(total_dist[p] for p in total_dist if p not in self.palms)

        # directions = self.dfs()
        # print(directions)

        return total

    def dfs(self, start_list):
        layer = start_list
        time = 0
        seen = Counter()

        while layer:
            new_layer = []
            for cell in layer:
                x, y = cell
                if cell in seen:
                    continue
                seen[cell] = time

                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in self.cells and (nx, ny) not in seen:
                        new_layer.append((nx, ny))
            time += 1
            layer = new_layer
        return seen

        


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