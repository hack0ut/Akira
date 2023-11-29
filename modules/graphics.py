from tkinter import messagebox


def info(text: str):
    messagebox.showinfo("Akira ", text)


def error(text: str):
    messagebox.showerror("Akira ", text)


def warning(text: str):
    messagebox.showwarning("Akira", text)
