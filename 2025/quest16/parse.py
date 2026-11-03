class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read()

    def _process_data(self):
        data = [int(x) for x in self.file.split(',')]
        return data
    
    def part_one(self):
        total = 0

        instructions = self._process_data()
        columns = 90

        for inst in instructions:
            total += columns // inst
        
        return total

    def part_two(self):
        total = 0

        instructions = self._process_data()
        
        

        return total
    
    def part_three(self):
        total = 0

        return total
    def add_to_grid(self, grid, dist):
        i = 0
        while i < len(grid):
            if grid[i][-1] == '.':
                grid[i][-1] = '#'
            else:
                grid[i].extend('#')
            i += dist

        return grid

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