import datetime

birthYear = int(input("Enter your Birth Year:"))
age = datetime.datetime.now().year - birthYear
print(f"Your Age is {age} years old")
