class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        self._process_data()
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        self.data = list(int(x) for x in self.file[0].split(','))
    
    def part_one(self):
        total = 0

        num_nails = 32
        mod_nails = num_nails / 2

        for left, right in zip(self.data, self.data[1:]):
            if (left - right) % mod_nails == 0:
                total += 1
        
        return total

    def part_two(self):
        total = 0

        test = []
        ugh = set()

        for left, right in zip(self.data, self.data[1:]):
            test.append((left, right))

        for i in range(len(test)):
            for j in range(i+1):
                x1, y1 = sorted(test[i])
                x2, y2 =  sorted(test[j])
                if (x1 < x2 < y1 < y2) or (x2 < x1 < y2 < y1):
                    ugh.add((x1,y1))
                    total += 1

        return total
    
    def part_three(self):
        total = 0

        test = []
        ugh = {}
        num_nails = 256

        for left, right in zip(self.data, self.data[1:]):
            test.append((left, right))

        for i in range(1, num_nails + 1):
            for j in range(1, num_nails + 1):
                if i != j and ugh.get((j,i)) is None:
                    ugh[(i,j)] = 0
                    for k in range(len(test)):
                        x1, y1 = sorted(test[k])
                        if (x1 < i < y1 < j) or (i < x1 < j < y1):
                            ugh[(i, j)] += 1
        print(ugh)
        max_key = max(ugh, key=ugh.get)
        max_value = ugh[max_key]
        print(max_key, '-', max_value)
                
        return total
    
    def _is_intersect(x, y):
        start = max(x.start, y.start)
        stop = min(x.stop, y.stop)

        if start < stop:
            return range(start, stop)
        return range(0)


if __name__ == '__main__':
    example1 = AdventDay('example1')
    print('Example Part 1 -', example1.part_one())
    
    input1 = AdventDay('input1')
    print('Input Part 1 -', input1.part_one())
    
    example2 = AdventDay('example2')
    print('Example Part 2 -', example2.part_two())
    
    # input2 = AdventDay('input2')
    # print('Input Part 2 -', input2.part_two())

    # example3 = AdventDay('example3')
    # print('Example Part 3 -', example3.part_three())    

    input3 = AdventDay('input3')
    print('Input Part 3 -', input3.part_three())