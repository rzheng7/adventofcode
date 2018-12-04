
import fire

class frequency(object):
    
    def __init__(self, frequency=None):
        lines = None
        if frequency:
            self.frequencies = frequency
        else:
            with open("./frequency_input.txt", 'r') as f:
                lines = f.readlines()
            self.frequencies =  map(int, lines)

    def total(self):
        # https://adventofcode.com/2018/day/1#part1

        print(sum(self.frequencies))

    def first_frequency_reached_twice(self):
        # https://adventofcode.com/2018/day/1#part2
        total_list = set([0]) 

        total = 0
        while True:
            for line in self.frequencies:
                total += line
                if total in total_list:
                    print ("{} {} {}".format("*"*10, total, "*"*10))
                    return
            
                total_list.add(total)

if __name__ == "__main__":
    
    fire.Fire(frequency([+3, +3, +4, -2, -4]))    
    fire.Fire(frequency([-6, +3, +8, +5, -6]))    
    fire.Fire(frequency([+7, +7, -2, -7, -4]))    
    fire.Fire(frequency())    