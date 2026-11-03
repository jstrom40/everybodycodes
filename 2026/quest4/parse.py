from collections import Counter, defaultdict
class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        data = [[int(x.split('=')[1]) for x in line.split()] for line in self.file]
        
        return data
    
    def part_one(self):
        total = 0

        data = self._process_data()
        # participant_times = Counter()
        participant_times = defaultdict(lambda: 0)
        

        for id, quest, part, time in data:
            participant_times[id] += time
        
        participant_times = sorted(participant_times.values())

        total = sum(i * t for i, t in enumerate(participant_times, 1))

        
        # participant_times = sorted(participant_times.items(), key=lambda item:item[1])
        # for place, (id, time) in enumerate(participant_times):
        #     total += (place+1) * time
        return total

    def part_two(self):
        total = 0
        data = self._process_data()

        participant_times = defaultdict(lambda: [0, 0])

        for id, quest, part, time in data:
            participant_times[id][0] -= 1
            participant_times[id][1] += time
        participant_times = sorted(participant_times.values())

        total = sum(idx * time for idx, (quest, time) in enumerate(participant_times, 1))
        return total
    
    def part_three(self):
        total = 0

        data = self._process_data()
        data = sorted(data)

        participant_dict = defaultdict(lambda: defaultdict(lambda: 0))

        for id, quest, part, time in data:
            if part == 1:
                participant_dict[(quest, part)][id] = time
            else:
                participant_dict[(quest, part)][id] = time+participant_dict[(quest, part - 1)][id]
        scores = defaultdict(lambda: 0)

        for (quest, part), times in participant_dict.items():
            times = times.items()
            times = sorted(times, key=lambda x:x[1])
            # print(quest, part, times) 
            for idx, (k, v) in enumerate(times):
                if idx == 0 or v != times[idx - 1][1]:
                    temp_score = max(50*part-idx,0)
                else:
                    pass
                scores[k] += temp_score

        scores = sorted(scores.values(), reverse=True)
        for i, score in enumerate(scores):
            if i == 0 or score != scores[i - 1]:
                multi = i + 1
            else:
                pass
            total += multi * score

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