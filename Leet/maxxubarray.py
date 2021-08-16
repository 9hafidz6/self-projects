#O(n^2) solution

class Solution:
    def __init__(self):
        pass
    def soln(self, inplist):
        #compute every single subarray 
        result = 0
        for i,num in enumerate(inplist):
            maximum = num
            if len(inplist) > 1:
                #start is included but stop is not
                for j in range(i+1,len(inplist)):
                    #add them all up
                    maximum += inplist[j]
                    # print(f"inplist is :{inplist[j]}")
                    # print(f"i is :{i} j is:{j}")
                    # print("maximum is: ", maximum)
                    result = max(result,maximum)
                    print(result)
            else:
                result = num
        return result

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

#==================================================================================
#naive method is O(n^2), check all possible sub array
#linear solution O(n)

class Solution1:
    def __init__(self):
        pass
    def soln(self, inplist):
        maxSub = inplist[0]
        curSum = 0

        for n in inplist:
            #if get negative prefix, we remove it 
            if curSum < 0:
                #largest subarray can be an empty array, 0
                curSum = 0
            curSum += n
            maxSub = max(curSum, maxSub)
            print(maxSub)
        return maxSub


def main():
    sol = Solution1()
    inp = input() #user gives input unordered list
    inp = inp.strip("[]")
    # print(inp)
    inplist = inp.split(",")

    inplist = [int(i) for i in inplist] #change all element inside to int type
    # print(type(inplist), inplist)
    print(sol.soln(inplist))

if __name__ == "__main__":
    main()
