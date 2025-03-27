import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip  


def generate_password(length, use_upper, use_lower, use_digits, use_punctuation):
    characters = ""

    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation

    if not characters:
        return "請至少選擇一個字符集"

    password = "".join(random.choice(characters) for i in range(length))
    return password


def generate():
    try:
        length = int(entry_length.get())  
    except ValueError:
        messagebox.showerror("錯誤", "請輸入有效的整數數字作為密碼長度！")
        return

    use_upper = check_upper.get()  
    use_lower = check_lower.get()  
    use_digits = check_digits.get() 
    use_punctuation = check_punctuation.get() 

    password = generate_password(
        length, use_upper, use_lower, use_digits, use_punctuation
    )

    label_result.config(text="生成的密碼是: " + password)


def copy_to_clipboard():
    password = label_result.cget("text").replace("生成的密碼是: ", "")  

    if password == "":
        messagebox.showerror("錯誤", "請生成密碼！")  
    else:
        pyperclip.copy(password)  
        messagebox.showinfo("已複製", "密碼已複製！")  


window = tk.Tk()
window.title("密碼生成器")

label_length = tk.Label(window, text="請輸入密碼長度: ")
label_length.grid(row=0, column=0, padx=5, pady=5)

entry_length = tk.Entry(window)
entry_length.grid(row=0, column=1, padx=5, pady=5)

check_upper = tk.BooleanVar()
check_upper.set(True) 
checkbox_upper = tk.Checkbutton(window, text="包含大寫字母", variable=check_upper)
checkbox_upper.grid(row=1, column=0, padx=5, pady=5, sticky="w")

check_lower = tk.BooleanVar()
check_lower.set(True) 
checkbox_lower = tk.Checkbutton(window, text="包含小寫字母", variable=check_lower)
checkbox_lower.grid(row=2, column=0, padx=5, pady=5, sticky="w")

check_digits = tk.BooleanVar()
check_digits.set(True) 
checkbox_digits = tk.Checkbutton(window, text="包含數字", variable=check_digits)
checkbox_digits.grid(row=3, column=0, padx=5, pady=5, sticky="w")

check_punctuation = tk.BooleanVar()
check_punctuation.set(True) 
checkbox_punctuation = tk.Checkbutton(
    window, text="包含特殊符號", variable=check_punctuation
)
checkbox_punctuation.grid(row=4, column=0, padx=5, pady=5, sticky="w")

button_generate = tk.Button(window, text="生成密碼", command=generate)
button_generate.grid(row=5, column=0, columnspan=2, pady=10)

label_result = tk.Label(window, text="生成的密碼是: ")
label_result.grid(row=6, column=0, columnspan=2, pady=5)

button_copy = tk.Button(window, text="複製密碼", command=copy_to_clipboard)
button_copy.grid(row=7, column=0, columnspan=2, pady=10)

window.mainloop()
