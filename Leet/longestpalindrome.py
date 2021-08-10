#neetcode solution

class Solution:
    def __init__(self):
        pass
    def soln(self, inp):
        res = ""
        reslen = 0

        for i in range(len(inp)):
            #odd length
            l, r = i, i
            while l >=0 and r < len(inp) and inp[l] == inp[r]:
                if (r-l+1) > reslen:
                    res = inp[l:r+1]
                    reslen = r - l + 1
                l -= 1
                r += 1
            #even length
            l, r = i, i + 1
            while l >=0 and r < len(inp) and inp[l] == inp[r]:
                if (r-l+1) > reslen:
                    res = inp[l:r+1]
                    reslen = r - l + 1
                l -= 1
                r += 1  
        return res

def main():
    sol = Solution()
    # inp = input() 
    inp = 'ababd'
    print(sol.soln(inp))

if __name__ == "__main__":
    main()
