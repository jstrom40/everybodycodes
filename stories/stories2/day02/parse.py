class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read()

    def _process_data(self):
        data = self.file
        self.fluffbots = ['R', 'G', 'B']
        return data
    
    def part_one(self):
        total = 0

        data = self._process_data()

        for balloon in data:
            if balloon != self.fluffbots[0]:
                self.fluffbots.append(self.fluffbots.pop(0))
                total += 1
        

        return total

    def part_two(self):
        total = 0

        repeat = 5

        balloons = list(self._process_data() * repeat)

        print(balloons)

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
    
    # input2 = AdventDay('input2')
    # print('Input Part 2 -', input2.part_two())

    # example3 = AdventDay('example3')
    # print('Example Part 3 -', example3.part_three())    

    # input3 = AdventDay('input3')
    # print('Input Part 3 -', input3.part_three())