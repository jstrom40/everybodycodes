class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        self.data = self._process_data()
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        data = [list(map(int, x.split(' '))) for x in self.file]

        return data
    
    def part_one(self):
        total = ''

        rounds = 10

        people = self.data.copy()
        people = [list(col) for col in zip(*people)]

        for i in range(rounds):
            people = self.parse_rounds(people, i)
            
        for x in people:
            total += str(x[0])
            
        return total

    def part_two(self):
        total = ''

        people = self.data.copy()
        people = [list(col) for col in zip(*people)]
        rounds = 10

        for i in range(rounds):
            people = self.parse_rounds(people, i)
            number = ''.join([str(x[0]) for x in people])
            print(i, '-', number)


        return total
    
    def part_three(self):
        total = 0

        return total
    
    def parse_rounds(self, people, iteration):
        
        row_len = len(people)
        current_row = iteration % row_len
        next_row = (current_row + 1) % row_len
        next_row_len = len(people[next_row])

        popped_val = people[current_row].pop(0)
        mod_index = popped_val % next_row_len
        num_loops = popped_val // next_row_len

        if (popped_val <= next_row_len):
            popped_value_insert_index = popped_val - 1
        elif mod_index == 0:
            popped_value_insert_index = popped_val
        else:
            if num_loops % 2 == 0:
                popped_value_insert_index = popped_val - 1
            else:
                popped_value_insert_index = popped_val
        people[next_row].insert(popped_value_insert_index, popped_val)
            
        return people


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