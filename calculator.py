# simple calculator
# print("---------- Welcome to the simple calculator ----------")
# name_of_user = input("What is your name? ")
# var = input(name_of_user + "are you ready to use the simple calculator? y or n ")

# if(var == "y"):
#         print("Great! Let's get started!")
import tkinter 
from tkinter import *
root=tkinter.Tk()
root.title("Calculator")
root.iconbitmap("C:\\Users\\Dell\\Desktop\\Abdullah uet data\\python\\calculator\\iconn.ico")
root.geometry("410x400+300+100")
root.configure(bg="#bcd2bd")
root.resizable(0,0)

# commands
equation=""
def show_data(value):
    global equation
    equation = equation + value
    label.config(text=equation)
def clear_data():
    global equation
    equation = ""
    label.config(text=equation)
def calculate():
    global equation
    result = " "
    if equation!="":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    label.config(text=result)   
def delete():
    global equation
    equation=equation[0:-1]
    label.config(text=equation)
# result show
label = Label(root, text="Calculator", bg="#dae3da", fg="black", width=36 , height=3 , font=("Arial", 14))
label.place(x=4,y=5)

# buttons
Button(root, text="Del", width=10, height=2,bg="#505550",fg="white", font=("verdana", 10),command=delete).place(x=10,y=100)
Button(root, text="+", width=10, height=2,bg="#0e0f0e",fg="white", font=("Arial", 10,"bold"),command=lambda: show_data("+")).place(x=110,y=100)
Button(root, text="-", width=10, height=2,bg="#0e0f0e",fg="white", font=("Arial", 10,"bold"),command=lambda: show_data("-")).place(x=210,y=100)
Button(root, text="x", width=10, height=2,bg="#0e0f0e",fg="white", font=("Arial", 10,"bold"),command=lambda: show_data("*")).place(x=310,y=100)

Button(root, text="9", width=10, height=2,bg="#0e0f0e",fg="white", font=("Arial", 10,"bold"),command=lambda: show_data("9")).place(x=10,y=160)
Button(root, text="8", width=10, height=2,bg="#0e0f0e",fg="white", font=("Arial", 10,"bold"),command=lambda: show_data("8")).place(x=110,y=160)
Button(root, text="7", width=10, height=2,bg="#0e0f0e",fg="white", font=("Arial", 10,"bold"),command=lambda: show_data("7")).place(x=210,y=160)
Button(root, text="/", width=10, height=2,bg="#0e0f0e",fg="white", font=("Arial", 10,"bold"),command=lambda: show_data("/")).place(x=310,y=160)

Button(root, text="6", width=10, height=2,bg="#0e0f0e",fg="white", font=("Arial", 10,"bold"),command=lambda: show_data("6")).place(x=10,y=220)
Button(root, text="5", width=10, height=2,bg="#0e0f0e",fg="white", font=("Arial", 10,"bold"),command=lambda: show_data("5")).place(x=110,y=220)
Button(root, text="4", width=10, height=2,bg="#0e0f0e",fg="white", font=("Arial", 10,"bold"),command=lambda: show_data("4")).place(x=210,y=220)
Button(root, text="%", width=10, height=2,bg="#0e0f0e",fg="white", font=("Arial", 10,"bold"),command=lambda: show_data("%")).place(x=310,y=220)

Button(root, text="3", width=10, height=2,bg="#0e0f0e",fg="white", font=("Arial", 10,"bold"),command=lambda: show_data("3")).place(x=10,y=280)
Button(root, text="2", width=10, height=2,bg="#0e0f0e",fg="white", font=("Arial", 10,"bold"),command=lambda: show_data("2")).place(x=110,y=280)
Button(root, text="1", width=10, height=2,bg="#0e0f0e",fg="white", font=("Arial", 10,"bold"),command=lambda: show_data("1")).place(x=210,y=280)
Button(root, text=".", width=10, height=2,bg="#0e0f0e",fg="white", font=("Arial", 10,"bold"),command=lambda: show_data(".")).place(x=310,y=280)

Button(root, text="0", width=10, height=2,bg="#0e0f0e",fg="white", font=("Arial", 10,"bold"),command=lambda: show_data("0")).place(x=10,y=340)
Button(root, text="Clear", width=22, height=2,bg="#f5aa52",fg="black", font=("Arial", 10,),command=clear_data).place(x=112,y=340)
Button(root, text="=", width=10, height=2,bg="#a387f2",fg="white", font=("Arial", 10,"bold"),command=calculate).place(x=310,y=340)
root.mainloop()
        
# elif(var == "n"):
#         print("Sorry to hear that you dont want to use the simple calculator.")
# else:
#         print("Please enter a valid input.")

 #end of code