class Grid:
    def __init__(self, data):
        self.grid = [list(x) for x in data]
    
    def print_grid(self):
        for row in self.grid:
            print(row)
        print()

    def find_points(self):
        source = self.find_pieces_coordinates('@')
        self.target = self.find_pieces_coordinates('#')
        return source, self.target
    
    def find_surrounded_points(self):
        surrounding_points = []
        x, y = self.target
        for mx, my in [(0,1),(0,-1),(1,0),(-1,0)]:
            surrounding_points.append((x + mx, y + my))
        return surrounding_points
        

    def find_pieces_coordinates(self, piece):
        for x, row in enumerate(self.grid):
            for y, col in enumerate(row):
                if col == piece:
                    return (x, y)
class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    # def _process_data(self):
        # data = 
        # return data
    
    def part_one(self):
        total = 0

        grid = Grid(self.file)

        source, target = grid.find_points()
        
        x,y = source
        mx, my = 0,-1
        seen = set()

        while True:
            if (x,y) == target:
                break
            mx, my = my, -mx
            nx, ny = x + mx, y + my
            if (nx, ny) in seen:
                continue
            seen.add((x, y))
            x, y = nx, ny
            
        total = len(seen)
            
        
        return total

    def part_two(self):
        total = 0

        grid = Grid(self.file)
        
        source, target = grid.find_points()
        sp = grid.find_surrounded_points()

        x,y = source
        mx, my = 0,-1
        seen = set()
        
        while True:
            if set(sp).issubset(seen):
                break
            mx, my = my, -mx
            nx, ny = x + mx, y + my
            if (nx, ny) in seen:
                continue
            seen.add((x, y))
            x, y = nx, ny

        return total
    
    def part_three(self):
        total = 0

        return total


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