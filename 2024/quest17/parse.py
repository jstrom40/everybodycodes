from heapq import heappush, heappop

class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        stars = []
        for y, rows in enumerate(self.file):
            for x, col in enumerate(rows):
                if col == '*':
                    stars.append((y, x))
        return stars
    
    def part_one(self):
        total = 0

        data = self._process_data()
        total = self.prims(data) + len(data)
        
        return total

    def part_two(self):
        total = 0

        data = self._process_data()
        total = self.prims(data) + len(data)

        return total
    
    def part_three(self):
        total = 0

        return total

    # Prim's algorithm Minimum Spanning Tree (MST) 
    def prims(self,points):
        pq = [(0, points[0])]
        total_dist = 0

        visited = set()

        while pq:
            dist, star = heappop(pq)
            if star in visited:
                continue
            visited.add(star)
            total_dist += dist

            for t in points:
                if t not in visited:
                    heappush(pq, (self.manhattan_dist(star, t), t))
        return total_dist

    def manhattan_dist(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


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

    # input3 = AdventDay('input3')
    # print('Input Part 3 -', input3.part_three())