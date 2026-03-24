import tkinter as tk
from tkinter import ttk
from googletrans import Translator

translator = Translator()

# Function to translate text
def translate_text():
    text = input_text.get("1.0", tk.END).strip()
    selected_lang = language_var.get()

    lang_dict = {
        "Urdu": "ur",
        "French": "fr",
        "Spanish": "es",
        "German": "de",
        "Arabic": "ar",
        "Hindi": "hi"
    }

    if text == "":
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Please enter text!")
        return

    try:
        translated = translator.translate(text, dest=lang_dict[selected_lang])
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated.text)
    except:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Translation failed. Check internet.")

# Function to copy text
def copy_text():
    text = output_text.get("1.0", tk.END).strip()
    if text:
        root.clipboard_clear()
        root.clipboard_append(text)

# Hover effects for button
def on_enter(e):
    translate_btn['bg'] = '#45a049'

def on_leave(e):
    translate_btn['bg'] = '#4CAF50'

# Create main window
root = tk.Tk()
root.title("AI-Powered Language Translator")
root.geometry("650x500")
root.configure(bg="#121212")

# Title
title = tk.Label(root, text="🌐 AI-Powered Language Translator",
                 font=("Segoe UI", 18, "bold"),
                 bg="#121212", fg="white")
title.pack(pady=15)

# Input section
tk.Label(root, text="Enter Text:",
         bg="#121212", fg="white", font=("Segoe UI", 11)).pack()

input_text = tk.Text(root, height=5, width=60,
                     bg="#1e1e1e", fg="white",
                     insertbackground="white",
                     relief="flat", bd=0,
                     padx=10, pady=10)
input_text.pack(pady=10)

# Frame for dropdown and button
frame = tk.Frame(root, bg="#121212")
frame.pack(pady=10)

# Language dropdown
language_var = tk.StringVar(value="Urdu")

dropdown = ttk.Combobox(frame, textvariable=language_var,
                        values=["Urdu", "French", "Spanish", "German", "Arabic", "Hindi"],
                        width=12)
dropdown.grid(row=0, column=0, padx=10)

# Translate button
translate_btn = tk.Button(frame, text="Translate",
                          bg="#4CAF50", fg="white",
                          font=("Segoe UI", 11, "bold"),
                          command=translate_text,
                          relief="flat", padx=15, pady=6)
translate_btn.grid(row=0, column=1, padx=10)

# Hover effect binding
translate_btn.bind("<Enter>", on_enter)
translate_btn.bind("<Leave>", on_leave)

# Output section
tk.Label(root, text="Translated Text:",
         bg="#121212", fg="white", font=("Segoe UI", 11)).pack()

output_text = tk.Text(root, height=5, width=60,
                      bg="#1e1e1e", fg="white",
                      insertbackground="white",
                      relief="flat", bd=0,
                      padx=10, pady=10)
output_text.pack(pady=10)

# Copy button
copy_btn = tk.Button(root, text="Copy",
                     bg="#2196F3", fg="white",
                     font=("Segoe UI", 11, "bold"),
                     command=copy_text,
                     relief="flat", padx=15, pady=6)
copy_btn.pack(pady=5)

# Run application
root.mainloop()