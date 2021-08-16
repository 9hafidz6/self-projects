#leetcode twosum
#input list that are sorted
# 3 numbers that sum to 0
#time complexity is O(n^2) by using 2 pointer method


class Solution:
    def __init__(self):
        self.name = ""

    def soln(self, inplist):
        inplen = len(inplist)
        result = []
        inplist.sort()
        for i,num in enumerate(inplist):
            if i > 0 and num == inplist[i-1]:
                continue

            l = i + 1
            r = inplen - 1
            # for j in range(i,inplen):
            while l < r:
                #same method as two sum II
                sum = inplist[i] + inplist[l] + inplist[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                elif sum == 0:
                    #append the 3 numbers in the result list
                    result.append([num,inplist[l], inplist[r]])
                    l += 1
                    while inplist[l] == inplist[l-1]:
                        #for the case of [-2,-2,0,0,2,2]
                        #to avoid duplicate combinations 
                        l += 1

        return result

def main():
    sol = Solution()
    # given an input of [1,2,3,4,5] etc find the sum if 3 numbers which equals to target
    #must not be repeating numbers
    inp = input()
    # target = input()
    inp = inp.strip("[]")
    # print(inp)
    inplist = inp.split(",")
    inplist = [int(i) for i in inplist]
    # print(type(inplist), inplist)
    print(sol.soln(inplist))

if __name__ == "__main__":
    main()
