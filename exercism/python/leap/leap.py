def inputYear(leap):
  while True:
    try:
       userInput = int(input(leap))       
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput 
       break 

year = inputYear("What year is it?")
if year%4 == 0 and year%100 != 0:
    print ("Leap Year!")
else:
    print ("Not a leap year!")
