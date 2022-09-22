#CODE BY Lucas Tsetskhladze (2s Compliment Binary Converter)
#Copyright © 2022 Lucas Tsetskhladze All Rights Reserved

number = 0
Binarystring = ''

number = input("Please put in a number between -128 and 127:")
number = int(number)
while number < -128 or number > 127:
  number = input("Boundary ERROR, Please put in a number between -128 and 127:")
  number = int(number)
if number < 0:
  listofnumber = 64
  number = 127 - abs(number)
  Binarystring += '1'
else:
  listofnumber = 128

while listofnumber >= 1:
  if number >= listofnumber:
    Binarystring += '1'
    number -= listofnumber
  else:
    Binarystring += '0'
  listofnumber /= 2

print("Your number in Binary is: " + Binarystring + " Hope you enjoy")