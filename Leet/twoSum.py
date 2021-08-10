#leetcode twosum
#input list that are not sorted
#time complexity is O(n^2)

class Solution:
    def __init__(self):
        self.name = ""

    def soln(self, inplist, target):
        l = 0
        r = len(inplist) - 1
        inplen = len(inplist)
        for i in range(inplen):
            requireNum = int(target) - int(inplist[i])
            if requireNum in inplist and inplist.index(requireNum) != i:
                return i, inplist.index(requireNum)
            else:
                continue

def main():
    sol = Solution()
    # given an input of [5,4,3,2,1] etc find the sum if 2 numbers which equals to target
    inp = input()
    target = input()
    inp = inp.strip("[]")
    # print(inp)
    inplist = inp.split(",")
    inplist = [int(i) for i in inplist]
    # print(type(inplist), inplist)
    print(sol.soln(inplist,target))

if __name__ == "__main__":
    main()
