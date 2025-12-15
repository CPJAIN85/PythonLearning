"""
Docstring for Assignment4_Task1_Read_File_and_Handle_Errors
  
1.  Opens and reads a text file named sample.txt.
2.  Prints its content line by line.
3.  Handles errors gracefully if the file does not exist.

"""
def read_file(file_name):     
    try:
        with open(file_name, 'rt') as file:
            rowId = 1
            for line in file:
                print(f"Line {rowId}: {line.strip()}")
                rowId += 1

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    read_file('sample.txt')   
    