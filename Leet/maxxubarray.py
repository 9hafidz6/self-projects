#naive method is O(n^2), check all possible sub array
#linear solution O(n)

class Solution:
    def __init__(self):
        pass
    def soln(self, inplist):
        maxSub = inplist[0]
        curSum = 0

        for n in inplist:
            #if get negative prefix, we remove it 
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(curSum, maxSub)
        return maxSub


def main():
    sol = Solution()
    inp = input() #user gives input unordered list
    inp = inp.strip("[]")
    # print(inp)
    inplist = inp.split(",")

    inplist = [int(i) for i in inplist] #change all element inside to int type
    # print(type(inplist), inplist)
    print(sol.soln(inplist))

if __name__ == "__main__":
    main()
