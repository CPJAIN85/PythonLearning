"""
Docstring for Assignment5_Task2_Demonstrate_List_Slicing
  
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list

""" 
# Step 1: Create a list of numbers from 1 to 10
numbers = list(range(1, 11))        
# Step 2: Extract the first five elements from the list
first_five = numbers[:5]            
# Step 3: Reverse these extracted elements
reversed_first_five = first_five[::-1]  
# Step 4: Print both the extracted list and the reversed list
print("Original list of numbers:", numbers)
print("Extracted first five elements:", first_five)
print("Reversed extracted elements:", reversed_first_five)  

 