class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        data = [list(map(int, x.split(','))) for x in self.file]
        return data
    
    def part_one(self):
        total = 0

        data = self._process_data()
        for row in data:
            total += self.calc(row, False)
        
        return total

    def part_two(self):
        total = 0


        data = self._process_data()

        for row in data:
            total += self.calc(row, True)

        return total
    
    def part_three(self):
        total = 0

        data = self._process_data()
        
        for row in data:
            total += self.calc(row, True)

        return total

    def calc(self, points, unique):
        current_point = 0
        visited = set()
        visited.add(0)
        for x in points:
            next_point = current_point - x
            if next_point in visited or next_point < 0:
                current_point += x
                while unique and current_point in visited:
                    current_point += 1
            else:
                current_point -= x
            visited.add(current_point)
        return current_point


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