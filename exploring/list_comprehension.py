def main():
    li = ["1","2","3","4","5"]

    li = [int(x) for x in li]

    newli = {x : x**2 for x in li if x < 5}

    for x,y in newli.items():
        print(x,y)

if __name__ == "__main__":
    main()