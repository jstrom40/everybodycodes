from collections import defaultdict, deque

class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        self.file_name = example
        self._process_data()
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        self.num_portals = int(self.file[0].split()[1])

        self.extra = [list(map(int, x.split())) for x in self.file[2:]]
    
    def part_one(self):
        portals = defaultdict(lambda: [])
        for i in range(self.num_portals):
            next_val = (i+1) % self.num_portals
            portals[i].append(next_val)
            portals[next_val].append(i)


        before = self.bfs_portals(portals)

        for x, y in self.extra:
            portals[x - 1].append(y - 1)
            portals[y - 1].append(x - 1)

        after = self.bfs_portals(portals)

        total = before - after
        
        return total

    def part_two(self):
        portals = defaultdict(lambda: [])
        for i in range(self.num_portals):
            for j in range(1,4):
                portals[i].append((i-j) % self.num_portals)
                portals[i].append((i+j) % self.num_portals)

        before = self.bfs_portals(portals)

        for x, y in self.extra:
            portals[x - 1].append(y - 1)
            portals[y - 1].append(x - 1)
        
        after = before
        for i in range(self.num_portals):
            for j in range(i + 1, self.num_portals):
                if j in portals[i]:
                    continue
                portals[i].append(j)
                portals[j].append(i)
                after = min(after, self.bfs_portals(portals))
                del portals[i][-1]
                del portals[j][-1]

        total = before - after

        return total
    
    def part_three(self):
        portals = defaultdict(lambda: [])
        for i in range(self.num_portals):
            for j in range(1,4):
                portals[i].append((i-j) % self.num_portals)
                portals[i].append((i+j) % self.num_portals)

        before = self.bfs_portals(portals)

        for x, y in self.extra:
            portals[x - 1].append(y - 1)
            portals[y - 1].append(x - 1)

        intervals = self.num_portals // 8
        
        points = []
        for i in range(8):
            points.append(i * intervals)

        print(points)

        
        total = before

        return total

    def bfs_portals(self, portals):
        total = 0
        for val in portals.keys():
        
            dq = deque([(0,val)])

            seen = [False] * len(portals)
            while dq:
                dist, key = dq.popleft()
                
                if seen[key]:
                    continue
                total += dist
                seen[key] = True

                for next_key in portals[key]:
                    if seen[next_key]:
                        continue
                    dq.append((dist + 1, next_key))

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

    example3 = AdventDay('example3')
    print('Example Part 3 -', example3.part_three())    

    # input3 = AdventDay('input3')
    # print('Input Part 3 -', input3.part_three())