import fire
from collections import Counter

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


    def count2(self, s):
        
        if 2 in Counter(s).values():
            self.count_2 += 1 
        if 3 in Counter(s).values():
            self.count_3 += 1

    def print_data(self):
        print(self.data)


    def check_sum(self):
        # part 1
        map(self.count2, self.data )

        print(self.count_2 * self.count_3)


    def common_between_two_boxes(self):
        # day 2 part II
        max_common_letters = None
        for k,v in enumerate(self.data):
            for i in self.data[k+1:]:
                common_num = 0
                common_letters = []
                for indx in range(len(v)):
                    if i[indx] == v[indx]:
                        common_num += 1
                        common_letters.append(i[indx])

                if not max_common_letters or len(max_common_letters) < common_num: 
                    max_common_letters = common_letters

        print("".join(max_common_letters))
    
if __name__ == "__main__":
    # fire.Fire(Inventory(['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']))

    # fire.Fire(Inventory(['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']))
    fire.Fire(Inventory())