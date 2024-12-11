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

# import json

# x = {
#     "name": "John",
#     "ade": 30,
#     "married": True,
#     "divorced": False,
#     "children": ("Ann", "Billy"),
#     "pets": None,
#     "cars": [
#         {"model": "Bmw 230", "mpg": 27.5},
#         {"model": "Ford Edge", "mpg": 24.1}
#     ]
# }

# print(json.dumps(x))
# print(x['cars'][1])

# import camelcase
# import re
# check if the string starts with "The" and ends with "Spain":
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# if x:
#     print("Yes we have a match!")
# else:
#     print("No match")
# x = re.findall("Portugal", txt)
# print(x)
# x = re.search("\s", txt)
# print("The first whitespace character is located in position:", x.start())

# splits the string at each whitespace and return a list
# x = re.search(r"\bS\w+", txt)
# print(x.group())


# try:
#     number = int(input("Enter a number: "))
#     print(1 / number)

# except ZeroDivisionError:
#     print("You can't Divide by Zero IDIOT")
# except ValueError:
#     print("Enter only Numbers please!")
# except Exception:
#     print("Something went wrong")
# finally:
# #     print("Do some cleanup here")

# f = open('file.txt')
# try:
#     f
#     var = bad_var
# except FileNotFoundError as e:
#     print(e)
# except Exception as e:
#     print(e)
# else:
#     print(f.read())
#     f.close
# finally:
#     print("Executing Finally...")


f = open('We.txt', 'x')
f.write('Hello How are you doing\nMy name is what you think i am\nAm still a beginner and am getting used to mistakes.')
f = open('TST.txt', 'r')
print(f.read())
f.close()
