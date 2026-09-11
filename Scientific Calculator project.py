import tkinter as tk
import math

# Create window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x650")
root.resizable(False, False)

# Display
display = tk.Entry(
    root,
    font=("Arial", 28),
    justify="right",
    bd=0
)
display.pack(fill="both", padx=15, pady=20, ipady=15)


# Functions
def press(value):
    display.insert(tk.END, value)


def clear():
    display.delete(0, tk.END)


def backspace():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])


def calculate():
    try:
        expression = display.get()
        expression = expression.replace("×", "*")
        expression = expression.replace("÷", "/")
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


def square():
    try:
        result = float(display.get()) ** 2
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.insert(tk.END, "Error")


def square_root():
    try:
        result = math.sqrt(float(display.get()))
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.insert(tk.END, "Error")


def sine():
    try:
        result = math.sin(math.radians(float(display.get())))
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.insert(tk.END, "Error")


def cosine():
    try:
        result = math.cos(math.radians(float(display.get())))
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.insert(tk.END, "Error")


def tangent():
    try:
        result = math.tan(math.radians(float(display.get())))
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.insert(tk.END, "Error")


def logarithm():
    try:
        result = math.log10(float(display.get()))
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.insert(tk.END, "Error")


# Button layout
buttons = [
    ["AC", "⌫", "%", "÷"],
    ["sin", "cos", "tan", "×"],
    ["√", "x²", "π", "−"],
    ["7", "8", "9", "+"],
    ["4", "5", "6", "("],
    ["1", "2", "3", ")"],
    ["00", "0", ".", "="]
]

# Create buttons
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")

    for button in row:

        if button == "AC":
            command = clear
        elif button == "⌫":
            command = backspace
        elif button == "=":
            command = calculate
        elif button == "√":
            command = square_root
        elif button == "x²":
            command = square
        elif button == "sin":
            command = sine
        elif button == "cos":
            command = cosine
        elif button == "tan":
            command = tangent
        elif button == "π":
            command = lambda: press(str(math.pi))
        elif button == "×":
            command = lambda: press("×")
        elif button == "÷":
            command = lambda: press("÷")
        elif button == "−":
            command = lambda: press("-")
        else:
            command = lambda x=button: press(x)

        tk.Button(
            frame,
            text=button,
            font=("Arial", 18),
            command=command,
            bd=0
        ).pack(
            side="left",
            expand=True,
            fill="both",
            padx=4,
            pady=4
        )

root.mainloop()