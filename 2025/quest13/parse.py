class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        self.data = self._process_data()
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        if '-' in self.file[0]:
            data = [list(map(int, x.split('-'))) for x in self.file]
        else:
            data = list(int(x) for x in self.file)
        return data
    
    def part_one(self):
        total = 0

        dial = []
        dial.append(1)
        
        
        for val_index, val in enumerate(self.data):
            if val_index % 2 == 0:
                dial.append(val)
            else:
                dial.insert(0,val)

        # print(dial)
        dial_len = len(dial)
        total = dial[(dial.index(1) + 2025) % dial_len]
        
        return total

    def part_two(self):
        total = 0

        dial = [1]

        for index, range_vals in enumerate(self.data):
            start, end = range_vals
            if index %  2 == 0:
                dial.extend(range(start,end+1))
            else:
                dial[0:0] = range(start, end+1)

        print(dial, len(dial))
        dial_len = len(dial)
        total = dial[(dial.index(1) + 20252025) % dial_len]

        return total
    
    def part_three(self):
        total = 0

        return total


if __name__ == '__main__':
    example1 = AdventDay('example1')
    print('Example Part 1 -', example1.part_one())
    
    input1 = AdventDay('input1')
    print('Input Part 1 -', input1.part_one())
    
    example2 = AdventDay('example2')
    print('Example Part 2 -', example2.part_two())
    
    input2 = AdventDay('input2')
    print('Input Part 2 -', input2.part_two())

    # example3 = AdventDay('example3')
    # print('Example Part 3 -', example3.part_three())    

    # input3 = AdventDay('input3')
    # print('Input Part 3 -', input3.part_three())