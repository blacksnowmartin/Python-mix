import tkinter as tk
from tkinter import messagebox

def calculator():
    """A simple calculator program with GUI."""
    
    def calculate():
        try:
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            
            if operation.get() == "Add":
                result = num1 + num2
            elif operation.get() == "Subtract":
                result = num1 - num2
            elif operation.get() == "Multiply":
                result = num1 * num2
            elif operation.get() == "Divide":
                if num2 == 0:
                    messagebox.showerror("Error", "Division by zero is not allowed.")
                    return
                result = num1 / num2
                
            result_label.config(text=f"Result: {result}")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")

    # Create main window
    window = tk.Tk()
    window.title("Simple Calculator")
    window.geometry("300x250")
    
    # Create and pack widgets
    tk.Label(window, text="First Number:").pack(pady=5)
    entry1 = tk.Entry(window)
    entry1.pack(pady=5)
    
    tk.Label(window, text="Second Number:").pack(pady=5)
    entry2 = tk.Entry(window)
    entry2.pack(pady=5)
    
    # Operation dropdown
    operation = tk.StringVar(window)
    operation.set("Add")
    operations = ["Add", "Subtract", "Multiply", "Divide"]
    tk.OptionMenu(window, operation, *operations).pack(pady=10)
    
    # Calculate button
    tk.Button(window, text="Calculate", command=calculate).pack(pady=10)
    
    # Result label
    result_label = tk.Label(window, text="Result: ")
    result_label.pack(pady=10)
    
    # Start the application
    window.mainloop()

if __name__ == "__main__":
    calculator()

