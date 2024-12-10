# import datetime
# x = datetime.datetime.now()
# print(x.strftime("%B"))

# y = datetime.datetime(2024, 8, 20)
# print(y.strftime('%d'))

# x = min(5, 10, 25)
# y = max(5, 10, 25)
# z = abs(-7.25)

# print(x, y, z)

# x = pow(2, 3)
# print(x)

# import math
# x = math.sqrt(64)
# print(int(x))

# import math
# x = math.ceil(1.4)
# y = math.floor(1.4)
# print(x, y)

# import math

# x = math.pi
# print(x)

import json

x = {
    "name": "John",
    "ade": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "Bmw 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x))
print(x['cars'][1])
