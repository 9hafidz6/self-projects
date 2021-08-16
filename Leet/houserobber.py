#dynamic programming question in linear time

class Solution:
    def __init__(self):
        pass
    def soln(self, inplist):
        rob1, rob2 = 0, 0,
        # [rob1, rob2, n, n+1, ...]
        for n in inplist:
            temp = max(rob1+n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

        # [1,2,3,1]
        # pass 1
        #     n = 1
        #     temp = 1
        #     r1 = 0
        #     r2 = 1
        # pass 2
        #     n = 2
        #     temp = 2
        #     r1 = 1
        #     r2 = 2
        # pass 3
        #     n = 3
        #     temp = 4
        #     r1 = 2
        #     r2 = 4
        # pass 4
        #     n = 1
        #     temp = 4
        #     r1 = 4
        #     r2 = 4
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
