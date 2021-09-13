from collections import deque

class Solution:
    def __init__(self):
        pass
    def rotate(self,b,rotate):
        d = deque(b)
        # print(type(d),d)

        # Rotate the deque 'rotate' steps to the right. If 'rotate' is negative, rotate to the left.
        d.rotate(-rotate)
        print(d)
        
def main():
    a = Solution()

    b = input().rstrip().split()
    # print(type(b))
    # for i in b:
    #     print(i)

    rotate_by = int(input().rstrip())

    a.rotate(b,rotate_by)


if __name__ == "__main__":
    main()