#longest consecurtive sequence in a list
#1 way is to use sorting O(nlog.n), check each element in list is consecurtive
#but need time complexity of O(n)
#use set data structure

class Solution:
    def __init__(self):
        pass
    def soln(self,inplist):
        numset = set(inplist) #put elements in a set, O(n)
        longest = 0
        for n in inplist:
            if (n-1) not in inplist: #check if element have left neighbour, if not, it means it is the start of a sequence 
                #if not, means it is the start of a seqeunce
                length = 0
                while (n+length) in numset:
                    length += 1
                longest = max(longest,length) #then get the length
        return longest

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
