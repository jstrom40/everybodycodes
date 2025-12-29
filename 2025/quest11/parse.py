class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        self.file_name = example
        self.data = self._process_data()
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        data = list(int(x) for x in self.file)

        return data
    
    def part_one(self):
        total = 0

        flocks = self.data.copy()

        max_rounds = 10
        rounds = 0
        flocks, rounds = self._phase_one(max_rounds, flocks)

        flocks, rounds = self._phase_two(max_rounds, rounds, flocks)

        for col_index, duck in enumerate(flocks, start=1):
            total += col_index * duck
        
        return total
    
    def _phase_one(self, max_rounds, flocks):
        round = 0
        moved = True
        while moved and round <= max_rounds:
            moved = False
            for i in range(len(flocks) - 1):
                if flocks[i] > flocks[i+1]:
                    flocks[i] -= 1
                    flocks[i+1] += 1
                    moved = True
            if not moved:
                break
            round += 1
        return flocks, round
    
    def _phase_two(self, max_rounds, round, flocks):
        moved = True
        while moved and round < max_rounds:
            moved = False
            for i in range(len(flocks) - 1):
                if flocks[i] < flocks[i+1]:
                    flocks[i] += 1
                    flocks[i+1] -= 1
                    moved = True
            if not moved:
                break
            round += 1
        return flocks, round

    def part_two(self):
        total = 0

        flocks = self.data.copy()

        max_rounds = 10000000
        round = 0
        flocks, round = self._phase_one(max_rounds, flocks)
        flocks, round = self._phase_two(max_rounds, round, flocks)
        
        total = round

        return total
    
    def part_three(self):
        total = 0
        
        flocks = self.data.copy()
        flocks.sort()

        flocks_len = len(flocks)
        flocks_sum = sum(flocks)
        avg_flock = flocks_sum / flocks_len
        
        total = sum(avg_flock - x for x in flocks if x < avg_flock)

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

    example3 = AdventDay('example3')
    print('Example Part 3 -', example3.part_three())    

    input3 = AdventDay('input3')
    print('Input Part 3 -', input3.part_three())