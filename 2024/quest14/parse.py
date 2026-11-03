from collections import Counter 
from heapq import heappop, heappush

class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        data = self.file
        self.directions = {
            "U": (0,1,0),
            "D": (0,-1,0),
            "R": (1,0,0),
            "L": (-1,0,0),
            "F": (0,0,1),
            "B": (0,0,-1),
        }
        return data
    
    def part_one(self):
        total = 0

        x, y, z = 0,0,0
        blocks = set()

        data = self._process_data()[0].split(',')
        for dir in data:
            dx, dy, dz = self.directions[dir[0]]
            amt = int(dir[1:])
            x, y, z = x + dx * amt, y + dy * amt, z + dz * amt
            blocks.add((x,y,z))

        total = max(y for x, y, z in blocks)

        
        return total

    def part_two(self):
        data = self._process_data()
        
        blocks = set()

        for row in data:
            x, y, z = 0,0,0
            for dir in row.split(','):
                dx, dy, dz = self.directions[dir[0]]
                amt = int(dir[1:])
                for _ in range(amt):
                    x, y, z = x + dx, y + dy, z + dz
                    blocks.add((x, y, z))

        return len(blocks)
    
    def part_three(self):
        total = 0

        data = self._process_data()

        blocks = set()
        leaves = set()

        for row in data:
            x, y, z = 0,0,0
            for dir in row.split(','):
                dx, dy, dz = self.directions[dir[0]]
                amt = int(dir[1:])
                for _ in range(amt):
                    x, y, z = x + dx, y + dy, z + dz
                    blocks.add((x, y, z))
            leaves.add((x, y, z))
        

        trunk = self.find_trunk(blocks)

        for leaf in leaves:
            self.find_start(leaf,trunk,blocks)
        return total

    def find_trunk(self, branches):
        trunk = set()
        for x, y, z in branches:
            if x == z == 0:
                trunk.add((x, y, z))
        return trunk

    def find_start(self, start, trunk, blocks):
        dist = 0
        visited = set()
        hq = []
        heappush(hq, (0, start))
        test = Counter()

        while hq:
            dist, (x, y, z) = heappop(hq)
            visited.add((x, y, z))
            if (x,y,z) in trunk:
                test[(x, y, z)] = dist
                break
            for dx, dy, dz in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
                nx, ny, nz = x + dx, y + dy, z + dz
                if (nx, ny, nz) in blocks and (nx, ny, nz) not in visited:
                    heappush(hq, (dist+1, (nx,ny,nz)))
                




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