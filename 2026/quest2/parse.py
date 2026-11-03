from collections import defaultdict, deque
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

        for group in data:
            alloys = self.build_edges(group)
            group_total = int(''.join(sorted(alloys, key = lambda k: len(alloys[k]))))
            total += group_total

        return total

    def part_two(self):
        total = 0

        data = self._process_data()
        for group in data:
            alloys = self.build_edges(group)
            total += self.find_group_output(alloys)

        return total
    
    def part_three(self):
        total = 0

        data = self._process_data()
        for group in data:
            alloys = self.build_edges(group)
            total += self.find_group_output(alloys)

        return total

    def build_edges(self, nodes):
        # Automatically initializes any missing keys to blank
        ordered_dict = defaultdict(lambda: set())
        for item in nodes:
            if '<' in item:
                x, y = item.split('<')
            else:
                y, x = item.split('>')
            ordered_dict[x].add(y)
            ordered_dict[y]

        return ordered_dict

    def find_group_output(self, nodes):
        output = ''
        while nodes:
            start = next(iter({x for x,y in nodes.items() if not y}))
            nodes = {x: y-{start} for x,y in nodes.items() if x != start}
            output += start
        return int(output)


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