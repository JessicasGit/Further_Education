"""
10.02.2023
7 different variables
    Print out and combine them with either strings
    or each other by using commas and f-strings
        Program should should contain at least
        14 different print commands.
"""

first_name = "Jessica"
last_name = "Göckler"
age = 34
day_of_birth = 18
month_of_birth = "April"
year_of_birth = 1988
programming_book = "HTML and CSS"
price_of_book = 29.95
euro = "€"
positive = True
course = "Applied Bioinformatics and Biostatistics"
abbr = "ABI"
duration = 8
duration2 = "Months"
day = 1
month = "February"

print("My name is",first_name,last_name,"and I'm",age,"Years old")
print("I was born at the",day_of_birth,"th of",month_of_birth,"in",year_of_birth)
print("The last book I bought was",programming_book,"and I paid",price_of_book,euro,"for it")
print("That",programming_book,"helps me a lot is",positive)
print("I take part of a course named",course,"since",day,month)
print("The duration is about",duration,duration2)
print("The abbreviation is",abbr,"and I think it helps me a lot learning Python")
print()
print(f"My name is {first_name} {last_name} and I'm {age} Years old")
print(f"I was born at the {day_of_birth}th of {month_of_birth} in {year_of_birth}")
print(f"The last book I bought was {programming_book} and I paid {price_of_book} {euro} for it")
print(f"That {programming_book} helps me a lot is {positive}")
print(f"I take part of a course named {course} since {month} {day}st")
print(f"The duration is about {duration} {duration2}")
print(f"The abbreviation is {abbr}, and I think it helps me a lot learning Python")
