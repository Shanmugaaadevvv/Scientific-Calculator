from tkinter import *
import math as m

# Initialize the main Tkinter window
root = Tk()
root.title("Scientific Calculator")
root.configure(bg="Grey")  # Background color for aesthetics

# Entry widget to display input and results
e = Entry(root, width=50, borderwidth=5, relief=RIDGE, fg="white", bg="black")
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Function to handle button clicks and add input to the entry
def click(to_print):
    old = e.get()
    e.delete(0, END)
    e.insert(0, old + to_print)

# Function to perform scientific calculations
def scientific_calculations(event):
    key = event.widget
    button_text = key['text']  # Renamed variable
    input_text = e.get()
    result = ''
    try:
        if button_text == 'deg':
            result = str(m.degrees(float(input_text)))
        elif button_text == 'sin':
            result = str(m.sin(m.radians(float(input_text))))
        elif button_text == 'cos':
            result = str(m.cos(m.radians(float(input_text))))
        elif button_text == 'tan':
            result = str(m.tan(m.radians(float(input_text))))
        elif button_text == 'lg':
            result = str(m.log10(float(input_text)))
        elif button_text == 'ln':
            result = str(m.log(float(input_text)))
        elif button_text == 'Sqrt':
            result = str(m.sqrt(float(input_text)))
        elif button_text == '1/x':
            result = str(1 / float(input_text))
        elif button_text == 'pi':
            result = str(m.pi if input_text == "" else float(input_text) * m.pi)
        elif button_text == 'e':
            result = str(m.e if input_text == "" else m.e ** float(input_text))
    except ValueError:  # Specific exception for invalid number input
        result = "Invalid Input"
    except ZeroDivisionError:  # Specific exception for division by zero
        result = "Math Error"
    e.delete(0, END)
    e.insert(0, result)

# Function to clear the entry
def clear():
    e.delete(0, END)

# Function to handle backspace
def backspace():
    current = e.get()
    e.delete(0, END)
    e.insert(0, current[:-1])

# Function to evaluate the expression
def evaluate():
    try:
        ans = eval(e.get())
        e.delete(0, END)
        e.insert(0, str(ans))
    except SyntaxError:  # Specific exception for syntax errors in input
        e.delete(0, END)
        e.insert(0, "Syntax Error")
    except ZeroDivisionError:
        e.delete(0, END)
        e.insert(0, "Math Error")

# List of buttons and their positions
buttons = [
    ('lg', 1, 0), ('ln', 1, 1), ('(', 1, 2), (')', 1, 3), ('C', 1, 4),
    ('deg', 2, 0), ('sin', 2, 1), ('cos', 2, 2), ('tan', 2, 3), ('mod', 2, 4),
    ('Sqrt', 3, 0), ('1/x', 3, 1), ('pi', 3, 2), ('e', 3, 3), ('Bksp', 3, 4),
    ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('/', 4, 3), ('*', 4, 4),
    ('4', 5, 0), ('5', 5, 1), ('6', 5, 2), ('-', 5, 3), ('+', 5, 4),
    ('1', 6, 0), ('2', 6, 1), ('3', 6, 2), ('=', 6, 3), ('0', 6, 4),
]

# Loop to create buttons dynamically
for (text, row, col) in buttons:
    if text in ['C', 'Bksp', '=']:
        btn = Button(root, text=text, padx=25, pady=15, relief=RIDGE, fg="white", bg="red" if text == 'C' else "yellow" if text == '=' else "orange")
        if text == 'C':
            btn.config(command=clear)
        elif text == 'Bksp':
            btn.config(command=backspace)
        elif text == '=':
            btn.config(command=evaluate)
    elif text in ['lg', 'ln', 'deg', 'sin', 'cos', 'tan', 'Sqrt', '1/x', 'pi', 'e', 'mod']:
        btn = Button(root, text=text, padx=25, pady=15, relief=RIDGE, fg="white", bg="black")
        btn.bind("<Button-1>", scientific_calculations)
    else:
        btn = Button(root, text=text, padx=25, pady=15, relief=RAISED, fg="white", bg="grey", command=lambda t=text: click(t))
    btn.grid(row=row, column=col)

# Run the Tkinter event loop
root.mainloop()
