from itertools import combinations

class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        self._process_data()
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        self.data = list(x.split(':')[1] for x in self.file)
        
        return None
    
    def part_one(self):
        total = 0
        print(self.data[0][1])

        for i, child in enumerate(self.data):
            parents = [d for j, d in enumerate(self.data) if i != j]
            is_child = self._is_child(child, parents)
            print(i, is_child)
            
        return total

    def part_two(self):
        total = 0

        return total
    
    def part_three(self):
        total = 0

        return total
    
    def _is_child(self, child, parents):
        parents_flipped = [list(col) for col in zip(*parents)]
        total = 0
        total_1 = 0
        total_2 = 0
        for i, val in enumerate(child):
            if val not in parents_flipped[i]:
                return 0
            else:
                total_1 += parents_flipped[i][0].count(val)
                total_2 += parents_flipped[i][1].count(val)
        total = total_1 * total_2
        return total
    
            


if __name__ == '__main__':
    example1 = AdventDay('example1')
    print('Example Part 1 -', example1.part_one())
    
    input1 = AdventDay('input1')
    print('Input Part 1 -', input1.part_one())
    
    # example2 = AdventDay('example2')
    # print('Example Part 2 -', example2.part_two())
    
    # input2 = AdventDay('input2')
    # print('Input Part 2 -', input2.part_two())

    # example3 = AdventDay('example3')
    # print('Example Part 3 -', example3.part_three())    

    # input3 = AdventDay('input3')
    # print('Input Part 3 -', input3.part_three())