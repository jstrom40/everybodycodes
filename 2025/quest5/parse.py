class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        self._process_data()
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        data = self.file[0].split(':')
        self.identifer = int(data[0])
        self.numbers = [int(x) for x in data[1].split(',')]

        print()
        
        return None
    
    def part_one(self):
        total = ''

        fishbone = self._create_fishbone(self.numbers)

        for row in fishbone:
            total += str(row[1])

        
        return total

    def part_two(self):
        total = 0
        market = []

        for row in self.file:
            data = row.split(':')
            identifer = int(data[0])
            numbers = [int(x) for x in data[1].split(',')]
            fishbone = self._create_fishbone(numbers)
            fish_total = ''
            for bone in fishbone:
                fish_total += str(bone[1])
            market.append(int(fish_total))

        total = max(market) - min(market)

        return total
    
    def part_three(self):
        total = 0
        market = []

        for row in self.file:
            data = row.split(':')
            identifer = int(data[0])
            numbers = [int(x) for x in data[1].split(',')]
            fishbone = self._create_fishbone(numbers)
            fish_total = ''
            for bone in fishbone:
                fish_total += str(bone[1])
            market.append((int(fish_total), fishbone, identifer))
        
        market.sort(reverse=True)
        print(market)
        for row_index, row in enumerate(market):
            print(row_index, row[2])
            total += (row_index + 1) * row[2]
        
        # for i in range(len(market) - 1):
        #     if market[i][0] == market[i+1][0]:
        #         for j in range(len(market[i][1])):
        #             left_bone = int("".join(map(str, market[i][1][j])))
        #             right_bone = int("".join(map(str, market[i+1][1][j])))
        #             if left_bone == right_bone:
        #                 continue
        #             elif left_bone < right_bone:
        #                 break
        #             elif left_bone > right_bone:
        #                 temp_market = market[i]
        #                 market[i] = market[i+1]
        #                 market[i+1] = temp_market
        #                 break
        #     else:
        #         continue
            

        return total
    
    def _create_fishbone(self, numbers):
        fishbone = [[0,0,0]]

        for index, num in enumerate(numbers):
            for bone_index, bone in enumerate(fishbone):
                if bone[1] == 0:
                    fishbone[bone_index][1] = num
                    break
                elif bone[0] == 0 and bone[1] > num:
                    fishbone[bone_index][0] = num
                    break
                elif bone[2] == 0 and bone[1] < num:
                    fishbone[bone_index][2] = num
                    break
                elif bone_index+1 == len(fishbone):
                    fishbone.append([0,0,0])
                else:
                    continue
        return fishbone



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