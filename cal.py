
import tkinter as tk
from tkinter import ttk

def calculate():
    try:
        # Get values from entry boxes
        n = float(entry_n.get())
        m = float(entry_m.get())
        
        # Clear previous results
        for widget in result_frame.winfo_children():
            widget.destroy()
            
        # Perform calculations and define labels
        operations = [
            (f"{n} + {m}", n + m, "Sum"),
            (f"{n} - {m}", n - m, "Difference"),
            (f"{n} * {m}", n * m, "Product"),
            (f"{n} / {m}", n / m if m != 0 else "Error (Div by 0)", "Quotient"),
            (f"{n} // {m}", n // m if m != 0 else "Error (Div by 0)", "Floor Division"),
            (f"{n} % {m}", n % m if m != 0 else "Error (Div by 0)", "Modulus"),
            (f"{n} ** {m}", n ** m if safe_exponent(n, m) else "Result too large", "Exponentiation")
        ]
        
        # Display results in a neat grid
        for i, (expr, res, name) in enumerate(operations):
            ttk.Label(result_frame, text=f"{name}:", font=('Helvetica', 10, 'bold')).grid(row=i, column=0, sticky='w', pady=2)
            ttk.Label(result_frame, text=f"The {name} of {n} and {m} is {res}").grid(row=i, column=1, sticky='w', padx=10, pady=2)
            
    except ValueError:
        # Error handling for invalid inputs
        for widget in result_frame.winfo_children():
            widget.destroy()
        ttk.Label(result_frame, text="Please enter valid numbers for n and m.", foreground="red").pack()

def safe_exponent(n, m):
    # Prevents the program from crashing if the exponent result is too massive
    try:
        n ** m
        return True
    except OverflowError:
        return False

# --- GUI Setup ---
root = tk.Tk()
root.title("Math Operations GUI")
root.geometry("450x400")
root.resizable(False, False)

# Style configuration
style = ttk.Style()
style.theme_use('clam')

# Input Frame
input_frame = ttk.LabelFrame(root, text=" Inputs ", padding=15)
input_frame.pack(fill="x", padx=15, pady=10)

ttk.Label(input_frame, text="Enter n:").grid(row=0, column=0, sticky='w')
entry_n = ttk.Entry(input_frame, width=15)
entry_n.insert(0, "5") # Default value
entry_n.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(input_frame, text="Enter m:").grid(row=1, column=0, sticky='w')
entry_m = ttk.Entry(input_frame, width=15)
entry_m.insert(0, "10") # Default value
entry_m.grid(row=1, column=1, padx=5, pady=5)

# Calculate Button
calc_btn = ttk.Button(input_frame, text="Calculate", command=calculate)
calc_btn.grid(row=0, column=2, rowspan=2, padx=15, ipady=5)

# Results Frame
result_frame = ttk.LabelFrame(root, text=" Results ", padding=15)
result_frame.pack(fill="both", expand=True, padx=15, pady=10)

# Run initial calculation on load
calculate()

root.mainloop()
