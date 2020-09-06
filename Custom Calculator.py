#What we are doing here is: converting temperature form celsius to fahrenheit.
#At the beginning we want to have a wellcome massage, an introduction print a long with instruction for the user.
#We are using extra "print()"'s to space up between our lines so that it looks more like a reall program.
print()
print()
print()
print ("Hello!")
print()
print("This is a Celsius To Fahrenheit Temperature Converter")
print()
celsius = input("Enter the temperature in celsius: ")
#Here we are asking the user for an input.
#Since the input is going to be numbers we need to convert our variable from stinge to the format of an integer-
#- so that the computer can calculate.
celsius = int(celsius)
#formula for our function is (C * 9/5 + 32)...according to Google.
fahrenheit = (celsius * 9/5) + 32
print()# we want our result to be well explained and displayed to the user.
print("Temperature is", fahrenheit, "degrees in Fahrenheit")
print()# at the end if we want to attract the user for future usage of our program we can print a very good closing massage like..
print("Thank You For Using This Converter")