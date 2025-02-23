import tkinter as tk

def calculate(operator):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                result = "Error! Division by zero."
            else:
                result = num1 / num2
        
        result_label.config(text=f"Result: {result}")
    
    except ValueError:
        result_label.config(text="Invalid input! Enter numbers.")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")

# Input fields
entry1 = tk.Entry(root)
entry1.pack(pady=5)

entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Buttons for operations
frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="+", command=lambda: calculate("+")).pack(side=tk.LEFT, padx=5)
tk.Button(frame, text="-", command=lambda: calculate("-")).pack(side=tk.LEFT, padx=5)
tk.Button(frame, text="*", command=lambda: calculate("*")).pack(side=tk.LEFT, padx=5)
tk.Button(frame, text="/", command=lambda: calculate("/")).pack(side=tk.LEFT, padx=5)
tk.Button(frame, text="reset", command=lambda: calculate("/")).pack(side=tk.LEFT, padx=5)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

# Run the application
root.mainloop()
