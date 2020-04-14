'''Write a Python program to convert temperatures to and from celsius, fahrenheit. Go to the editor
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius

Fahrenheit to Celsius formula:
(°F - 32) x 5/9 = °C or in plain english, First subtract 32, then multiply by 5,
then divide by 9.

Celsius to Fahrenheit formula:
(°C × 9/5) + 32 = °F or in plain English, Multiple by 9, then divide by 5, then
add 32.
'''
#temp_fah=float(input('enter temp. in fahrenheit :'))

tem_cel=float(input('enter temp. in celsius : '))
f=(tem_cel*1.8)+32
print(f)
