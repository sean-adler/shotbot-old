import os

def getLogPath():
    """
    Outputs the path of the log.txt file.
    """
    pwd = os.path.dirname(os.path.abspath(__file__))
    log_file = os.path.join(pwd, 'log.txt')

    return log_file

def log_request(ingredient_list):
    """
    Convert a list to a string and write it to log.txt.
    """
    logPath = getLogPath()
    ingredient_string = "".join([str(i) for i in ingredient_list])
    with open(logPath, 'a') as log:
        log.write(ingredient_string)
        log.write("\n")

def getLog():
    """
    Reads the log.txt file and removes newlines.
    """
    logPath = getLogPath()
    
    with open(logPath) as f:
        log = f.readlines()

    cleanedLog = []
    
    for line in log:
        drink = line[0:8]
        cleanedLog.append(drink)
    
    return cleanedLog

def clearLog():
    """
    Erases contents of the log.txt file.
    """
    logPath = getLogPath()

    with open(logPath, 'w') as f:
        f.write('')

def getIngredients():
    """
    Outputs a list of the ingredients ShotBot can pour.
    """
    ingredients = ['Whiskey', 'Tequila', 'Vodka', 'Blue Curacao', 'Orange Juice',
                   'Pineapple Juice', 'Cranberry Juice', 'Sour Mix']
    return ingredients

def getDrinkInfo():
    """
    Outputs a dictionary containing all drink names, and their
    corresponding ingredients and counts (times consumed).
    Counts start at 0 and are modified by drink_chart() in
    test_shotbot_server.py.
    """
    drinkInfo = {
                'Bay Breeze': {'ingredients': '00600440',
                                'count': 0},
                 'Cosmopolitan': {'ingredients': '00603042',
                                    'count': 0},
                 'Green Monster': {'ingredients': '00040004',
                                    'count': 0},
                 'Green Widow': {'ingredients': '00046000',
                                    'count': 0},
                 'Margarita': {'ingredients': '07001004',
                                    'count': 0},
                 'Screwdriver': {'ingredients': '00808000',
                                    'count': 0},
                 'Tequila Sunrise': {'ingredients': '08004400',
                                    'count': 0},
                 'Whiskey Sour': {'ingredients': '80000008',
                                    'count': 0},
                 'Custom Drinks': {'ingredients': 'xxxxxxxx',
                                   'count': 0}
                 }
    
    return drinkInfo
