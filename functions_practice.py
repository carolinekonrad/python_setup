"""Practice with Functions"""

__author__ = "Caroline Konrad"

#Hello function
def hello():
    print("Hello there")

#Pack function
def pack(x, y, z):
    newList = [x, y, z]
    return(newList)

#EatLunch function
def eat_lunch(myList):
    if len(myList) == 0:
        print('My lunchbox is empty')
    else:
        for i in range(len(myList)):
            if i == 0:
                print(f"First I eat {myList[i]}")
            else:
                print(f"Next I eat {myList[i]}")

hello()
print(pack('yellow', 'green', 'blue'))
print(pack(15,16,17))
eat_lunch([])
eat_lunch(["pudding"])
eat_lunch(["crackers", "cheese", "bananas"])