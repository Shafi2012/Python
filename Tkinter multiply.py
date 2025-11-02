import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Getting Started with Tkinter")
root.geometry("400x300")  # width=400, height=300

# Add a label to describe the functionality
lbl_title = tk.Label(root, text="This app multiplies two numbers", font=("Arial", 12, "bold"), fg="blue")
lbl_title.pack(pady=10)

# Labels for asking user input
lbl_num1 = tk.Label(root, text="Enter first number:")
lbl_num1.pack()

entry_num1 = tk.Entry(root)
entry_num1.pack()

lbl_num2 = tk.Label(root, text="Enter second number:")
lbl_num2.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

# Text box to display result
txt_result = tk.Text(root, height=2, width=25)
txt_result.pack(pady=10)

# Function to calculate product
def calculate_product():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        product = num1 * num2
        txt_result.delete("1.0", tk.END)
        txt_result.insert(tk.END, f"Product: {product}")
    except ValueError:
        txt_result.delete("1.0", tk.END)
        txt_result.insert(tk.END, "Please enter valid numbers!")

# Button to trigger calculation
btn_calculate = tk.Button(root, text="Calculate Product", command=calculate_product, bg="lightgreen")
btn_calculate.pack(pady=10)

# Run the main loop
root.mainloop()

