class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        self._process_data()
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read()

    def _process_data(self):
        self.mappings = {
            "A": 0,
            "B": 1,
            "C": 3,
            "D": 5
        }
        # self.data = list(map(str, x)) for x in self.file
        self.data = self.file
    
    def part_one(self):
        total = 0

        for beetle in self.data:
            total += self.mappings[beetle]
        
        return total

    def part_two(self):
        total = 0

        pairs = [self.data[i:i+2] for i in range(0, len(self.data), 2)]
        for pair in pairs:
            left, right = pair
            total += self.mappings.get(left, 0)
            total += self.mappings.get(right, 0)
            if 'x' not in pair:
                total += 2
                

        return total
    
    def part_three(self):
        total = 0

        pairs = [self.data[i:i+3] for i in range(0, len(self.data), 3)]
        for pair in pairs:
            for beetle in pair:
                total += self.mappings.get(beetle, 0)
            if pair.count('x') == 1:
                total += 2
            if 'x' not in pair:
                total += 6
            # print(total)

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

    example3 = AdventDay('example3')
    print('Example Part 3 -', example3.part_three())    

    input3 = AdventDay('input3')
    print('Input Part 3 -', input3.part_three())