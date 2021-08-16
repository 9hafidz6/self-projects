#leetcode 3, longest consecutive substring without repeating characters 
#my method (not optimal)
#O(n^2)

class Solution:
    def __init__(self):
        pass
    def solve(self,inp):
        substring = []
        maxlen = 0
        for num,i in enumerate(inp):
            r = num
            while r < len(inp):
                if inp[r] not in substring:
                    substring.append(inp[r])
                    # len += 1
                    # len = max(len, len(substring))
                    maxlen = max(len(substring), maxlen)
                    # print("len of r:", r)
                    r += 1
                else:
                    substring.clear()
                    # substring.append(inp[num])
                    break
        return maxlen

def main():
    inp = input()
    sol = Solution()
    print(sol.solve(inp))

if __name__ == "__main__":
    main()

#======================================================================================
#neetcode method, uses a sliding window method (2 pointers), O(n)

class Solution1:
    def __init__(self):
        pass
    def solve(self,inp):
        l = 0
        length = 0
        charSet = set()

        for r in range(len(inp)):
            while inp[r] in charSet:
                charSet.remove(inp[l])
                l += 1
            charSet.add(inp[r])
            length = max(length, r-l+1)
        return length

def main():
    inp = input()
    sol = Solution1()
    print(sol.solve(inp))

if __name__ == "__main__":
    main()