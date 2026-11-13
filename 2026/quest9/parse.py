from heapq import heappush, heappop
from collections import defaultdict

class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        data = []
        for row in self.file:
            row = row.replace(', ', '=').split('=')
            data.append((int(row[1]), int(row[3]), int(row[5])))
        return data
    
    def part_one(self):
        total = 0

        data = self._process_data()
        for _, growth, limit in data:
            elements = self.grow_tree(growth, limit)
        
        return total

    def part_two(self):
        total = 0

        return total
    
    def part_three(self):
        total = 0

        return total

    def grow_tree(self, growth, limit):
        half_delay = (growth - 1) // 2
        fresh_delay = growth - 1

        splits_at = defaultdict(int)

        splits_at[growth] = 1
        elements = 1
        total = 1
        time = 1
        while total < limit:
            time += 1
            splits = splits_at.pop(time, 0)
            total += elements + splits
            if splits:
                elements += 2 * splits
                splits_at[time + half_delay] += splits * 2
                splits_at[time + fresh_delay] += splits



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