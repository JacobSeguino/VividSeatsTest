#just a starting 2d array so we have some base numbers and a welcome message
store = [["Company A", 1000, 3000],["Company B", 6000, 10000],["Company C", 500, 2500]]
print "hello, I hope you are having a good day"

#for determing the best stores for the given hights and lowest price, for best results use (int, int)
def HiLow (low, high):
    low, high = lowToHigh(low, high)
        
    print "for a high of {0} and a low of {1} your stores are:".format(high, low)
    checkOut = []
    for i in store:
        if i[1] <= high and i[2] > low:
            checkOut.append(i[0])
        elif i[2] >= low and i[2] < high:
            checkOut.append(i[0])
            
    if not checkOut:
        print "Sorry, none of our current stores match your choices"
    else:
        for j in checkOut:
            print j

#for adding a new store to the list, for best results use (string, int, int)
def addStore(name, low, high):
    low, high = lowToHigh(low, high)
    newStore = [name, low, high]
    store.append(newStore)
    print "the new store list is:"
    for i in store:
        print i

#for adding stores if you want to have the use put their input
def addInputStores():
    name = raw_input("please enter a store name:")
    low = getRawNumber("low")
    high = getRawNumber("high")
    addStore(name, low, high)

#for if you want the user to put in their own price range they are looking for
def hiLowUserInput():
    print "What is the price range you are looking for?"
    low = getRawNumber("low")
    high = getRawNumber("high")
    low, high = lowToHigh(low, high)
    HiLow(low, high)

#a function to sort low and high number
def lowToHigh(low, high):
    if high < low:
        newLow = high
        high = low
        low = newLow
    return low, high

#check to see if the input is a number or not
def getRawNumber(setWord):
    num = (int(raw_input("Please enter a {0} price:".format(setWord))))
    while not num.isdigit():
        num = raw_input("Sorry, that was not a number. Please, enter a number:")
    return num

HiLow(2500, 5000)
# HiLow(3000, 6000)
# HiLow(200, 400)
# HiLow(12000, 15000)
# HiLow(900, 7000)
# HiLow(2000, 1000)
#hiLowUserInput()

print "have a nice day"