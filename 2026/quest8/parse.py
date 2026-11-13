from collections import defaultdict

class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        data = [list(x) for x in self.file]
        return data
    
    def part_one(self):
        total = 0

        data = self._process_data()
        r_len = len(data)
        c_len = len(data[0])

        grid = defaultdict(list)

        for r in range(r_len):
            for c in range(c_len):
                col = data[r][c]
                if col == '.':
                    continue
                else:
                    grid[(r - c)].append(int(col) if col != '.' else 0)
        
        for k, v in grid.items():
            subtotal = 0
            curr_ent = v[0]
            for ent in v:
                if ent == curr_ent:
                    subtotal += 1
                elif curr_ent < ent:
                    subtotal += 1
                    curr_ent = ent
                else:
                    curr_ent -= 1
            total += subtotal
        
        return total

    def part_two(self):
        total = 0

        data = self._process_data()
        r_len = len(data)
        c_len = len(data[0])

        

        # r-c is top-left to bottom-right
        # r+c is top-right to bottom-left
        dirs = ['UL', 'UR', 'L', 'R', 'BR', 'BL']
        for d in dirs:
            grid = defaultdict(list)
            
            for r in range(r_len):
                for c in range(c_len):
                    match d:
                        case 'UL':
                            val = r - c
                            col = data[r][c]
                        case 'UR':
                            val = r + c
                            col = data[r][c]
                        case 'L':
                            val = r
                            col = data[r][c]
                        case 'R':
                            val = r
                            col = data[r][c_len - c - 1]
                        case 'BR':
                            val = r + c
                            col = data[r_len - r - 1][c]
                        case 'BL':
                            val = r - c
                            col = data[r_len - r - 1][c]
                    if col == '.':
                        continue
                    else:
                        grid[val].append(int(col) if col != '.' else 0)
            
            subtotal = self.find_ents(grid)
            total += subtotal
            # print(d, subtotal, grid)

        return total
    
    def part_three(self):
        total = 0

        data = self._process_data()
        r_len = len(data)
        c_len = len(data[0])

        dirs = ['UL', 'UR', 'L', 'R', 'BR', 'BL']

        grid = defaultdict(list)
        d = dirs[0]
        round = 0
        for r in range(r_len):
            for c in range(c_len):
                match d:
                    case 'UL':
                        val = r - c
                        col = data[r][c]
                    case 'UR':
                        val = r + c
                        col = data[r][c]
                    case 'L':
                        val = r
                        col = data[r][c]
                    case 'R':
                        val = r
                        col = data[r][c_len - c - 1]
                    case 'BR':
                        val = r + c
                        col = data[r_len - r - 1][c]
                    case 'BL':
                        val = r - c
                        col = data[r_len - r - 1][c]
                if col == '.':
                    continue
                else:
                    grid[val].append(int(col) if col != '.' else 0)
        
        


        return total

    def find_ents(self, grid):
        total = 0
        for k, v in grid.items():
            curr_ent = v[0]
            for ent in v:
                if ent == curr_ent:
                    total += 1
                elif curr_ent < ent:
                    total += 1
                    curr_ent = ent
                else:
                    curr_ent -= 1
        return total


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