from collections import defaultdict

class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().split('\n\n')

    def _process_data(self):
        data = []

        for row in self.file[0].split('\n'):
            parsing = row.split(':')
            data.append((parsing[0], parsing[1].split(',')))

        track_file = self.file[1].split('\n')
        # print(track_file, len(track_file))
        track = []
        track.extend(track_file[0])
        for i in range(2):
            for j in range(1, len(track_file)-1):
                row = track_file[j].split()
                if i == 0:
                    track.extend(row[1])
                else:
                    track.extend(row[0])
            if i == 0:
                track.extend(track_file[-1][::-1])
        track.pop(0)
        track.append('S')
        
        self.mappings = {
            "+": 1,
            "-": -1,
            "=": 0
        }
        
        return data, track
    
    def part_one(self):
        total = ''

        action_plan, track = self._process_data()

        devices = []
        for actions in action_plan:
            power = 10
            row_total = 0
            i = 0
            while i < 10:
                action = actions[1][i % len(actions[1])]
                power += self.mappings[action]
                row_total += power
                i += 1
            devices.append((row_total, actions[0]))
    
        for row in sorted(devices):
            total += row[1]
        
        return total[::-1]

    def part_two(self):
        total = ''

        action_plan, track = self._process_data()

        devices = defaultdict(int)

        
        for actions in action_plan:
            power = 10
            for i in range(len(track) * 10):
                track_action = track[i % len(track)]
                if track_action in ('+', '-'):
                    action = track_action
                else:
                    action = actions[1][i % len(actions[1])]
                
                power += self.mappings[action]
                devices[actions[0]] += power

        
        devices = dict(sorted(devices.items(),reverse=True, key=lambda x: x[1]))
        print(devices)
        for k in devices.keys():
            total += k

        return total
    
    def part_three(self):
        total = 0

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