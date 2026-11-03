from collections import defaultdict
class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        data = []
        for row in self.file:
            num, values = row.split(':')
            rpg = [int(''.join("1" if c.isupper() else "0" for c in block),2) for block in values.split()]
            
            data.append((num, rpg))
        return data
    
    def part_one(self):
        total = 0

        data = self._process_data()

        # Brute Force Method
        for num, values in data:
            r, g, b = values

            if g > r and g > b:
                total += int(num)
        
        return total

    def part_two(self):
        total = 0

        data = self._process_data()

        min_color = 999999
        max_shine = 0

        for id, values in data:
            r, g, b, s = values
            max_shine = max(max_shine, s)
            if s == max_shine:
                min_color = min(min_color, r + g + b)
            if (r + g + b) == min_color:
                total = id
        for id, values in data:
            r, g, b, s = values
            if s == max_shine:
                print(id, r, g, b, s, r+g+b)
        print(max_shine)

        return total
    
    def part_three(self):
        total = 0

        data = self._process_data()

        groups = defaultdict(int)
        
        for id, values in data:
            r, g, b, s = values
            if 30 < s < 33:
                continue
            if r > g and r > b:
                cat = 'red'
            elif g > r and g > b:
                cat = 'green'
            elif b > r and b > g:
                cat = 'blue'
            if s >= 33:
                cat += '-shiny'
            elif s <= 30:
                cat += '-matte'
            groups[cat] += int(id)
        total = max(groups.values())


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

    input3 = AdventDay('input3')
    print('Input Part 3 -', input3.part_three())