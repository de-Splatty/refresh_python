first_name = "Adkins"
last_name = "Macharia"
print("Full name:", first_name, "Mwangi", last_name)

country = "Kenya"
city = "Nairobi"
print(f"I am from {country} and I live in {city}.")

age = 18
year = 2025
print(f"In the current year of {year}, I am {age} years old.")

is_married = False
if not is_married:
    print("I am not married.")
else:
    print("I am married.")

is_true = True
is_light_on = True

first_name, last_name, country, city, age, year, is_married, is_true, is_light_on = (
    "Adkins",
    "Macharia",
    "Kenya",
    "Nairobi",
    18,
    2025,
    False,
    True,
    True,
)

if len(first_name) > len(last_name):
    print("Your first name is longer than your last name.")
else:
    print("Your last name is longer than your first name.")

number_one= 10
number_two= 6
summation = number_one + number_two
diff= number_one - number_two
product = number_one * number_two
division = number_one / number_two
modulus = number_one % number_two
floor_division = number_one // number_two
exponentiation = number_one ** number_two
print(summation, diff, product, division, modulus, floor_division, exponentiation)

radius = 30
pi = 3.142
area_of_circle = pi * radius ** 2
print(f"The area of a circle with a radius of{radius} is: {area_of_circle}")
circumference_of_circle = 2 * pi * radius
print(f"The circumference of a circle with a radius of {radius} is: {circumference_of_circle}")

user_first_name = input("Enter your first name:")
user_last_name = input("Enter your last name:")
user_country = input("Enter your country:")
user_age = int(input("Enter your age: "))
if user_country.strip().casefold() == "kenya" and user_age >= 18:
    print(f"{user_first_name} {user_last_name} you are eligible to vote.")
if user_country != "Kenya" or "kenya":
    print("Only Kenyan citizens are allowed to vote.")
if user_age < 18:
    print("You must be at least 18 years old to vote.")

