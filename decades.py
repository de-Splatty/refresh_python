age = input("What is your age?\n")
age = int(age)
#the input function always returns a string so we need to convert it to an integer using the int() function
#we can also convert it to a float using the float() function
decades = age // 10 #the double forward slash is used to get the quotient of a division also called a floor division operator
years = age % 10 #the percentage sign is used to get the remainder of a division also called a modulus operator
print("you are " + str(decades)+ " decades old and " + str(years) + " years old")