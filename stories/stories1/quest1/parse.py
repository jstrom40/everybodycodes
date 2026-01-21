class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        self.data = self._process_data()
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        data = []

        for row in self.file:
            row_split = []
            value_split = row.split()
            pair_split = [list(x.split('=')) for x in value_split]
            for left, right in pair_split:
                row_split.append(int(right))
            data.append(row_split)
        # print(data)
        return data
    
    def part_one(self):
        remainders = []

        for row in self.data:
            a_answer = self.eni(row[0], row[3], row[6], 1)
            b_answer = self.eni(row[1], row[4], row[6], 1)
            c_answer = self.eni(row[2], row[5], row[6], 1)
            row_answer = a_answer + b_answer + c_answer
            remainders.append(row_answer)

        answer = max(remainders)
        
        return answer

    def part_two(self):
        remainders = []


        for row in self.data:
            a_answer = self.eni_part2(row[0], row[3], row[6])
            b_answer = self.eni_part2(row[1], row[4], row[6])
            c_answer = self.eni_part2(row[2], row[5], row[6])
            row_answer = a_answer + b_answer + c_answer
            remainders.append(row_answer)

        answer = max(remainders)
        return answer
    
    def part_three(self):
        total = 0

        assert self.eni_part3(2,7,5) == 19
        assert self.eni_part3(3,8,16) == 48

        for row in self.data:
            a_answer = self.eni_part3(row[0], row[3], row[6])
            b_answer = self.eni_part3(row[1], row[4], row[6])
            c_answer = self.eni_part3(row[2], row[5], row[6])
            
            row_answer = a_answer + b_answer + c_answer
            total = max(total, row_answer)

        return total
    
    def eni_part3(self, n, exp, mod):
        score = 0
        for i in range(1, exp+1):
            score += pow(n, i, mod)
            # print(score)
        
        return score

    def eni_part2(self, n, exp, mod):
        remainder = []
        score = 0
        for i in range(5):
            score = pow(n, exp - i, mod)
            remainder.append(score)
        
        answer = int(''.join(str(x) for x in remainder))
        
        return answer
    
    def eni(self, n, exp, mod, score):
        remainder = []
        for _ in range(exp):
            score *= n
            score = score % mod
            remainder.append(score)
        
        remainder = remainder[::-1]
        answer = int(''.join(str(x) for x in remainder))
        
        return answer


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