"""
Name:
Surname:
ID:
"""

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

class PancakeSort(SortingAlgorithm):

    def sort(self):

        """
        Implement the sort method for the Pancake Sort algorithm 
        """
        
        raise NotImplementedError #remove when implementing method


if __name__ == "__main__":

    d = [7, 5, 10, -11 ,3, -4, 99, 1]
    print(d)
    insSorter = PancakeSort(d)
    insSorter.sort()
    print(d)

