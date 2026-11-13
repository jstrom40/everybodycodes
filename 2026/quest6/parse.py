from collections import defaultdict

class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        self.data = defaultdict(lambda: '')
        for row in self.file:
            row = row.split(':')
            parent = row[0]
            children = row[1].split(',')

            self.data[parent] = children
    
    def part_one(self):
        total = 0

        self._process_data()

        queue = ['NULL']
        visited = set()

        while queue:
            node = queue.pop()

            children = self.data[node]

            for child in children:
                if child == 'NULL' or child in visited:
                    continue
                visited.add(child)
                queue.append(child)
        total = len(visited)
        
        return total

    def part_two(self):
        total = 0

        self._process_data()

        total = len(self.dfs('NULL')) - 1
        return total
    
    def part_three(self):

        data = self._process_data()
        answer = set()

        null_1 = self.dfs('NULLv1')
        null_2 = self.dfs('NULLv2')
        null_3 = self.dfs('NULLv3')


        answer.update(null_1 & null_2)
        answer.update(null_2 & null_3)
        answer.update(null_1 & null_3)

        return len(answer)

    def dfs(self, start):
        queue = [start]
        visited = set()

        while queue:
            item = queue.pop()

            if item in visited:
                continue
            visited.add(item)

            for k, v in self.data.items():
                if item in v:
                    queue.append(k)
        return visited
    
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