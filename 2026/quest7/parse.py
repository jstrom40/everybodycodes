from collections import defaultdict

class Cloud:
    def __init__(self, id, energy, connections):
        self.id = id
        self.energy = int(energy)
        self.connections = connections

class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        self.data = self._process_data()
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        
        data = defaultdict(dict)
        
        for row in self.file:
            row = row.split(', ')
            id = row[0].split('=')[1]
            energy = int(row[1].split('=')[1])
            connections = row[2].split('=')[1].split(',')
            # cloud = Cloud(id, energy, connections)
            data[id]['connections'] = connections
            data[id]['energy'] = energy
        return data
    
    def part_one(self):
        total = 0
        

        starting_id = max(self.data, key = lambda i: len(self.data[i]['connections']))
        impulse = 5
        self.dfs(impulse, starting_id)
        
        total = sum(v['energy'] for k, v in self.data.items())

        return total

    def part_two(self):
        
        starting_id = max(self.data, key = lambda i: len(self.data[i]['connections']))
        impulse = 10

        self.dfs(impulse, starting_id)

        total = sum(v['energy'] for k, v in self.data.items())

        return total
    
    def part_three(self):
        total = 0

        return total

    def dfs(self, impulse, starting_id):
        queue = [(impulse,starting_id)]
        
        while queue:
            impulse, id = queue.pop()

            if impulse == 0:
                continue

            self.data[id]['energy'] += impulse

            for cloud in self.data[id]['connections']:
                queue.append((impulse - 1, cloud))


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