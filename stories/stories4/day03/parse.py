class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.top = False
        self.right = False
        self.bottom = False
        self.left = False

    def is_isolated(self):
        return self.top and self.right and self.bottom and self.left

class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):

        self.width = int(self.file[0].split('=')[1])
        self.height = int(self.file[1].split('=')[1])

        self.h_offset = list(self.file[2].split('=')[1])
        self.h_len = len(self.h_offset)

        self.v_offset = list(self.file[3].split('=')[1])
        self.v_len = len(self.v_offset)
    
    def part_one(self):
        total = 0

        self._process_data()

        grid = []

        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(Tile(x, y))
            grid.append(row)

        # for x in range(self.width):
        #     print(self.v_offset[x % self.v_len])
        #     print(self.v_offset[(x + 1) % self.v_len])

        for y in range(self.height):
            first_check = self.h_offset[y % self.h_len]
            second_check = self.h_offset[(y + 1) % self.h_len]
            for x in range(self.width):
                if x % 2 == 0:
                    if first_check == '0':
                        grid[y][x].top = True
                    if second_check == '0':
                        grid[y][x].bottom = True
                else:
                    if first_check == '1':
                        grid[y][x].top = True
                    if second_check == '1':
                        grid[y][x].bottom = True

        for x in range(self.width):
            first_check = self.v_offset[x % self.v_len]
            second_check = self.v_offset[(x + 1) % self.v_len]
            for y in range(self.height):
                if y % 2 == 0:
                    if first_check == '0':
                        grid[y][x].left = True
                    if second_check == '0':
                        grid[y][x].right = True
                else:
                    if first_check == '1':
                        grid[y][x].left = True
                    if second_check == '1':
                        grid[y][x].right = True
        for x in range(self.height):
            for y in range(self.width):
                if grid[x][y].is_isolated():
                    total += 1

        
        return total

    def part_two(self):
        total = 0

        return total
    
    def part_three(self):
        total = 0

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