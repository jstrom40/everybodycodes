from functools import cache
class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        self.is_example = example
        self._process_data()
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        self.stamps_part1 = [1, 3, 5, 10]
        self.stamps_part1.reverse()
        self.stamps_part2 = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30]
        self.stamps_part2.reverse()
        self.data = [int(x) for x in self.file]
    
    def part_one(self):
        total = 0

        for target in self.data:
            amount = self.greedy(target)
            total += amount
        
        return total

    def part_two(self):
        total = 0

        for target in self.data:
            amount = self.optimizer(target)
            total += amount
        
        return total
    
    def part_three(self):
        total = 0

        return total
    
    def greedy(self, target):
        res = 0

        for stamp in self.stamps_part1:
            if target >= stamp:
                cnt = target // stamp
                res += cnt

                target -= cnt * stamp
            if target == 0:
                break
        return res
    
    @cache
    def optimizer(self, target):
        if target == 0:
            return 0
        if target < 0:
            return 10**100
        best = 10**100
        for stamp in self.stamps_part2:
            sub = self.optimizer(target - stamp)
            best = min(best, sub + 1)
        return best



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