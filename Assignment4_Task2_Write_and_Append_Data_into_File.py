"""
Docstring for Assignment4_Task2_Write_and_Append_Data_into_File
  
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file. 

"""

def write_into_file(file_name, data_to_write):
    try:
        # Write data to the file
        with open(file_name, 'w') as file:
            file.write(data_to_write + '\n') 

        print(f"Data successfully written to '{file_name}'.")
        
        # Read and display the final content of the file
        with open(file_name, 'r') as file: 
            for line in file:
                print(line.strip())
    
    except Exception as e:
        print(f"An error occurred: {e}")




def  append_file(file_name,  data_to_append):
    try: 
        
        # Append additional data to the file
        with open(file_name, 'a') as file:
            file.write(data_to_append + '\n')
        
        print("Data appended successfully.")

        # Read and display the final content of the file
        with open(file_name, 'r') as file:            
            for line in file:
                print(line.strip())
    
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    user_input = input("Enter text to write to the file: ") 
    write_into_file('sample.txt', user_input)
    additional_data_input = input("Enter the additional text to append: ") 
    append_file('sample.txt', additional_data_input)
 