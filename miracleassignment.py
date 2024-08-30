mylist = []
userchioce = 0
def start():
    print("welcome to your personal list manager")
    print("enter 1 to add")
    print("enter 2 to remove")
    print("enter 3 to view")
    userchioce = input()

def additem():
    print("enter new item")
    additem = input()
    mylist.append('item to add')
    print(mylist)

def viewitems():
    print(mylist)

def removeitem():
    print("enter purchased item")
    purchaseditem = input()
    mylist.remove('purchased item')
    print(mylist)

def countitems():
    count = len(mylist)
    print('count')



def start():






