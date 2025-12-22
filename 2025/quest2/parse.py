class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        self.data = self._process_data()
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        data = self.file[0].split('=')[1].strip('[]')
        return data
    
    def part_one(self):
        total = 0

        ax, ay = self.data.split(',')
        ax, ay = int(ax), int(ay)
        
        x, y = 0,0
        iterations = 3

        for _ in range(iterations):
            x, y = self._multiply(x, y, x, y)
            x, y = self._divide(x, y, 10, 10)
            x, y = self._add(x, y, ax, ay)

        # x, y, ax, ay = 0,0,35630,-64830
        # for i in range(100):
        #     x, y = self._multiply(x, y, x, y)
        #     x, y = self._divide(x, y, 100000, 100000)
        #     x, y = self._add(x, y, ax, ay)
        #     if x not in range(-1000000, 1000000) or y not in range(-1000000, 1000000):
        #         print('here', i)
        #         break

        return [x,y]

    def part_two(self):
        total = 0

        ax, ay = self.data.split(',')
        ax, ay = int(ax), int(ay)

        opposite_corner = [ax + 1000, ay + 1000]
        iterations = 100

        for row in range(101):
            for col in range(101):
                # print(row, col)
                x_spot = ax + col * 10
                y_spot = ay + row * 10
                x, y = 0, 0
                valid = True
                for _ in range(iterations):
                    x, y = self._multiply(x, y, x, y)
                    x, y = self._divide(x, y, 100000,100000)
                    x, y = self._add(x, y, x_spot, y_spot)
                    if x not in range(-1000000, 1000000) or y not in range(-1000000, 1000000):
                        valid = False
                        break
                if valid:
                    total += 1 

        return total
    
    def part_three(self):
        total = 0

        ax, ay = self.data.split(',')
        ax, ay = int(ax), int(ay)

        opposite_corner = [ax + 1000, ay + 1000]
        iterations = 100

        for row in range(1001):
            print(row)
            for col in range(1001):
                x_spot = ax + col
                y_spot = ay + row
                x, y = 0, 0
                valid = True
                for _ in range(iterations):
                    x, y = self._multiply(x, y, x, y)
                    x, y = self._divide(x, y, 100000,100000)
                    x, y = self._add(x, y, x_spot, y_spot)
                    if x not in range(-1000000, 1000000) or y not in range(-1000000, 1000000):
                        valid = False
                        break
                if valid:
                    total += 1 

        return total
    
    def _multiply(self, x1, y1, x2, y2):

        x = x1 * x2 - y1 * y2
        y = x1 * y2 + y1 * x2

        return x, y
    
    def _divide(self, x1, y1, x2, y2):

        x = int(x1 / x2)
        y = int(y1 / y2)

        return x, y

    def _add(self, x1, y1, x2, y2):

        x = x1 + x2
        y = y1 + y2

        return x, y

if __name__ == '__main__':
    example1 = AdventDay('example1')
    print('Example Part 1 -', example1.part_one())
    
    example2 = AdventDay('example2')
    print('Example Part 2 -', example2.part_two())
    
    example3 = AdventDay('example3')
    print('Example Part 3 -', example3.part_three())

    input1 = AdventDay('input1')
    print('Input Part 1 -', input1.part_one())

    input2 = AdventDay('input2')
    print('Input Part 2 -', input2.part_two())

    input3 = AdventDay('input3')
    print('Input Part 3 -', input3.part_three())