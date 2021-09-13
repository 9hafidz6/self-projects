# https://docs.python.org/3/tutorial/datastructures.html#sets

def main():
    # use set to remove duplicates in a list 
    # for integers, set will sort in ascending order 
    # for string, set will order the elements randomly 
    input_list = [5,5,4,4,1,2,3]
    s = set(input_list)
    print(s)

    input_list = ["aba","aba","aa","aa","bb","bb","d","f","g","aba",]
    d = set(input_list)
    print(d)    

    # operators such as | & can be used on sets 

    s1 = {1,2,3,4,5}
    s2 = {3,4,5,6,7}

    print(s1 & s2) # AND operator
    print(s1 | s2) # OR operator
    print(s1 ^ s2) # XOR operator
    print(s1 - s2) # elements in a s1 but not in s2, disjointed sets 

if __name__ == '__main__':
    main()