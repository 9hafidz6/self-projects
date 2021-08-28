#pascal triangle 

class Solution:
    def __init__(self):
        pass
    def solve(self,num_row):
        res = [[1]]
        #res[-1] is referring to the previous index in res
        for i in range(num_row - 1):
            temp_list = [0] + res[i] + [0]
            # temp_list = [0] + res[-1] + [0] can also use 
            print(f"pass number:{i} \n{temp_list}")
            new_row = []
            #for j in range((len(res[-1])+1)): not plus 2 as it will be out of range 
            for j in range((len(res[i])+1)):
                new_row.append(temp_list[j] + temp_list[j+1])
            res.append(new_row)

        print(res)

def main():
    pascal = Solution()
    num_row = input()
    pascal.solve(int(num_row))

if __name__ == "__main__":
    main()