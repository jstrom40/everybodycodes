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
            '>':(0,1),
            'v':(1,0),
            '^':(-1,0),
            '<':(0,-1)
        }
        # self.ghosts = defaultdict()
        self.ghosts = []
        self.walls = set()
        for x, row in enumerate(self.file):
            for y, col in enumerate(row):
                if col == '#':
                    self.walls.add((x, y))
                elif col in self.directions:
                    dir = self.directions[col]
                    self.ghosts.append([x, y, dir[0], dir[1],0])
    
    def part_one(self):
        rounds = 10
        for _ in range(rounds):
            self.cycle(1 << 63)
        collisions = sum(x[4] for x in self.ghosts)
        
        return collisions

    def part_two(self):
        limit = 10000
        round = 0

        while self.active_ghosts(limit):
            round += 1
            self.cycle(limit)

        return round
    
    def part_three(self):
        limit = 1000000000000
        round = 0

        while self.active_ghosts(limit):
            round += 1
            self.cycle(limit)

        return round

    def cycle(self, limit):
        temp = defaultdict(lambda: 0)
        for gi, (x, y, dx, dy, col) in enumerate(self.ghosts):
            nx, ny = x + dx, y + dy
            if (nx, ny) in self.walls:
                self.ghosts[gi][2] = dy
                self.ghosts[gi][3] = dx * -1
                self.ghosts[gi][4] += 1
                if self.ghosts[gi][4] < limit:
                    temp[(x, y)] += 1
            else:
                self.ghosts[gi][0] = nx
                self.ghosts[gi][1] = ny
                if self.ghosts[gi][4] < limit:                
                    temp[(nx, ny)] += 1
        for gi, (x, y, dx, dy, _) in enumerate(self.ghosts):
            if temp[(x, y)] > 1:
                self.ghosts[gi][2] = dx * -1
                self.ghosts[gi][3] = dy * -1
                self.ghosts[gi][4] += 1
    
    def active_ghosts(self, limit):
        return sum(1 for x in self.ghosts if x[4] < limit)


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