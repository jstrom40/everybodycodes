class Node:
    def __init__(self, id, plug, left, right):
        self.id = id
        self.plugColor, self.plugType = plug.split()
        self.leftColor, self.leftType = left.split()
        self.rightColor, self.rightType = right.split()
        self.leftBond = None
        self.rightBond = None

        self.leftNode = None
        self.rightNode = None
        

    def insert(self, node, part1 = True, part2 = False, part3 = False):
        if self.leftNode is None:
            if part1:
                if self.leftType == node.plugType and self.leftColor == node.plugColor:
                    self.leftNode = node
                    return True
            else:
                if self.leftType == node.plugType or self.leftColor == node.plugColor:
                    self.leftNode = node
                    return True
        
        if self.leftNode is not None:
            if self.leftNode.insert(node, part2):
                return True
            
        if self.rightNode is None:
            if part1:
                if self.rightType == node.plugType and self.rightColor == node.plugColor:
                    self.rightNode = node
                    return True
            else:
                if self.rightType == node.plugType or self.rightColor == node.plugColor:
                    self.rightNode = node
                    return True
                
        if self.rightNode is not None:
            if self.rightNode.insert(node, part2):
                return True
        return False
    
    def traverse(self):
        output = []
        if self.leftNode:
            output += self.leftNode.traverse()
        output.append(self.id)
        if self.rightNode:
            output += self.rightNode.traverse()
        return output


class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        data = []
        for row in self.file:
            row = row.replace('=', ', ').split(', ')
            data.append((row[1], row[3], row[5], row[7]))
        return data
    
    def part_one(self):
        total = 0

        data = self._process_data()
        
        root = None
        for row in data:
            id, plug, left, right = row
            node = Node(id, plug, left, right)
            if root is None:
                root = node
                continue
            root.insert(node)
        output = root.traverse()

        for index, n in enumerate(output, start=1):
            total += index * int(n)
        
        return total

    def part_two(self):
        total = 0

        data = self._process_data()
        
        root = None
        for row in data:
            id, plug, left, right = row
            node = Node(id, plug, left, right)
            if root is None:
                root = node
                continue
            root.insert(node, False, True)
        output = root.traverse()
        
        for index, n in enumerate(output, start=1):
            total += index * int(n)
        return total
    
    def part_three(self):
        total = 0

        data = self._process_data()
        
        root = None
        for row in data:
            id, plug, left, right = row
            node = Node(id, plug, left, right)
            if root is None:
                root = node
                continue
            root.insert(node, True)

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

    # example3 = AdventDay('example3')
    # print('Example Part 3 -', example3.part_three())    

    # input3 = AdventDay('input3')
    # print('Input Part 3 -', input3.part_three())