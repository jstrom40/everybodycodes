class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        self._process_data()
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        self.data = self.file[0]
        return None
    
    def part_one(self):
        total = 0

        novices = {}
        mentors = {}
        for letter in self.data:
            if letter.isupper():
                if letter in mentors:
                    mentors[letter] += 1
                else:
                    mentors[letter] = 1
            else:
                if letter in novices:
                    novices[letter] += mentors[letter.upper()]
                else:
                    novices[letter] = mentors[letter.upper()]
        
        print(mentors)
        print(novices)

        total = sum(novices.values())

        return total

    def part_two(self):
        total = 0

        novices = {}
        mentors = {}
        for letter in self.data:
            if letter.isupper():
                if letter in mentors:
                    mentors[letter] += 1
                else:
                    mentors[letter] = 1
            else:
                if letter in novices:
                    novices[letter] += mentors[letter.upper()]
                else:
                    novices[letter] = mentors[letter.upper()]

        total = sum(novices.values())

        return total
    
    def part_three(self):
        total = 0

        num_repeats = 1000
        distance_limit = 1000

        tents = self.data * num_repeats

        for letter_index, letter in enumerate(tents):
            
            if not letter.isupper():
                if letter_index < distance_limit:
                    lookup_range = letter_index
                else:
                    lookup_range = distance_limit
                # test = tents[letter_index - lookup_range:letter_index + distance_limit + 1]
                # print(test, len(test), lookup_range, letter_index)
                mentor_check = tents[letter_index - lookup_range:letter_index + distance_limit + 1].count(letter.upper())
                # print(letter, '-', mentor_check)
                total += mentor_check

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