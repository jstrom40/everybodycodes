class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        data = [x.split('=') for x in self.file]

        beacons = {}
        
        for row in self.file:
            var, output = row.split('=')
            if var == 'MOVES':
                moves = output
            else:
                output = tuple(map(int, output.strip('[]').split(',')))
                if var == 'START':
                    start = output
                else:
                    beacons[var] = output




        return start, beacons, moves
    
    def part_one(self):
        total = 0

        start, beacons, moves = self._process_data()
        visited = set()
        visited.add(start)

        cx, cy = start

        for beacon in moves:
            end = beacons[beacon]
            hx, hy = self.find_halfway((cx, cy), end)
            cx, cy = int(cx + hx), int(cy + hy)
            visited.add((cx, cy))
            
        
        return len(visited)

    def part_two(self):
        total = 0

        start, beacons, moves = self._process_data()
        visited = []
        visited.append(start)

        cx, cy = start
        fireflies = set()

        for beacon in moves:
            end = beacons[beacon]
            hx, hy = self.find_halfway((cx, cy), end)
            cx, cy = int(cx + hx), int(cy + hy)
            if (cx, cy) not in visited:
                visited.append((cx, cy))

        self.pprint(visited)

        for points in visited:
            x, y = points
            for dx, dy in ((-1,0), (1,0), (0, 1), (0,-1)):
                nx, ny = x + dx, y + dy
                if (nx, ny) in visited:
                    continue
                else:
                    fireflies.add((nx, ny))
        

        return len(set(fireflies))
    
    def part_three(self):
        total = 0

        return total
    
    def find_halfway(self, start, end):
        x, y = start
        nx, ny = end

        return (((nx - x) / 2), ((ny - y) / 2))

    def pprint(self, data: set) -> None:
        min_x = min(d[0] for d in data)
        max_x = max(d[0] for d in data)
        min_y = min(d[1] for d in data)
        max_y = max(d[1] for d in data)
        print(min_x, max_x, min_y, max_y)
        for y in range(max_y + 1, min_y - 2, -1):
            print(
                "".join("#" if (x, y) in data else "." for x in range(min_x - 1, max_x + 2))
            )
        print()


if __name__ == '__main__':
    example1 = AdventDay('example1')
    print('Example Part 1 -', example1.part_one())
    
    input1 = AdventDay('input1')
    print('Input Part 1 -', input1.part_one())
    
    example2 = AdventDay('example2')
    print('Example Part 2 -', example2.part_two())
    
    # input2 = AdventDay('input2')
    # print('Input Part 2 -', input2.part_two())

    example3 = AdventDay('example3')
    print('Example Part 3 -', example3.part_three())    

    # input3 = AdventDay('input3')
    # print('Input Part 3 -', input3.part_three())