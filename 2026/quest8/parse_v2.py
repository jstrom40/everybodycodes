from collections import defaultdict

class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        self._process_data()
        
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        self.directions = {
            "TL": (1,1),
            "TR": (1,-1),
            "R": (0,-2),
            "BR": (-1,-1),
            "BL": (-1,1),
            "L": (0,2)
        }
        self.start_directions = {
            "TL": ((-1,1), (0,2)),
            "BL": ((1,1), (0,2)),
            "TR": ((0,2),(1,1)),
            "BR": ((1,-1), (0,-2)),
            "L": ((1,-1), (1,1)),
            "R": ((1,1), (1,-1))
        }
        self.x_len = len(self.file)
        self.y_len = len(self.file[0])
        self.grid = {}
        self.starts = {}
    
        for r, row in enumerate(self.file):
            for c, col in enumerate(row):
                if col != '.':
                    self.grid[(r,c)] = int(col)
                    if c == 0:
                        self.starts['TL'] = (r, c)
                        self.starts['BL'] = (r, c)
                    if c == self.y_len - 1:
                        self.starts['BR'] = (r, c)
                    if r == 0 and 'L' not in self.starts:
                        self.starts['L'] = (r, c)
                        self.starts['TR'] = (r, c)
                        self.starts['R'] = (r, self.y_len - c - 1)
        self.warriors = 0
    
    def part_one(self):
        
        total = self.find_ents('TL')
        
        return total

    def part_two(self):
        total = 0

        self.find_ents('R')

        for dir in self.directions:
            total += self.find_ents(dir) 

        return total
    
    def part_three(self):
        total = 0
        rounds = [dir for dir in self.directions]

        while self.warriors < 100000:
            round_dir = rounds.pop(0)
            rounds.append(round_dir)
            total += self.find_ents(round_dir, True)
        
        return total


    def find_ents(self, direction, round3 = False):
        start = self.starts[direction]
        next_dir = self.start_directions[direction]
        energy = 0

        while start:
            subenergy = self.find_path(start, direction, round3)
            # print(start, subenergy)
            energy += subenergy
            x, y = start
            for dx, dy in next_dir:
                nx, ny = x + dx, y + dy
                if (nx, ny) in self.grid:
                    start = (nx, ny)
                    break
            else:
                start = None
        return energy

    def find_path(self, start, direction, round3=False):
        x, y = start

        energy = 1 if self.grid[start] > 0 else 0
        dx, dy = self.directions[direction]
        shadow = self.grid[start]

        if round3:
            
            if self.grid[start] == 9:
                self.warriors += 1
                self.grid[start] = -2
            else:
                self.grid[start] += 1


        nx, ny = x + dx, y + dy
        while (nx, ny) in self.grid:
            cur_ent = self.grid[(nx, ny)]
            shadow = max(0, shadow - 1)
            if cur_ent > shadow:
                if cur_ent > 0:
                    energy += 1
                    shadow = self.grid[nx, ny]
                if round3:
                    self.grid[(nx, ny)] += 1
            elif cur_ent < 1:
                self.grid[(nx, ny)] += 1
            if round3 and self.grid[(nx, ny)] == 10:
                self.grid[(nx, ny)] = -2
                self.warriors += 1
            nx, ny = (nx + dx, ny + dy)
        return energy


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

    input3 = AdventDay('input3')
    print('Input Part 3 -', input3.part_three())