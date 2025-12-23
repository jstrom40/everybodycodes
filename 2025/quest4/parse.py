class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        self.data = self._process_data()
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        #part 1-2 parse
        # data = [int(x) for x in self.file]
        #part 3 parse
        data = [list(map(int, x.split('|'))) for x in self.file]
        
        return data
    
    def part_one(self):
        total = 0

        start_val = self.data[0]
        last_val = self.data[-1]

        total = int(start_val / last_val * 2025)
        
        return total

    def part_two(self):
        total = 0

        required_val = 10000000000000

        start_val = self.data[0]
        last_val = self.data[-1]

        total = required_val / (start_val / last_val)

        return total
    
    ## 625000000000
    
    def part_three(self):
        total = 0
    
        starting_gear = self.data[0][0]
        end_gear = self.data[-1][0]
        middle_gears = self.data[1:-1]

        rotation_amt = 1


        for gear in middle_gears:
            rotation_amt *= gear[1] / gear[0]
        
        total = int(100 * rotation_amt * starting_gear / end_gear)

        return total


if __name__ == '__main__':
    # example1 = AdventDay('example1')
    # print('Example Part 1 -', example1.part_one())
    
    # example2 = AdventDay('example2')
    # print('Example Part 2 -', example2.part_two())
    
    example3 = AdventDay('example3')
    print('Example Part 3 -', example3.part_three())

    # input1 = AdventDay('input1')
    # print('Input Part 1 -', input1.part_one())

    # input2 = AdventDay('input2')
    # print('Input Part 2 -', input2.part_two())

    input3 = AdventDay('input3')
    print('Input Part 3 -', input3.part_three())