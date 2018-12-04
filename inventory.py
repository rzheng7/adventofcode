import fire

class Inventory(object):

    def __init__(self, data=None):
        self.data = None
        self.count_2 = 0
        self.count_3 = 0

        if data:
            self.data = data
        else:
            with open("./inventory_input.txt", 'r') as f:
                self.data = map(lambda x: x[:-1], f.readlines())

    def count(self, s):
        
        cc = [0, 0] 
        for c in set(s):
            if s.count(c) == 2:
                cc[0] = 1
            if s.count(c) == 3:
                cc[1] = 1
        
        print("{}, 2={}, 3={}".format(s, *cc))
        
        self.count_2 += cc[0]
        self.count_3 += cc[1]

    def print_data(self):
        print(self.data)


    def check_sum(self):
        # part 1
        map(self.count, self.data )

        print(self.count_2 * self.count_3)
    
if __name__ == "__main__":
    fire.Fire(Inventory(['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']))
    fire.Fire(Inventory())