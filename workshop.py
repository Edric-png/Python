import tkinter as tk

w = tk.Tk()
w.title("Workshop Greeting")

tk.Label(w, text="Enter your name:").pack()
e = tk.Entry(w)
e.pack()

t = tk.Text(w, height=5, width=40)
t.pack()

def check():
    t.delete("1.0", tk.END)
    t.insert(tk.END, f"Welcome, {e.get()}!\nWorkshop Date: August 26, 2026")

tk.Button(w, text="Check In", command=check).pack()
w.mainloop()