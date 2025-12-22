class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        self._process_data()
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        self.names = self.file[0].split(',')
        self.instructions = self.file[2].split(',')
    
    def part_one(self):
        final_word = ''
        names_len = len(self.names)

        current_index = 0

        for dir in self.instructions:
            move_amount = int(dir[1:])
            if dir[0] == 'L':
                move_amount = move_amount * -1
            if (current_index + move_amount) >= names_len:
                current_index = names_len - 1
            elif (current_index + move_amount) < 0:
                current_index = 0
            else:
                current_index += move_amount
        
        final_word = self.names[current_index]
        return final_word

    def part_two(self):
        final_word = ''
        names_len = len(self.names)

        current_index = 0

        for dir in self.instructions:
            move_amount = int(dir[1:])
            if dir[0] == 'L':
                move_amount = move_amount * -1
            current_index = (current_index + move_amount) % names_len
        
        final_word = self.names[current_index]
        return final_word

    def part_three(self):
        final_word = ''
        names_len = len(self.names)

        data = self.names.copy()

        current_index = 0
        swap_index = 0

        for dir in self.instructions:
            move_amount = int(dir[1:])
            if dir[0] == 'L':
                move_amount = move_amount * -1
            swap_index = (move_amount) % names_len
            current_name = data[current_index]
            next_name = data[swap_index]
            data[current_index] = next_name
            data[swap_index] = current_name
            # current_index = swap_index

        
        final_word = data[0]
        return final_word


if __name__ == '__main__':
    example = AdventDay('example')
    print('Example Part 1 -', example.part_one())
    print('Example Part 2 -', example.part_two())
    print('Example Part 3 -', example.part_three())

    input1 = AdventDay('input1')
    print('Input Part 1 -', input1.part_one())

    input2 = AdventDay('input2')
    print('Input Part 2 -', input2.part_two())

    input3 = AdventDay('input3')
    print('Input Part 3 -', input3.part_three())