def hello():
    print("hello")

def pack(item1, item2, item3):
    packedItems = [item1, item2, item3]
    return packedItems

def eat_lunch(lunchBox):
    if len(lunchBox) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(lunchBox)):
            if i == 0:
                print(f"First I eat {lunchBox[0]}")
            else:
                print(f"Next I eat {lunchBox[i]}")