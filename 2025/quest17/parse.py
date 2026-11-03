class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        data = []
        for row in self.file:
            row = row.replace('@', '0')
            row = [int(x) for x in row]
            data.append(row)
        return data
    
    def part_one(self):
        total = 0

        grid = self._process_data()
        vx, vy = self.find_start(grid)
        radius = 10
        
        for x, row in enumerate(grid):
            for y, col in enumerate(row):
                if self.destroy_block(vx, vy, x, y, radius):
                    total += col
        
        return total

    def part_two(self):
        total = 0

        grid = self._process_data()
        vx, vy = self.find_start(grid)
        max_radius = len(grid[0]) // 2
        damage_list = []
        

        for i in range(max_radius):
            radius_total = 0
            for x, row in enumerate(grid):
                for y, col in enumerate(row):
                    if self.destroy_block(vx, vy, x, y, i+1):
                        radius_total += col
                        grid[x][y] = 0
            damage_list.append(radius_total)
        
        max_damage = max(damage_list)
        total = max_damage * (damage_list.index(max_damage) + 1)


        return total
    
    def part_three(self):
        total = 0

        return total
    
    def find_start(self, grid):
        for x, row in enumerate(grid):
            for y, col in enumerate(row):
                if col == 0:
                    return x, y
                
    def destroy_block(self, vx, vy, x, y, radius):
        return ((vx - x) ** 2 + (vy - y) ** 2) <= (radius ** 2)



if __name__ == '__main__':
    example1 = AdventDay('example1')
    print('Example Part 1 -', example1.part_one())
    
    input1 = AdventDay('input1')
    print('Input Part 1 -', input1.part_one())
    
    example2 = AdventDay('example2')
    print('Example Part 2 -', example2.part_two())
    
    input2 = AdventDay('input2')
    print('Input Part 2 -', input2.part_two())

    # example3 = AdventDay('example3')
    # print('Example Part 3 -', example3.part_three())    

    # input3 = AdventDay('input3')
    # print('Input Part 3 -', input3.part_three())