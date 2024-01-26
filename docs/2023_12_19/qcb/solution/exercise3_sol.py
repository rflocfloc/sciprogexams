"""
Name:
Surname:
ID:
"""

import random

class SortingAlgorithm:
    def __init__(self, data, verbose = True):
        self.data = data
        self.comparisons = 0
        self.operations = 0
        self.verbose = verbose

    def getData(self):
        return self.data

    def getOperations(self):
        return self.operations

    def getComparisons(self):
        return self.comparisons

    def sort(self):
        raise NotImplementedError

class pancakeSort(SortingAlgorithm):

    def flip(self, i):
        self.data[:i+1] = reversed(self.data[:i+1])

    def max_index(self, max_pankcake):
        cur_max = 0
        for i in range(1,max_pankcake+1):
            if self.data[i] > self.data[cur_max]:
                cur_max = i
        return cur_max

    def sort(self):

        """
        Implement the Pancake Sort algorithm 
        """
        
        
        n = len(self.data)-1

        for big_flip in range(n, 0, -1):

            # Find the index of the maximum element in self.data[0..curr_size-1]
            mi = self.max_index(big_flip)

            # Move the maximum element to end of current self.dataay if it's not already there
            # Flip the self.data from 0 to max element index
            self.flip(mi)
            # Flip the whole self.data
            self.flip(big_flip)

        return self.data


if __name__ == "__main__":

    d = [7, 5, 10, -11 ,3, -4, 99, 1]
    print(d)
    insSorter = pancakeSort(d)
    insSorter.sort()
    print(d)

