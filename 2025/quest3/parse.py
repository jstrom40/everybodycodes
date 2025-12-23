from collections import Counter
class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        self.data = self._process_data()
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        data = [list(map(int, x.split(','))) for x in self.file][0]
        return data
    
    def part_one(self):
        total = 0

        test = self.data.copy()
        
        crates = self.data
        crates.sort()

        stacked_crates = []
        stacked_crates.append(crates.pop())

        while crates:
            validate = crates.pop()
            if validate < min(stacked_crates):
                stacked_crates.append(validate)
        total = sum(stacked_crates)
        
        print(sum(set(test)))
        
        return total

    def part_two(self):
        total = 0

        test = self.data.copy()

        crates = self.data
        crates.sort(reverse=True)

        stacked_crates = []
        stacked_crates.append(crates.pop())

        while crates:
            validate = crates.pop()
            if validate > max(stacked_crates):
                stacked_crates.append(validate)
        total = sum(stacked_crates[:20])
        print(sum(sorted(set(test))[:20]))

        return total
    
    def part_three(self):
        total = 0

        crates = self.data
        
        total = max(Counter(crates).values())

        return total


if __name__ == '__main__':
    example1 = AdventDay('example1')
    print('Example Part 1 -', example1.part_one())
    
    example2 = AdventDay('example2')
    print('Example Part 2 -', example2.part_two())
    
    example3 = AdventDay('example3')
    print('Example Part 3 -', example3.part_three())

    input1 = AdventDay('input1')
    print('Input Part 1 -', input1.part_one())

    input2 = AdventDay('input2')
    print('Input Part 2 -', input2.part_two())

    input3 = AdventDay('input3')
    print('Input Part 3 -', input3.part_three())