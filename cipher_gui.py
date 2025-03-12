import tkinter as tk
from tkinter import messagebox

# Caesar Cipher Function
def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    if mode == "decrypt":
        shift = -shift  

    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  
    
    return result

# Encrypt/Decrypt Function
def process_text(mode):
    message = entry_text.get()
    try:
        shift_value = int(entry_shift.get())
        if mode == "encrypt":
            result = caesar_cipher(message, shift_value, mode="encrypt")
        else:
            result = caesar_cipher(message, shift_value, mode="decrypt")
        
        output_label.config(text=f"Result: {result}")
        copy_button.config(state="normal")  # Enable Copy Button
    except ValueError:
        messagebox.showerror("Error", "Shift value must be a number!")

# Copy to Clipboard
def copy_to_clipboard():
    result_text = output_label.cget("text").replace("Result: ", "")
    root.clipboard_clear()
    root.clipboard_append(result_text)
    root.update()
    messagebox.showinfo("Copied", "Result copied to clipboard!")

# Clear All Fields
def clear_fields():
    entry_text.delete(0, tk.END)
    entry_shift.delete(0, tk.END)
    output_label.config(text="Result: ")
    copy_button.config(state="disabled")  # Disable Copy Button

# GUI Setup
root = tk.Tk()
root.title("Caesar Cipher Tool")
root.geometry("500x400")
root.configure(bg="white")

# Labels
tk.Label(root, text="Enter Message:", bg="white", fg="black", font=("Arial", 14)).pack(pady=5)
entry_text = tk.Entry(root, width=50, font=("Arial", 14), bd=2, relief="solid")
entry_text.pack(pady=5)

tk.Label(root, text="Enter Shift Value:", bg="white", fg="black", font=("Arial", 14)).pack(pady=5)
entry_shift = tk.Entry(root, width=10, font=("Arial", 14), bd=2, relief="solid")
entry_shift.pack(pady=5)

# Buttons
button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=10)

encrypt_button = tk.Button(button_frame, text="🔒 Encrypt", command=lambda: process_text("encrypt"), bg="#4CAF50", fg="white", font=("Arial", 14), width=12)
encrypt_button.grid(row=0, column=0, padx=5)

decrypt_button = tk.Button(button_frame, text="🔓 Decrypt", command=lambda: process_text("decrypt"), bg="#f39c12", fg="white", font=("Arial", 14), width=12)
decrypt_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(button_frame, text="🧹 Clear", command=clear_fields, bg="#e74c3c", fg="white", font=("Arial", 14), width=12)
clear_button.grid(row=0, column=2, padx=5)

# Output Label
output_label = tk.Label(root, text="Result: ", bg="white", fg="black", font=("Arial", 16, "bold"), wraplength=450, justify="center")
output_label.pack(pady=20)

# Copy to Clipboard Button
copy_button = tk.Button(root, text="📋 Copy", command=copy_to_clipboard, bg="#3498db", fg="white", font=("Arial", 14), width=12, state="disabled")
copy_button.pack()

# Run the GUI
root.mainloop()
