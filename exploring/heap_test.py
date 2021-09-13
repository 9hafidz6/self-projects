import heapq
 # https://docs.python.org/3/library/heapq.html#heapq.heapify

def main():
    # li = [5,5,4,4,3,2,1]

    # use list of tuple to see how the elements are placed 
    # the order is the same as using a normal list
    li = [(5,2),(5,1),(4,3),(4,4),(3,5),(2,6),(1,7)]
    heapq.heapify(li) # takes O(n) time, can take duplicate elements 

    # heapify is by default a minheap, to make a maxheap, change the values to negative 
    print(li)

    # print all the elements in heap 'li' by using heappop
    # heap is now empty
    for i in range(len(li)):
        print(heapq.heappop(li))
    print(li)

    for j in range(5):
        heapq.heappush(li,j+1)
    print(li)
    
if __name__ == '__main__':
    main()