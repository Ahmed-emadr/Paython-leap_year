#  function to implement conditions to check leap year
def is_leap(year):
  # Checking if the given year is leap year by using "or " "and" gates
  if((year % 400 == 0) or
     (year % 100 != 0) and
     (year % 4 == 0)):

    print("Given Year is a leap Year")#user output message

  # Else it is not a leap year
  else:
    print ("Given Year is not a leap Year")#user output message

year = int(input("Enter the number: "))# user input message
# Printing result
is_leap(year) #function call
