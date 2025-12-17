"""
Assignment6_Task1_GUICalculator_Using_Tkinter

1.   Creates a simple calculator GUI using Tkinter.
2.   Supports basic arithmetic operations: addition, subtraction, multiplication, and division. 

"""   
from tkinter import *  

# Create the main window
root = Tk()
root.geometry("400x350")

root.title("Simple Calculator")

# Entry Boxes
entry1 = Entry(root,width=58,borderwidth=3)
entry1.place(x=20,y=20)    

#Buttons
def click(num):
    result=entry1.get()   
    entry1.delete(0,END)
    entry1.insert(0,str(result)+str(num))

b=Button(root,text="1",width=12,command=lambda:click(1)) 
b.place(x=20,y=60)  
b=Button(root,text="2",width=12,command=lambda:click(2)) 
b.place(x=150,y=60)
b=Button(root,text="3",width=12,command=lambda:click(3))        
b.place(x=280,y=60)

b=Button(root,text="4",width=12,command=lambda:click(4)) 
b.place(x=20,y=100)
b=Button(root,text="5",width=12,command=lambda:click(5)) 
b.place(x=150,y=100)
b=Button(root,text="6",width=12,command=lambda:click(6)) 
b.place(x=280,y=100) 

b=Button(root,text="7",width=12,command=lambda:click(7))
b.place(x=20,y=140)
b=Button(root,text="8",width=12,command=lambda:click(8))
b.place(x=150,y=140)
b=Button(root,text="9",width=12 ,command=lambda:click(9))
b.place(x=280,y=140)

b=Button(root,text="0",width=12,command=lambda:click(0))
b.place(x=20,y=180)

#Operation Buttons
def add():
    n1=entry1.get()
    global math
    math="addition"
    global i
    i=float(n1)
    entry1.delete(0,END) 

def subtract():
    n1=entry1.get()
    global math
    math="subtraction"
    global i
    i=float(n1)
    entry1.delete(0,END)    
    
def multiply():
    n1=entry1.get()
    global math
    math="multiplication"
    global i
    i=float(n1)
    entry1.delete(0,END)

def divide():
    n1=entry1.get()
    global math
    math="division"
    global i
    i=float(n1)
    entry1.delete(0,END)

b=Button(root,text="+",width=12,command=add)
b.place(x=150,y=180)  
b=Button(root,text="-",width=12,command=subtract)
b.place(x=280,y=180)

b=Button(root,text="*",width=12,command=multiply)
b.place(x=20,y=220)
b=Button(root,text="/",width=12,command=divide)
b.place(x=150,y=220)

def equal():
    n2=entry1.get()
    entry1.delete(0,END)
    if math=="addition":
        entry1.insert(0,i+float(n2))
    elif math=="subtraction":
        entry1.insert(0,i-float(n2)) 
    elif math=="multiplication":
        entry1.insert(0,i*float(n2)) 
    elif math=="division":
        entry1.insert(0,i/float(n2))

b=Button(root,text="=",width=12,command=equal)    
b.place(x=280,y=220)

def decimal():
    result=entry1.get()   
    entry1.delete(0,END)
    entry1.insert(0,str(result)+str("."))

b=Button(root,text=".",width=12,command=decimal)
b.place(x=20,y=280)

def clear():
    entry1.delete(0,END)    


b=Button(root,text="Clear",width=30,command=clear)    
b.place(x=150,y=280)


# def add():
#     try:
#         result = float(entry1.get()) + float(entry2.get())
#         messagebox.showinfo("Result", f"Addition Result: {result}")
#     except ValueError:
#         messagebox.showerror("Error", "Invalid input. Please enter numeric values.")        
# def subtract():
#     try:
#         result = float(entry1.get()) - float(entry2.get())
#         messagebox.showinfo("Result", f"Subtraction Result: {result}")
#     except ValueError:
#         messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

# def multiply():
#     try:
#         result = float(entry1.get()) * float(entry2.get())
#         messagebox.showinfo("Result", f"Multiplication Result: {result}")
#     except ValueError:
#         messagebox.showerror("Error", "Invalid input. Please enter numeric values.")
# def divide():
#     try:
#         result = float(entry1.get()) / float(entry2.get())
#         messagebox.showinfo("Result", f"Division Result: {result}")
#     except ValueError:
#         messagebox.showerror("Error", "Invalid input. Please enter numeric values.")
#     except ZeroDivisionError:
#         messagebox.showerror("Error", "Cannot divide by zero.")



# # Create and place the input fields and buttons
# tk.Label(root, text="Enter first number:").grid(row=0, column=0)
# entry1 = tk.Entry(root) 
# entry1.grid(row=0, column=1)

# tk.Label(root, text="Enter second number:").grid(row=1, column=0)
# entry2 = tk.Entry(root)
# entry2.grid(row=1, column=1)

# # Create and place the buttons
# tk.Button(root, text="Add", command=add).grid(row=2, column=0)
# tk.Button(root, text="Subtract", command=subtract).grid(row=2, column=1)
# tk.Button(root, text="Multiply", command=multiply).grid(row=3, column=0)
# tk.Button(root, text="Divide", command=divide).grid(row=3, column=1)    

# Run the application
root.mainloop()