import pytest
from pprint import pprint
import re
class Schedule(object):

    def __init__(self, data=None):
        self.data = None
        self.guards = dict()
        if data:
            self.data = data.split("\n")
        else:
            with open("./day4.txt", 'r') as f:
                self.data = f.readlines()

        self.data = sorted(self.data)

    def print_data(self):
        for i in self.data:
            pprint(i)

    def parse_blocks(self):

        guard_num = 0
        wake_ups = 0
        sleeps = []
        falls_asleep = 0
        for line in self.data:

            if "Guard" in line:
                if guard_num != 0:
                    if guard_num not in self.guards.keys():
                        # import pdb
                        # pdb.set_trace()
                        self.guards[guard_num] = []
                    self.guards[guard_num].append({'date': date, 'sleeps': sleeps})

                guard_num = int(re.search(r"#(\d*)", line).groups()[0])
                sleeps = []
                date = re.search(r'\d{4}-(\d{2}-\d{2})', line).groups()[0]

            if "falls asleep" in line:
                sleep = int(re.search(r":(\d*)]", line).groups()[0])
            if "wakes up" in line:
                wake_up = int(re.search(r":(\d*)]", line).groups()[0])
                sleeps.append((sleep, wake_up))
                sleep = 0
                wake_up = 0

        self.guards[guard_num].append({'date': date, 'sleeps': sleeps})

        # pprint(self.guards)

    def most_minutes_asleep(self):
        max_guard = 0
        max_min = 0
        mins = [0] * 60
        max_sleep = 0
        total_sleep = 0
        for guard, duties in self.guards.items():
            pprint("Guard = {}".format (guard))
            for duty in duties:
                for sleep in duty['sleeps']:
                    total_sleep += sleep[1] - sleep[0]
                    for i in range(sleep[0], sleep[1]):
                         mins[i] += 1

            print(mins)
            print("total sleep time: {}".format(total_sleep))
            if max_sleep < total_sleep:
                max_guard = guard
                max_sleep = total_sleep
                max_min = mins.index(max(mins))
            mins = [0] * 60
            total_sleep = 0

        print()

        print("guard: {} min: {} total: {}".format(max_guard, max_min, max_guard * max_min))


    def a_minute_asleep_the_most(self):
        max_guard = 0
        max_min = 0
        mins = [0] * 60
        max_sleep = 0
        total_sleep = 0
        for guard, duties in self.guards.items():
            pprint("Guard = {}".format (guard))
            for duty in duties:
                for sleep in duty['sleeps']:
                    pprint(sleep)
                    total_sleep += sleep[1] - sleep[0]
                    for i in range(sleep[0], sleep[1]):
                         mins[i] += 1

            print(mins)
            print("total sleep time: {}".format(total_sleep))
            if max_sleep < max(mins):
                max_guard = guard
                max_sleep = max(mins)
                max_min = mins.index(max_sleep)
            mins = [0] * 60
            total_sleep = 0

        print()

        print("guard: {} min: {} total: {}".format(max_guard, max_min, max_guard * max_min))


# def test_schedule():
# sch = Schedule("""
# [1518-11-01 00:00] Guard #10 begins shift
# [1518-11-01 00:05] falls asleep
# [1518-11-01 00:25] wakes up
# [1518-11-01 00:30] falls asleep
# [1518-11-01 00:55] wakes up
# [1518-11-01 23:58] Guard #99 begins shift
# [1518-11-02 00:40] falls asleep
# [1518-11-02 00:50] wakes up
# [1518-11-03 00:05] Guard #10 begins shift
# [1518-11-03 00:24] falls asleep
# [1518-11-03 00:29] wakes up
# [1518-11-04 00:02] Guard #99 begins shift
# [1518-11-04 00:36] falls asleep
# [1518-11-04 00:46] wakes up
# [1518-11-05 00:03] Guard #99 begins shift
# [1518-11-05 00:45] falls asleep
# [1518-11-05 00:55] wakes up
#     """)
sch = Schedule()
# sch.print_data()
sch.parse_blocks()
sch.print_data()
sch.a_minute_asleep_the_most()





