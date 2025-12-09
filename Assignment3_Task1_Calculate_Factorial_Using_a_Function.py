#By using recursion method we will calculate factorial
 
def calculate_factorial(num):
    factorial=0
    if(num==1):
      return num
    else:
      factorial=factorial+(num*calculate_factorial(num-1))

    return factorial

# Take a number input from user and call the method to calculate the factorial
user_num=int(input("Enter a number: "))
print (f"Factorial of {user_num} is: {calculate_factorial(user_num)}")




    