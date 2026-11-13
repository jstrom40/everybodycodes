class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        self._process_data()
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        self.magma = []
        for x, row in enumerate(self.file):
            for y, col in enumerate(row):
                if col == '#':
                    self.magma.append((x, y))
        self.directions = [(0,1), (1,0), (-1,0), (0,-1)]
        self.x_len = len(self.file)
        self.y_len = len(self.file[0])
    
    def part_one(self):
        total = 0

        seen = set()
        for x, y in self.magma:
            if (x, y) in seen:
                continue
            seen.add((x, y))

            queue = [(x, y)]
            subtotal = []
            while True:
                x, y = queue.pop()
                subtotal.append((x, y))
                for dx, dy in self.directions:
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in self.magma and (nx, ny) not in seen:
                        queue.append((nx, ny))
                        seen.add((nx,ny))
                if not queue:
                    # print(subtotal)
                    distinct_x = {x for x, y in subtotal}
                    distinct_y = {y for x, y in subtotal}
                    total += min(len(distinct_x), len(distinct_y))
                    break
        return total

    def part_two(self):
        total = 0

        return total
    
    def part_three(self):
        total = 0

        return total


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