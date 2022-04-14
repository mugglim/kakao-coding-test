import sys
sys.setrecursionlimit(10**6)


class DisjointSet:
    def __init__(self, size):
        self.size = size
        self.parents = {}

    def find(self, room_number):
        if room_number not in self.parents:
            self.parents[room_number] = room_number + 1
            return room_number

        self.parents[room_number] = self.find(self.parents[room_number])
        return self.parents[room_number]


def solution(k, room_number):
    ds = DisjointSet(k)
    return [ds.find(x) for x in room_number]
