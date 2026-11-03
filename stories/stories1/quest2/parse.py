from collections import Counter
class Node:
    def __init__(self, id, rank, symbol):
        self.id = id
        self.nodeRank = rank
        self.nodeSymbol = symbol
        self.leftNode = None
        self.rightNode = None
    
    def insert(self, node):
        if self.nodeRank < node.nodeRank:
            if self.rightNode is None:
                self.rightNode = node
                return True
            if self.rightNode is not None:
                if self.rightNode.insert(node):
                    return True
        if self.nodeRank > node.nodeRank:
            if self.leftNode is None:
                self.leftNode = node
                return True
            if self.leftNode is not None:
                if self.leftNode.insert(node):
                    return True
        return False
    
    def swap(self, node_l, node_r):
        if self.id == node_l.id:
            self.nodeRank = node_r.nodeRank
            self.nodeSymbol = node_r.nodeSymbol
        
        if self.leftNode:
            if self.leftNode.swap(node_l, node_r):
                return True

        if self.rightNode:
            if self.rightNode.swap(node_l, node_r):
                return True
        
        return False
    
    
    def define_levels(self, level, res):
        if len(res) <= level:
            res.append([])
        res[level].append(self.nodeSymbol)

        if self.leftNode:
            self.leftNode.define_levels(level + 1, res)

        if self.rightNode:
            self.rightNode.define_levels(level + 1, res)
        return res
            

class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data_part_one(self):
        data = []
        for row in self.file:
            row = row.replace('=',' ').split()
            id = row[2]
            left_a,left_s = row[4].strip('[]').split(',')
            right_a,right_s = row[6].strip('[]').split(',')
            data.append((id, int(left_a), left_s, int(right_a), right_s))
            
        return data
    
    def _process_data_part_two(self):
        data = {}
        dir = []
        for row in self.file:
            row = row.replace('=',' ').split()
            if len(row) == 2:
                command = row[0]
                id = row[1]
                dir.append((command, id))
                continue
            else:
                command = row[0]
                id = row[2]
                left_a,left_s = row[4].strip('[]').split(',')
                right_a,right_s = row[6].strip('[]').split(',')
                data[id] = (int(left_a), left_s, int(right_a), right_s)
                dir.append((command, id))
        return dir, data
    
    def part_one(self):

        data = self._process_data_part_one()
        # print(data)
        root_l = None
        root_r = None
        for index, row in enumerate(data):
            id, left_a, left_s, right_a, right_s = row
            
            if root_l is None:
                root_l = Node(id, left_a, left_s)
            if root_r is None:
                root_r = Node(id, right_a, right_s)
            if index == 0:
                continue
            node_l = Node(id, left_a, left_s)
            node_r = Node(id, right_a, right_s)
            
            root_l.insert(node_l)
            root_r.insert(node_r)
        
        output_l = ''.join(max(root_l.define_levels(0,[]), key=len))
        output_r = ''.join(max(root_r.define_levels(0,[]), key=len))


        total = output_l + output_r
        
        return total

    def part_two(self):
        total = 0

        dir, data = self._process_data_part_two()

        root_l = None
        root_r = None
        for index, row in enumerate(dir):
            command, id = row
            left_a, left_s, right_a, right_s = data.get(id)
            node_l = Node(id, left_a, left_s)
            node_r = Node(id, right_a, right_s)

            if command == 'ADD':
                if root_l is None:
                    root_l = Node(id, left_a, left_s)
                if root_r is None:
                    root_r = Node(id, right_a, right_s)
                if index == 0:
                    continue
                
                root_l.insert(node_l)
                root_r.insert(node_r)
            else:
                root_l.swap(node_l, node_r)
                root_r.swap(node_r, node_l)
                data[id] = (right_a, right_s, left_a, left_s)
        output_l = ''.join(max(root_l.define_levels(0,[]), key=len))
        output_r = ''.join(max(root_r.define_levels(0,[]), key=len))

        total = output_l + output_r

        return total
    
    def part_three(self):
        total = 0

        return total

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