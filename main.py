#Leap Year
# it is a leap year if it is divisible by 4 but not by 100
# if it is divisible by 4 and 100 then it is not a leap year
# if it is divisible by 4, 100 and 400 then it is a leap year
print("Welcome to Leap Year Calculator")
year = int(input("Enter a year to see if its a leap year: "))
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("This is a leap year")
    else:
      print("This is not a leap year")
  else:
    print("This is a leap year")
else:
  print("This is not a leap year")
