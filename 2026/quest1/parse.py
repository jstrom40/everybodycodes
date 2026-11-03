from math import sqrt, ceil

class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        data = [int(x) for x in self.file[0].split(',')]
        return data
    
    def part_one(self):
        total = 0

        data = self._process_data()
        for x in data:
            root = ceil(sqrt(x))
            total += (root ** 2) - x
        
        return total

    def part_two(self):
        total = 0

        data = self._process_data()

        for x in data:
            root = max(ceil(sqrt(x)), 3)
            area = root ** 2
            perimeter = self.find_perimeter(root)
            while perimeter < x:
                root += 1
                perimeter = self.find_perimeter(root)
            
            total += perimeter  - x

        return total
    
    def part_three(self):
        total = 0

        data = self._process_data()

        for x in data:
            root = ceil(sqrt(x))
            if root % 2 == 0:
                root += 1
            dots = root ** 2 - 1
            while dots < x:
                root += 2
                dots = root ** 2 - 1
            total += (dots - x)

        return total

    def find_perimeter(self, root):
        return (2 * root) + (2 * (root - 2))


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