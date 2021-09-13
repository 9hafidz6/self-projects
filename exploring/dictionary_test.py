# sorting a dictionary by value
# https://careerkarma.com/blog/python-sort-a-dictionary-by-value/

def main(): 
    orders = {
        'cappuccino': 54,
        'latte': 56,
        'espresso': 72,
        'americano': 48,
        'cortado': 41
    }

    # print both the key in value in dictionary
    for k,v in orders.items():
        print(k,v)

    # the .items() gives the key and value pair 
    # sorting by value in descending order
    print("sorting dictionary by value in descending order")
    sort_orders = sorted(orders.items(), key=lambda x: x[1], reverse=True)
    # sorted() returns a list, sort() changes the current list
    for i in sort_orders:
        print(i[0], i[1])

    # sort by key
    print("sorting dictionary by key in descending order")
    sort_orders = sorted(orders.items(), key=lambda x: x[0], reverse=True)
    for i in sort_orders:
        print(i[0], i[1])

    # sort the dictionary by keys but only returns a list of keys 
    sort_orders = sorted(orders.keys(), reverse=True)
    print(sort_orders)


if __name__ == "__main__":
    main()