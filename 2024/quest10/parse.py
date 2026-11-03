class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        self.file_name = example
    
    def _read_file(self, file_name):
        if file_name == 'input2':
            with open(file_name, 'r') as f:
                return f.read().split('\n\n')
        else:
            with open(file_name, 'r') as f:
                return f.read().splitlines()

    def _process_data(self):
        if self.file_name == 'input2':
            data = self.file
        elif '3' in self.file_name:
            data = self.file
        else:
            data = [list(x) for x in self.file]
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.alphabet = self.alphabet.upper()
        
        return data
    
    def part_one(self):
        total = ''

        row_grid = self._process_data()
        col_grid = [list(col) for col in zip(*self._process_data())]
        
        for x, row in enumerate(row_grid):
            for y, col in enumerate(row):
                if col == '.':
                    common = list(set(row_grid[x]) & set(col_grid[y]) ^ set(['.']))[0]
                    total += common
        
        return total

    def part_two(self):
        total = 0

        if self.file_name == 'example2':
            grid = self._process_data()
            runic_word = self.runic_word(grid)
            total = self.calc_power(runic_word)
        else:
            grids = self._process_data()
            new_grids = []

            for g in grids:
                g = g.splitlines()
                new_list = [[] for _ in range(15)]
                new_list = [[] for _ in range(15)]
                for row in g:
                    row = row.split()
                    for index, subrow in enumerate(row):
                        new_list[index].append(subrow)
                new_grids.append(new_list)
            
            for x in new_grids:
                for y in x:
                    y = [list(col) for col in y]
                    runic_word = self.runic_word(y)
                    total += self.calc_power(runic_word)
        
        return total
    
    def part_three(self):
        total = 0

        grid = self._process_data()

        print(grid)

        return total
    
    def runic_word(self, grid):
        row_grid = grid
        col_grid = [list(col) for col in zip(*row_grid)]
        runic_word = ''    

        for x, row in enumerate(row_grid):
            for y, col in enumerate(row):
                if col == '.':
                    common = list(set(row_grid[x]) & set(col_grid[y]) ^ set(['.']))[0]
                    row_grid[x][y] = common
                    col_grid[y][x] = common
                    runic_word += common
        return runic_word
    
    def calc_power(self, runic_word):
        word_total = 0
        for index, letter in enumerate(runic_word, start=1):
            word_total += index * (self.alphabet.index(letter) + 1)

        return word_total



if __name__ == '__main__':
    example1 = AdventDay('example1')
    print('Example Part 1 -', example1.part_one())
    
    input1 = AdventDay('input1')
    print('Input Part 1 -', input1.part_one())
    
    example2 = AdventDay('example2')
    print('Example Part 2 -', example2.part_two())
    
    input2 = AdventDay('input2')
    print('Input Part 2 -', input2.part_two())

    example3 = AdventDay('example3')
    print('Example Part 3 -', example3.part_three())    

    # input3 = AdventDay('input3')
    # print('Input Part 3 -', input3.part_three())