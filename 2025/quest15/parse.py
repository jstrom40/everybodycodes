from collections import deque

class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        data = self.file[0].split(',')
        return data
    
    def part_one(self):
        total = 0

        instructions = self._process_data()
        seen, end_location = self.find_visited(instructions)
        total = self.dfs(seen, end_location)
        
        
        return total

    def part_two(self):
        total = 0

        instructions = self._process_data()
        seen, end_location = self.find_visited(instructions)
        total = self.dfs(seen, end_location)

        return total
    
    def part_three(self):
        total = 0

        instructions = self._process_data()
        seen, end_location = self.find_visited(instructions)
        total = self.dfs(seen, end_location)

        return total
    
    def find_visited(self, instructions):
        x, y = (0,0)
        mx, my = (-1,0)
        seen = set()

        for inst in instructions:
            dir = inst[0]
            amount = int(inst[1:])
            if dir == 'R':
                mx, my = (my, -mx)
            else:
                mx, my = (-my, mx)
            for i in range(amount):
                nx, ny = x + (mx * i), y + (my * i)
                seen.add((nx, ny))

            x, y = x + (mx * amount), y + (my * amount)
        return seen, (x, y)
    
    def dfs(self, seen, target):

        minx, maxx = 0,0
        miny, maxy = 0,0
        for x, y in seen:
            minx = min(minx, x)
            maxx = max(maxx, x)
            miny = min(miny, y)
            maxy = max(maxy, y)
        print(minx, maxx,miny, maxy)
        
        
        tx, ty = target
        dq = deque([(0, 0, 0)])
        visited = set()

        while dq:
            distance, x, y = dq.popleft()

            if (x, y) == (tx,ty):
                return distance
            if (x, y) in visited:
                continue
            visited.add((x, y))

            for mx, my in [(0,1), (1,0), (-1,0), (0, -1)]:
                nx, ny = x + mx, y + my
                if (nx, ny) not in seen:
                    if nx in range(minx-1, maxx+1) and ny in range(miny-1, maxy+1):
                        dq.append((distance + 1, nx, ny))
            
        return 0

if __name__ == '__main__':
    example1 = AdventDay('example1')
    print('Example Part 1 -', example1.part_one())
    
    input1 = AdventDay('input1')
    print('Input Part 1 -', input1.part_one())
    
    # example2 = AdventDay('example2')
    # print('Example Part 2 -', example2.part_two())
    
    input2 = AdventDay('input2')
    print('Input Part 2 -', input2.part_two())

    # example3 = AdventDay('example3')
    # print('Example Part 3 -', example3.part_three())    

    input3 = AdventDay('input3')
    print('Input Part 3 -', input3.part_three())