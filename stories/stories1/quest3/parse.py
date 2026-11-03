class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        data = []
        for row in self.file:
            row = row.replace('=', ' ').split()
            data.append((int(row[1]), int(row[3])))
        return data
    
    def part_one(self):
        total = 0

        snails = self._process_data()
        for _ in range(100):
            for i in range(len(snails)):
                snails[i] = self.move_snails(snails[i])
        
        for snail in snails:
            total += self.score_snails(snail)
        
        return total

    def part_two(self):
        total = 0

        return total
    
    def part_three(self):
        total = 0

        return total
    
    def move_snails(self, snail):
            x, y = snail
            if y == 1:
                x, y = y, x
            else:
                y -= 1
                x += 1
            return (x, y)
    def score_snails(self, snail):
        x, y = snail
        return x + (100 * y)


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