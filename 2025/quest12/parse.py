from collections import deque
class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        self.data = self._process_data()
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        data = [list(map(int, x)) for x in self.file]
        self.move = [(1,0), #D
                     (0,-1),#L
                     (-1,0),#U
                     (0,1)  #R
                     ] 

        return data
    
    def part_one(self):
        total = 0

        barrels = self.data
        row_len = len(barrels)
        col_len = len(barrels[0])

        dq = deque([(0, 0)])
        visited = set()

        while dq:
            x, y = dq.popleft()

            if (x, y) in visited:
                continue
            visited.add((x,y))

            for move_x, move_y in self.move:
                next_x, next_y = move_x + x, move_y + y
                if (next_x in range(row_len) and next_y in range(col_len)):
                    if barrels[x][y] >= barrels[next_x][next_y]:
                        dq.append((next_x, next_y))
                
        total = len(visited)        
        return total

    def part_two(self):
        total = 0

        barrels = self.data
        row_len = len(barrels)
        col_len = len(barrels[0])

        dq = deque([(0, 0)])
        dq.append((row_len-1, col_len-1))
        visited = set()

        while dq:
            x, y = dq.popleft()

            if (x, y) in visited:
                continue
            visited.add((x,y))

            for move_x, move_y in self.move:
                next_x, next_y = move_x + x, move_y + y
                if (next_x in range(row_len) and next_y in range(col_len)):
                    if barrels[x][y] >= barrels[next_x][next_y]:
                        dq.append((next_x, next_y))
                
        total = len(visited)

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
    
    input2 = AdventDay('input2')
    print('Input Part 2 -', input2.part_two())

    # example3 = AdventDay('example3')
    # print('Example Part 3 -', example3.part_three())    

    # input3 = AdventDay('input3')
    # print('Input Part 3 -', input3.part_three())