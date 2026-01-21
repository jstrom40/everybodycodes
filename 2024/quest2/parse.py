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

        for line in self.sentences:
            subtotal = 0
            for word in line.split(' '):
                for v_word in self.validate_words:
                    word_count = self.count_occurrences(word, v_word)
                    subtotal += word_count
                    if word_count > 0:
                        print(word, v_word, word_count)
                    
            print(line, subtotal)
            total += subtotal



        return total
    
    def part_three(self):
        total = 0

        return total
    
    def count_occurrences(self, word, validation_word):
        total = 0
        validation_len = len(validation_word)
        word_len = len(word)
        word_reversed = word[::-1]
        if validation_len > word_len:
            return 0
        for i in range(word_len - validation_len + 1):
            if validation_word == word[0+i:i+validation_len]:
                total += validation_len
            if validation_word == word_reversed[0+i:i+validation_len]:
                total += validation_len
        return total



if __name__ == '__main__':
    example1 = AdventDay('example1')
    print('Example Part 1 -', example1.part_one())
    
    input1 = AdventDay('input1')
    print('Input Part 1 -', input1.part_one())
    
    example2 = AdventDay('example2')
    print('Example Part 2 -', example2.part_two())
    
    # input2 = AdventDay('input2')
    # print('Input Part 2 -', input2.part_two())

    # example3 = AdventDay('example3')
    # print('Example Part 3 -', example3.part_three())    

    # input3 = AdventDay('input3')
    # print('Input Part 3 -', input3.part_three())