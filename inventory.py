import fire

class Inventory(object):

    def __init__(self, data=None):
        self.data = None

        if data:
            self.data = data
        else:
            with open("./inventory_input.txt", 'r') as f:
                self.data = map(lambda x: x[:-1], f.readlines())


    def print_data(self):
        print(self.data)
    
if __name__ == "__main__":
    fire.Fire(Inventory(['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']))