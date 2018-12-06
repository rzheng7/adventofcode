import pytest
from array import array
from pprint import pprint

class Claim(object):

    def __init__(self, data=None):

        self.map = []
        if data:
            self.lines = data
        else:
            with open("./day3.txt", 'r') as f:
                self.lines = f.readlines()

        self.max_edge = array('i', [0,0])
        self.max_rect = array('i', [0,0])
        for line in self.lines:
            clm_id = int(line.split("@")[0].strip("#"))
            clm_edge = list(map(int, line.split("@")[1].split(":")[0].split(",")))
            clm_rect = list(map(int, line.split("@")[1].split(":")[1].split("x")))
            self.map.append([clm_id, clm_edge, clm_rect])

            if clm_edge[0] > self.max_edge[0]:
                self.max_edge[0] = clm_edge[1]
            if clm_edge[1] > self.max_edge[1]:
                self.max_edge[1] = clm_edge[1]

            if clm_rect[0] > self.max_rect[0]:
                self.max_rect[0] = clm_rect[0]
            if clm_rect[1] > self.max_rect[1]:
                self.max_rect[1] = clm_rect[1]


    def print_data(self):
        for k,v in enumerate(self.lines):
            print("line {}: {}".format(k,v))

        for i in self.map:
            print(i)

    def populate_map(self):
        col =  self.max_rect[0] + self.max_edge[0]
        row =  self.max_rect[1] + self.max_edge[1]

        claim_map = [[0]*col for i in range(row)]
        for i in self.map:
            start_col, start_row = i[1]
            clm_width, clm_height  = i[2]
            for j in range(start_col, start_col+clm_width):
                for k in range(start_row, start_row+clm_height):

                    if claim_map[k][j] == 0:
                        claim_map[k][j] = 1
                    else:
                        claim_map[k][j] = 2

        sum = 0
        for i in range(col):
            sum += claim_map[i].count(2)

        print(sum)

    def overlap_map(self):
        col =  self.max_rect[0] + self.max_edge[0]
        row =  self.max_rect[1] + self.max_edge[1]

        claim_map = [[0]*col for i in range(row)]
        for i in self.map:
            start_col, start_row = i[1]
            clm_width, clm_height  = i[2]
            for j in range(start_col, start_col+clm_width):
                for k in range(start_row, start_row+clm_height):
                        claim_map[k][j] += 1

        done = False
        for i in self.map:
            tmp=[]
            start_col, start_row = i[1]
            clm_width, clm_height  = i[2]
            for j in range(start_col, start_col+clm_width):
                for k in range(start_row, start_row+clm_height):
                    tmp.append(claim_map[k][j])
            if all(map(lambda x: x == 1, tmp)):
                print(i[0])



def test_read_file():
    data = \
["#1 @ 1,3: 4x4",
"#2 @ 3,1: 4x4",
"#3 @ 5,5: 2x2"]


    # clm = Claim(data)
    clm = Claim()
    # clm.populate_map()
    clm.overlap_map()



