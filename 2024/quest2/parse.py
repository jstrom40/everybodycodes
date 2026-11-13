class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        self._process_data()
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().split('\n\n')

    def _process_data(self):
        self.validate_words = self.file[0].split(':')[1].split(',')
        self.sentence = self.file[1].split(' ')
        self.sentences = self.file[1].split('\n')
        
    
    def part_one(self):
        total = 0

        # Option 1 - manual
        for val in self.sentence:
            for word in self.validate_words:
                if word in val:
                    total += 1
        
        return total

    def part_two(self):
        total = 0

        longer_list = set()
        for word in self.validate_words:
            longer_list.add(word[::-1])

        self.validate_words.extend(longer_list)

        for line in self.sentences:
            for word in line.split(' '):
                subtotal = set()
                for v_word in self.validate_words:
                    if v_word in word:
                        for i in range(len(word) - len(v_word) + 1):
                            if word[i:i+len(v_word)] == v_word:
                                subtotal.update(range(i, i+len(v_word)))
                total += len(subtotal)

        return total
    
    def part_three(self):
        total = 0

        longer_list = set()
        for word in self.validate_words:
            longer_list.add(word[::-1])

        self.validate_words.extend(longer_list)
        matches = set()
        for idx,word in enumerate(self.sentences):
            matches.update(self.validate_word(word, idx))
        # matches = sorted(matches)
        

        for i in range(len(self.sentences[0])):
            word = ''
            for j in range(len(self.sentences)):
                word += self.sentences[j][i]
            matches.update(self.validate_word(word,i,True))
        total = len(matches)
        return total

    def validate_word(self, word, idx,up=False):
        n_len = len(word)
        test = word * 2 if not up else word
        submatches = set()
        for v_word in self.validate_words:
            if v_word in test:
                for i in range(len(test) - len(v_word) + 1):
                    if test[i:i+len(v_word)] == v_word:
                        for j in range(i,i+len(v_word)):
                            fixed_j = j % len(word)
                            if up:
                                submatches.add((fixed_j, idx))
                            else:
                                submatches.add((idx, fixed_j))
        return submatches


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