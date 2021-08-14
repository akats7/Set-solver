import random, collections
class Solution:

    def __init__(self,data):
        self.input = data
        self.numsCount = collections.defaultdict(int)
    
    def findSets(self):

        self.countsPerRow = []
        for row in self.input:
            for el in row:
                self.numsCount[el] += 1

        for row in self.input:
            count = 0
            for num in row:
                count += self.numsCount[num]
            self.countsPerRow.append([row,count])
        
        self.countsPerRow.sort(key = lambda x: x[1])

    def findMaxSets(self):

        self.findSets()
        usedNums = set()
        usedSets = []
        count = 0

        for row in self.countsPerRow:
            if usedNums.isdisjoint(set(row[0])):
                count += 1
                usedSets.append(row[0])
                usedNums.update(row[0])
        # print(self.countsPerRow)
        print(usedSets)
        return count

input = [[1,2,3],[1,9,11],[1,8,10],[1,8,11],[1,8,11],[1,8,11],[1,8,10],[2,3,11],[1,8,11],[1,8,10],[1,9,11],[1,8,10],[1,8,11],[1,8,10],[1,8,11],[1,8,10],[1,8,11],[1,9,10],[6,7,8],[9,10,11],[8,9,11]]

game = Solution(input)

print(game.findMaxSets())

    















