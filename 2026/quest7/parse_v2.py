from dataclasses import dataclass
from collections import deque
from copy import deepcopy

@dataclass
class Cloud:
    def __init__(self, id, energy, connections):
        self.id = id
        self.energy = int(energy)
        self.connections = connections
        self.exploded = False

class AdventDay:

    def __init__(self, example):
        self.file = self._read_file(example)
        self.is_example = True if 'example' in example else False
        self.data = self._process_data()
    
    def _read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read().splitlines()

    def _process_data(self):
        
        data = {}
        
        for row in self.file:
            row = row.split(', ')
            id = row[0].split('=')[1]
            energy = int(row[1].split('=')[1])
            connections = row[2].split('=')[1].split(',')
            data[id] = Cloud(id, energy, connections)
        return data
    
    def part_one(self):
        total = 0

        starting_id = sorted(self.data.values(), key = lambda x: len(x.connections))[-1].id
        impulse = 5
        # self.propogate(impulse, starting_id)
        # total = sum(v.energy for k, v in self.data.items())

        self.propogate_v2({starting_id: {5: 1}})
        total = sum(v.energy for k, v in self.data.items())

        return total

    def part_two(self):
        
        starting_id = sorted(self.data.values(), key = lambda x: len(x.connections))[-1].id
        impulse = 10
        # self.propogate(impulse, starting_id)

        self.propogate_v2({starting_id: {10: 1}})
        total = sum(v.energy for k, v in self.data.items())

        return total
    
    def part_three(self):
        total = 0

        explosion_limit = 100 if self.is_example else 1000000
        impulse = 10
        original = deepcopy(self.data)
        for x in original.keys():
            self.propogate_v2({x: {10: 1}}, True, explosion_limit)
            sub_total = sum(v.energy for k, v in self.data.items() if not v.exploded)
            total = max(total, sub_total)
            self.data = deepcopy(original)

        return total

    def propogate(self, impulse, starting_id, part3=False, explosion_limit = 0):
        queue = [(impulse,starting_id)]
        
        while queue:
            current_impulse, id = queue.pop()

            if current_impulse == 0:
                continue

            self.data[id].energy += current_impulse

            for cloud in self.data[id].connections:
                queue.append((current_impulse - 1, cloud))
    
    def propogate_v2(self, to_handle, w_explosions = False, explosion_limit = 0):
        exploded = set()
        while to_handle:
            to_handle_next = {}
            for cloud_id, values in to_handle.items():
                if cloud_id in exploded:
                    continue
                for strength, impulse in values.items():
                    self.data[cloud_id].energy += strength * impulse
                for c_id in self.data[cloud_id].connections:
                    if c_id in exploded:
                        continue
                    if c_id not in to_handle_next:
                        to_handle_next[c_id] = {}
                    for strength, impulse in values.items():
                        if strength > 1:
                            to_handle_next[c_id][strength - 1] = to_handle_next[c_id].get(strength - 1, 0) + impulse
                if w_explosions and self.data[cloud_id].energy > explosion_limit:
                    exploded.add(cloud_id)
                    self.data[cloud_id].exploded = True
                    for c_id in self.data[cloud_id].connections:
                        if c_id in exploded:
                            continue
                        if c_id not in to_handle_next:
                            to_handle_next[c_id] = {}
                        to_handle_next[c_id][10] = to_handle_next.get(10,0) + 1

            to_handle = to_handle_next if [k for k, v in to_handle_next.items() if v] else None


    def propogate_p3(self, impulse, starting_id, explosion_limit):
            queue = deque([(1, impulse,starting_id)])
            current_stage = 1

            # explode_list = []
            
            while queue:
                stage, current_impulse, id = queue.popleft()
                if id == '5' and stage == 7:
                    id = id
                if current_stage != stage:
                    # explode_list = [k for k,v in self.data.items() if v.exploded]
                    # print()
                    for k, v in self.data.items():
                        if not v.exploded:
                            if v.energy >= explosion_limit:
                                self.data[k].exploded = True
                                for cloud in self.data[k].connections:
                                    if not self.data[cloud].exploded:
                                        queue.append((stage, impulse, cloud))
                        # print(current_stage, '-', k, '-', v.energy)
                    # print()
                    current_stage += 1
                if current_impulse == 0:
                    continue

                if self.data[id].exploded:
                    continue
    
                self.data[id].energy += current_impulse
    
                # if self.data[id].energy >= explosion_limit:
                #     self.data[id].exploded = True
                #     for cloud in self.data[id].connections:
                #         if cloud not in explode_list:
                #             queue.append((stage + 1, impulse, cloud))
                    # for cloud in self.data[id].connections:
                    #     if self.data[cloud].exploded:
                    #         continue
                    #     else:
                    #         queue.append((stage + 1, impulse, cloud))
                
                # else:
                for cloud in self.data[id].connections:
                    if not self.data[cloud].exploded:
                        queue.append((stage + 1, current_impulse - 1, cloud))


if __name__ == '__main__':
    example1 = AdventDay('example1')
    print('Example Part 1 -', example1.part_one())
    
    input1 = AdventDay('input1')
    print('Input Part 1 -', input1.part_one())
    
    example2 = AdventDay('example2')
    print('Example Part 2 -', example2.part_two())
    
    input2 = AdventDay('input2')
    print('Input Part 2 -',  input2.part_two())

    example3 = AdventDay('example3')
    print('Example Part 3 -', example3.part_three())    

    input3 = AdventDay('input3')
    print('Input Part 3 -', input3.part_three())