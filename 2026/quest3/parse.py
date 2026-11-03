class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        data = [x.split() for x in self.file]
        return data
    
    def part_one(self):
        total = 0

        data = self._process_data()
        for x, y in data:
            x = [int(x) for x in x.replace('ISO-', '')]
            y = [int(y) for y in y]
            n = len(x)
            for i in range(n):
                total += y[i] * (x[i] ** (n - i - 1))
        
        return total

    def part_two(self):
        total = 0

        data = self._process_data()
        for x, y in data:
            x = x.replace('ISO-', '')
            x_len = len(x)
            y_len = len(y)
            if x_len != y_len:
                x = self.fix_iso(x, x_len, y_len)
            x = [int(x) for x in x]
            y = [int(y) for y in y]
            for i in range(y_len):
                total += y[i] * (x[i] ** (y_len - i - 1))

        return total
    
    def part_three(self):
        total = 0

        data = self._process_data()
        data = [[x.split('-')[1], y] for x, y in data]
        
        for base, value in data:
            is_valid = True
            score = self.get_score(base, value)

            for other_values in range(int(value)):
                if self.get_score(base, str(other_values)) == score:
                    # print(other_values)
                    is_valid = False
                    break
            if is_valid:
                # print(score)
                total += score


        return total

    def fix_iso(self, node, x_len, y_len):
        if x_len > y_len:
            # return node % (10 ** y_len)
            return node[-y_len:]
        else:
            flipped = node[::-1]
            new_node = flipped
            for i in range(y_len - x_len):
                new_node += flipped[i % x_len]
            return new_node[::-1]
        
    def get_score(self, base, value):
        base = base[::-1]
        values = value[::-1]
        length = len(base)

        ans = sum(int(base[i%length])**i*int(v) for i,v in enumerate(values))
        return ans


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