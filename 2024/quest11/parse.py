from collections import defaultdict
from functools import cache
class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        data = defaultdict(list)
        for row in self.file:
            parent, children = row.split(':')
            data[parent] = children.split(',')
        
        return data
    
    def part_one(self):
        total = 0

        generations = self._process_data()

        current_termite_list = []
        current_termite_list.append('A')

        for _ in range(4):
            new_termite_list = []
            for termite in current_termite_list:
                new_termite_list.extend(generations[termite])
            current_termite_list = new_termite_list

        total = len(current_termite_list)
        
        return total

    def part_two(self):
        total = 0

        generations = self._process_data()

        current_termite_list = []
        current_termite_list.append('Z')

        for _ in range(10):
            new_termite_list = []
            for termite in current_termite_list:
                new_termite_list.extend(generations[termite])
            current_termite_list = new_termite_list

        total = len(current_termite_list)

        return total
    
    def part_three(self):
        total = 0

        generations = self._process_data()
        termite_type = generations.keys()

        min_termite_amt = 0
        max_termite_amt = 0

        self.find_population('A', generations)

        # for t_type in termite_type:
            # current_termite_list = []
            # self.find_population(t_type)

            

        # total = max_termite_amt - min_termite_amt
        # for _ in range(20):
        #     for termite
        #         for termite in current_termite_list:
        #             new_termite_list.extend(generations[termite])
        #         current_termite_list = new_termite_list
        # termite_count = len(current_termite_list)
        # if min_termite_amt == 0:
        #     min_termite_amt = termite_count
        # min_termite_amt = min(min_termite_amt, termite_count)
        # max_termite_amt = max(max_termite_amt, termite_count)

        return total

    @cache
    def find_population(self, termite_type, generations):
        termite_count = 1
        print(generations[termite_type])
        # print(generations[termite_type])
            

        return None

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

    # input3 = AdventDay('input3')
    # print('Input Part 3 -', input3.part_three())