from itertools import product, combinations

class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        self._process_data()
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().split('\n\n')

    def _process_data(self):
        self.names = self.file[0].split(',')
        
        validation_list = self.file[1].split('\n')
        self.validation_set = {}
        for row in validation_list:
            row = row.split(' > ')
            validation_letter = row[0]
            comparison = [x for x in row[1].split(',')]
            self.validation_set[validation_letter] = comparison

    
    def part_one(self):
        total = ''
    

        # first attempt
        # for name in self.names:
        #     valid = True
        #     for i in range(len(name)-1):
        #         if name[i + 1] in self.validation_set[name[i]]:
        #             continue
        #         else:
        #             valid = False
        #             break
        #     if valid:
        #        total = name

        # trying with zip
        for name_index, name in enumerate(self.names):
            for left, right in zip(name, name[1:]):
                if right not in self.validation_set.get(left, []):
                    break
            else:
                total = name

        
        return total

    def part_two(self):
        total = 0

        # new way of using start=1 in enumerate
        for name_index, name in enumerate(self.names, start=1):
            if self._is_valid(name):
                total += name_index

        return total
    
    def part_three(self):
        total = 0
        possible = set()
        
        for name in self.names:
            if self._is_valid(name):
                test = self._name_generator_count(name[-1], len(name))
                possible |= self._name_generator(name)

        total = len(possible)
        return total
    
    def _is_valid(self, name):
        for left, right in zip(name, name[1:]):
            if right not in self.validation_set.get(left, []):
                return False
        else:
            return True
    
    def _name_generator_count(self, last, name_len):
        count = 0
        if name_len >= 7:  
            count += 1
        if name_len >= 11: 
            return count
        
        for next in self.validation_set.get(last, []):
            count += self._name_generator_count(next, name_len+1)
        return count
    
    def _name_generator(self, prefix):
        output = set()

        if len(prefix) >= 7: output.add(prefix)
        if len(prefix) == 11: return output

        for next in self.validation_set.get(prefix[-1], []):
            output |= self._name_generator(prefix + next)

        return output




    
        

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