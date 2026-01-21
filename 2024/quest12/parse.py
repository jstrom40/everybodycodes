class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        data = [list(x) for x in self.file[0:-1]]

        self.segment = {
            "A": 1,
            "B": 2,
            "C": 3
        }
        
        return data
    
    def part_one(self):
        total = 0
        
        grid = self._process_data()

        print(self.find_point(grid, 'C'))
        print(self.find_point(grid, 'T'))
        
        return total

    def part_two(self):
        total = 0

        return total
    
    def part_three(self):
        total = 0

        return total

    def find_point(self, grid, point):

        for x, row in enumerate(grid):
            for y, col in enumerate(row):
                if col == point:
                    return (x, y)

if __name__ == '__main__':
    example1 = AdventDay('example1')
    print('Example Part 1 -', example1.part_one())
    
    # input1 = AdventDay('input1')
    # print('Input Part 1 -', input1.part_one())
    
    # example2 = AdventDay('example2')
    # print('Example Part 2 -', example2.part_two())
    
    # input2 = AdventDay('input2')
    # print('Input Part 2 -', input2.part_two())

    # example3 = AdventDay('example3')
    # print('Example Part 3 -', example3.part_three())    

    # input3 = AdventDay('input3')
    # print('Input Part 3 -', input3.part_three())