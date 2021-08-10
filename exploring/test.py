#trying to have a dynamic number of objects in a list 
#and iterate through the list of objects

class Solution:
    def __init__(self):
        self.name = ""
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name

def main():
    objList = []
    #sol = Solution()
    #sol.setName("hafidz")
    #sol1 = Solution()
    #sol1.setName("hazzrin")

    #objList.append(sol)
    #objList.append(sol1)

    length = input()
    for i in range(int(length)):
        obj = Solution()
        name = input()
        obj.setName(name)
        objList.append(obj)

    for num,i in enumerate(objList):
        print(num+1,i.getName())

if __name__ == "__main__":
    main()
