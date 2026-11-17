import math

class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        hands = [int(x) for x in self.file[0].split()[1].split(':')]
        directions = [1 if x == 'CW' else -1 for x in self.file[1].split()[1].split(':')]
        current = [int(x) for x in self.file[2].split()[1].split(':')]
        move = [int(x) for x in self.file[3].split()[1].split(':')]

        return hands, directions, current, move
    
    def part_one(self):
        total = 0

        hands, directions, current, move = self._process_data()
        # Gives the least common multiple of hands so that we have an equal number of "ticks" on the clock
        points = math.lcm(*hands)
        
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