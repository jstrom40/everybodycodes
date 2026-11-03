class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().split('\n\n')

    def _process_data(self):
        self.grid = [list(x) for x in self.file[0].splitlines()]
        rules = [list(x) for x in self.file[1].splitlines()]

        self.mappings = {
            "R": (0,1),
            "L": (0,-1)
        }
        
        return rules
    
    def part_one(self):
        total = 0

        rules = self._process_data()
        i = 0
        for index, row in enumerate(rules):
            toss_slot = index + 1
            final_slot = self.traverse_board(row, i)
            i += 2
            coins = (final_slot * 2) - toss_slot
            if coins > 0:
                total += coins
        
        return total

    def part_two(self):
        total = 0
        rules = self._process_data()
        
        for row in rules:
            greedy_coins = 0
            for slot in range(1, len(self.grid[0]) // 2 + 2):
                rules_copy = row[:]
                toss_slot = slot * 2 - 2
                final_slot = self.traverse_board(rules_copy, toss_slot)
                coins = (final_slot * 2) - slot
                greedy_coins = max(greedy_coins, coins)
            total += greedy_coins

        return total
    
    def part_three(self):
        total = 0

        rules = self._process_data()
        
        needy_coins = 999999
        greedy_coins = 0

        for row in rules:
            for slot in range(1, len(self.grid[0]) // 2 + 2):
                rules_copy = row[:]
                toss_slot = slot * 2 - 2
                final_slot = self.traverse_board(rules_copy, toss_slot)
                coins = (final_slot * 2) - slot
                if coins > 0:
                    needy_coins = min(needy_coins, coins)
                greedy_coins = max(greedy_coins, coins)
            total += greedy_coins
        print(needy_coins, greedy_coins)
        
        total = ' '.join(map(str, [needy_coins, greedy_coins]))

        return total
    
    def traverse_board(self, rules, pos):
        col = pos
        for row in self.grid:
            
            if row[col] == '.':
                continue
            dir = rules.pop(0)
            if col == 0:
                col += 1
            elif col == len(row) - 1:
                col -= 1
            else:
                if dir == 'L':
                    col -= 1
                else:
                    col += 1
        return col // 2 + 1


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

    # input3 = AdventDay('input3')
    # print('Input Part 3 -', input3.part_three())