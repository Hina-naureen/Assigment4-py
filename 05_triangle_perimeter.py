import tkinter as tk
from tkinter import messagebox

# Function to calculate perimeter
def calculate_perimeter():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        c = float(entry3.get())
        perimeter = a + b + c
        result_label.config(text=f"🔹 Perimeter: {perimeter}")
    except ValueError:
        messagebox.showerror("Invalid Input", "❌ Please enter valid numbers for all sides.")

# Function to clear placeholder on focus
def clear_placeholder(event, entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, tk.END)
        entry.config(fg="#000000")

# GUI Window setup
root = tk.Tk()
root.title("🔺 Triangle Perimeter Calculator")
root.geometry("400x400")
root.config(bg="#f7fafd")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="🔺 Triangle Perimeter Calculator", font=("Segoe UI", 16, "bold"), bg="#f7fafd", fg="#333")
title_label.pack(pady=(20, 5))

# Divider line
divider = tk.Frame(root, height=2, bg="#cccccc", bd=0)
divider.pack(fill="x", padx=40, pady=(0, 20))

# Style for entries
entry_style = {"font": ("Segoe UI", 12), "justify": "center", "bg": "#ffffff", "fg": "#888", "relief": "solid", "bd": 1}

# Side 1 Entry
entry1 = tk.Entry(root, **entry_style)
entry1.insert(0, "Enter length of side 1")
entry1.bind("<FocusIn>", lambda event: clear_placeholder(event, entry1, "Enter length of side 1"))
entry1.pack(pady=8, ipadx=10, ipady=6)

# Side 2 Entry
entry2 = tk.Entry(root, **entry_style)
entry2.insert(0, "Enter length of side 2")
entry2.bind("<FocusIn>", lambda event: clear_placeholder(event, entry2, "Enter length of side 2"))
entry2.pack(pady=8, ipadx=10, ipady=6)

# Side 3 Entry
entry3 = tk.Entry(root, **entry_style)
entry3.insert(0, "Enter length of side 3")
entry3.bind("<FocusIn>", lambda event: clear_placeholder(event, entry3, "Enter length of side 3"))
entry3.pack(pady=8, ipadx=10, ipady=6)

# Calculate Button
calc_button = tk.Button(
    root,
    text="Calculate Perimeter",
    font=("Segoe UI", 12, "bold"),
    bg="#4caf50",
    fg="white",
    activebackground="#45a049",
    relief="flat",
    command=calculate_perimeter
)
calc_button.pack(pady=20, ipadx=10, ipady=5)

# Result Label
result_label = tk.Label(root, text="", font=("Segoe UI", 13), bg="#f7fafd", fg="#003366")
result_label.pack(pady=10)

# Footer
footer = tk.Label(root, text="© 2025 by YourName", font=("Segoe UI", 9), fg="#aaa", bg="#f7fafd")
footer.pack(side="bottom", pady=10)

# Run GUI
root.mainloop()
