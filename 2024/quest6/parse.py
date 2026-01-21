from heapq import heappop, heappush
from collections import defaultdict, Counter

class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        self.data = self._process_data()
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        data = []
        self.tree_data = {}

        for row in self.file:
            parent, *children = row.split(':')
            children = children[0].split(',')
            self.tree_data[parent] = children
            for child in children:
                data.append((parent, child))
        

        return data
    
    def part_one(self):
        total = ''

        paths = self.build_tree_v2(self.tree_data, "RR", [])
        optimal_list = []
        for path in paths:
            if path[-1] == '@':
                print(path, len(path))
                optimal_list.append(path)
        
        unique_index = Counter(map(len, optimal_list))

        print(unique_index)

        return total

    def part_two(self):
        total = ''

        paths = self.build_tree(self.tree_data, "RR", [])
        optimal_list = []
        for path in paths:
            if path[-1] == '@':
                optimal_list.append(path)
        
        unique_index = Counter(map(len, optimal_list))
        unique_index, = (k for k,v in unique_index.items() if v == 1)
        
        for path in optimal_list:
            if len(path) == unique_index:
                print(path)
                for word in path:
                    
                    total += word[0]

        return total
    
    def part_three(self):
        total = ''

        paths = self.build_tree(self.tree_data, "RR", [])
        optimal_list = []
        for path in paths:
            if path[-1] == '@':
                optimal_list.append(path)
        
        unique_index = Counter(map(len, optimal_list))
        unique_index, = (k for k,v in unique_index.items() if v == 1)
        
        for path in optimal_list:
            if len(path) == unique_index:
                print(path)
                for word in path:
                    total += word[0]

        return total

    def build_tree(self, tree, node, current_path):
        current_path = current_path + [node]

        children = [child for child in tree.get(node, [])]

        if not children:
            return [current_path]
        
        paths = []
        for child in children:
            new_paths = self.build_tree(tree, child, current_path)
            paths.extend(new_paths)
        
        return paths


if __name__ == '__main__':
    example1 = AdventDay('example1')
    print('Example Part 1 -', example1.part_one())
    
    input1 = AdventDay('input1')
    print('Input Part 1 -', input1.part_one())
    
    # example2 = AdventDay('example2')
    # print('Example Part 2 -', example2.part_two())
    
    input2 = AdventDay('input2')
    print('Input Part 2 -', input2.part_two())

    # example3 = AdventDay('example3')
    # print('Example Part 3 -', example3.part_three())    

    # input3 = AdventDay('input3')
    # print('Input Part 3 -', input3.part_three())