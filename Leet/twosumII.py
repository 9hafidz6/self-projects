#leetcode twosum, find 2 number that add up to target
#input list that are sorted
#time complexity is O(n) by using 2 pointer method
#question uses 1 based index

class Solution:
    def __init__(self):
        self.name = ""

    def soln(self, inplist, target):
        l = 0
        r = len(inplist) - 1
        inplen = len(inplist)
        while l < r:
            num = inplist[l] + inplist[r]
            if num < target:
                l += 1
            elif num > target:
                r -= 1
            elif num == target:
                return l+1,r+1
            else:
                return l+1,r+1

def main():
    sol = Solution()
    # given an input of [1,2,3,4,5] etc find the sum if 2 numbers which equals to target
    inp = input()
    target = input()
    inp = inp.strip("[]")
    # print(inp)
    inplist = inp.split(",")
    #convert elements in inplist to int type
    inplist = [int(i) for i in inplist]
    # print(type(inplist), inplist)
    print(sol.soln(inplist,int(target)))

if __name__ == "__main__":
    main()
