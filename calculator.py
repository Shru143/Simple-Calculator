import tkinter as tk
from tkinter import messagebox

def button_click(item):
    current = input_text.get()
    input_text.set(current + str(item))

def button_clear():
    input_text.set("")

def button_equal():
    try:
        result = str(eval(input_text.get()))
        input_text.set(result)
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")
        input_text.set("")
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        input_text.set("")

window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x400")
window.configure(bg="sky blue")  

input_text = tk.StringVar()

input_frame = tk.Frame(window, bg="sky blue") 
input_frame.pack()

input_field = tk.Entry(input_frame, textvariable=input_text, font=('arial', 18), width=22, bd=8, justify='right')
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

btns_frame = tk.Frame(window, bg="sky blue")  
btns_frame.pack()

button_color = "pink"  
button_font = ('arial', 14, 'bold')  

clear = tk.Button(btns_frame, text="C", width=10, height=3, bg=button_color, font=button_font, command=button_clear)
clear.grid(row=0, column=0)

divide = tk.Button(btns_frame, text="/", width=10, height=3, bg=button_color, font=button_font, command=lambda: button_click("/"))
divide.grid(row=0, column=1)

multiply = tk.Button(btns_frame, text="*", width=10, height=3, bg=button_color, font=button_font, command=lambda: button_click("*"))
multiply.grid(row=0, column=2)

subtract = tk.Button(btns_frame, text="-", width=10, height=3, bg=button_color, font=button_font, command=lambda: button_click("-"))
subtract.grid(row=0, column=3)

seven = tk.Button(btns_frame, text="7", width=10, height=3, bg=button_color, font=button_font, command=lambda: button_click(7))
seven.grid(row=1, column=0)

eight = tk.Button(btns_frame, text="8", width=10, height=3, bg=button_color, font=button_font, command=lambda: button_click(8))
eight.grid(row=1, column=1)

nine = tk.Button(btns_frame, text="9", width=10, height=3, bg=button_color, font=button_font, command=lambda: button_click(9))
nine.grid(row=1, column=2)

add = tk.Button(btns_frame, text="+", width=10, height=3, bg=button_color, font=button_font, command=lambda: button_click("+"))
add.grid(row=1, column=3)

four = tk.Button(btns_frame, text="4", width=10, height=3, bg=button_color, font=button_font, command=lambda: button_click(4))
four.grid(row=2, column=0)

five = tk.Button(btns_frame, text="5", width=10, height=3, bg=button_color, font=button_font, command=lambda: button_click(5))
five.grid(row=2, column=1)

six = tk.Button(btns_frame, text="6", width=10, height=3, bg=button_color, font=button_font, command=lambda: button_click(6))
six.grid(row=2, column=2)

equal = tk.Button(btns_frame, text="=", width=10, height=3, bg=button_color, font=button_font, command=button_equal)
equal.grid(row=2, column=3)

one = tk.Button(btns_frame, text="1", width=10, height=3, bg=button_color, font=button_font, command=lambda: button_click(1))
one.grid(row=3, column=0)

two = tk.Button(btns_frame, text="2", width=10, height=3, bg=button_color, font=button_font, command=lambda: button_click(2))
two.grid(row=3, column=1)

three = tk.Button(btns_frame, text="3", width=10, height=3, bg=button_color, font=button_font, command=lambda: button_click(3))
three.grid(row=3, column=2)

modulus = tk.Button(btns_frame, text="%", width=10, height=3, bg=button_color, font=button_font, command=lambda: button_click("%"))
modulus.grid(row=3, column=3)

zero = tk.Button(btns_frame, text="0", width=22, height=3, bg=button_color, font=button_font, command=lambda: button_click(0))
zero.grid(row=4, column=0, columnspan=2)

window.mainloop()

