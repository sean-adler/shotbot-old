def getDrinkList():
        drinkList = {'00600440': 'Bay Breeze',
		'00603042': 'Cosmopolitan',
		'00040004': 'Green Monster',
		'00046000': 'Green Widow',
		'07001004': 'Margarita',
		'00808000': 'Screwdriver',
		'08004400': 'Tequila Sunrise',
		'80000008': 'Whiskey Sour'}
	return drinkList

def getDrinkInfo():
        drinkInfo = {'Bay Breeze': {'ingredients': '00600440',
                                    'count': 0},
                     'Cosmopolitan': {'ingredients': '00600440',
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
