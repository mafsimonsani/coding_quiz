"""Write a program which prompts the user for a Celsius temperature,
convert the temperature to Fahrenheit, and print out the converted temperature.
"""

# ask a Celsius temperature to user

Celsius_temp = input('Enter a temperature: ')
Celsius_temp = float(Celsius_temp)

# convert Celsius to Fahrenheit: Celsius * 9/5 + 32

Fahrenheit_temp = Celsius_temp * 9/5 + 32

# print Fahrenheit temperature
print('The converted temperature:', Fahrenheit_temp)
 
