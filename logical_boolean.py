temperature = 75

if temperature > 80 or temperature < 60:
    print("The temperature is extreme.")
else:
    print("The temperature is moderate.")
    
temp = 35
forecast = "rainy"

if temp > 30 and forecast == "sunny":
    print("It's a hot and sunny day.")
elif temp < 30 and forecast == "rainy":
    print("It's a cool and rainy day.")
    
weather = "windy"

if not weather == "sunny":
    print("It's not a sunny day.")
else:
    print("It's a sunny day.")
    
    #not true = false
    #not false = true
    
raining = True

if raining:
    print("It's raining, take an umbrella.")
if not raining:
    print("It's not raining, no umbrella needed.")