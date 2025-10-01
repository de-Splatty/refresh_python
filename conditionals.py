#there are various comparators in python 
# > greater than
# < less than
# == equal to
# != not equal to
# >= greater than or equal to
# <= less than or equal to
 # if statements helps the program know what to do based on certain conditions

weight = input("What is your weight in kg?\n")
height = input("What is your height in m?\n")
weight = float(weight)
height = float(height)
bmi = weight / (height**2)
if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Healthy weight")
elif bmi >= 25 and bmi < 30:
    print("Overweight")
elif bmi >= 30 and bmi < 35:
    print("Obesity class 1")
elif bmi >= 35 and bmi < 40:
    print("Obesity class 2")
else:
    print("Obesity class 3")




