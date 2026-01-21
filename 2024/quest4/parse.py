class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        self.data = self._process_data()
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        data = list(int(x) for x in self.file)
        return data
    
    def part_one(self):
        total = 0

        min_nail = min(self.data)

        for nail in self.data:
            if nail > min_nail:
                total += nail - min_nail
        
        return total

    def part_two(self):
        total = 0

        min_nail = min(self.data)

        for nail in self.data:
            if nail > min_nail:
                total += nail - min_nail

        return total
    
    def part_three(self):
        total = 0

        nails = self.data.copy()

        nails.sort()

        target = nails[len(nails)//2]
        for nail in nails:
            total += abs(nail - target)

        return total


if __name__ == '__main__':
    example1 = AdventDay('example1')
    print('Example Part 1 -', example1.part_one())
    
    input1 = AdventDay('input1')
    print('Input Part 1 -', input1.part_one())
    
    # example2 = AdventDay('example2')
    # print('Example Part 2 -', example2.part_two())
    
    input2 = AdventDay('input2')
    print('Input Part 2 -', input2.part_two())

    example3 = AdventDay('example3')
    print('Example Part 3 -', example3.part_three())    

    input3 = AdventDay('input3')
    print('Input Part 3 -', input3.part_three())