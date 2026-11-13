from itertools import count

class AdventDay:

    def __init__(self, example):
        self.is_example = True if 'example' in example else False
    
    def part_one(self):
        num_blocks = 13 if self.is_example else 4099454

        num_levels = 1
        current_blocks = 1
        while current_blocks < num_blocks:
            num_levels += 1
            width = num_levels * 2 - 1
            current_blocks += width
        total = width * (current_blocks - num_blocks) 
        
        return total

    def part_two(self):
        total = 0
        priests = 3 if self.is_example else 867
        acolytes = 5 if self.is_example else 1111
        available_blocks = 50 if self.is_example else 20240000

        level = 1
        width = 1
        current_blocks = 1
        while current_blocks < available_blocks:
            level = (level * priests) % acolytes
            width += 2
            current_blocks += width * level

        total = width * (current_blocks - available_blocks)

        return total
    
    def part_three(self):
        total = 0
        priests = 2 if self.is_example else 900027
        acolytes = 5 if self.is_example else 10
        available_blocks = 160 if self.is_example else 202400000

        thickness = 1
        width = 1
        current_blocks = 1
        heights = [1]
        while current_blocks < available_blocks:
            thickness = (thickness * priests) % acolytes + acolytes
            width += 2
            heights.insert(0,0)
            heights.append(0)
            for i in range(len(heights)):
                heights[i] += thickness
            num_blocks = sum(heights)
            for i in range(1, len(heights) - 1):
                removed = (priests * width * heights[i]) % acolytes
                num_blocks -= removed
            current_blocks = num_blocks

        total = current_blocks - available_blocks

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