from GChartWrapper import Pie

def createChart():
    print Pie(cleanData()).title('Drinks').color('red', 'lime', 'orange', 'green', 'pink', 'black', 'yellow', 'purple').label('whiskey', 'tequila', 'vodka', 'blue curacao', 'orange juice', 'pineapple juice', 'cranberry juice', 'sour mix')

# make color list and label list
colors = ['red', 'lime', 'orange', 'green', 'pink', 'black', 'yellow', 'purple']
                                               
def cleanData():
    drinkList = [0,0,0,0,0,0,0,0]
    with open('log.txt') as log:
        drinkData = log.readlines()
    for i in range(len(drinkList)):
        for drink in drinkData:
            drinkList[i] += int(drink[i])
    return drinkList

createChart()

#print Pie([5,10]).title('Drinks').color('red','lime').label('hello', 'world')
