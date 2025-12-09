"""
Docstring for Assignment3_Task2_Using_the_Math_Module_for_Calculations
By using Math moudle we do some calculation.
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
      o   Square root of the number
      o   Natural logarithm (log base e) of the number
      o   Sine of the number (in radians)
3. Displays the calculated results.

"""
  
#import math module
import math

# Take a number input from user and call the method to calculate the factorial
print()
print("==============================")
user_num=int(input("Enter a number: "))
print("==============================")
print (f"Square root:  {math.sqrt(user_num)}")
print (f"Natural logarithm:  {math.log(user_num)}")
print (f"Sine:  {math.sin(user_num)}")
print("==============================")
print()
print("Thanks for using Math Module for calculations")
print()





    