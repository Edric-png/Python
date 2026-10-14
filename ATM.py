import tkinter as tk
root = tk.Tk()
root.title("ATM PIN Setup")
root.geometry("300x400")
f = tk.Frame(root, relief="raised", bd=3)
f.pack(pady=10)
tk.Label(f, text="Account:").grid(row=0, column=0)
a = tk.Entry(f)
a.grid(row=0, column=1)
tk.Label(f, text="PIN:").grid(row=1, column=0)
p = tk.Entry(f, show="*")
p.grid(row=1, column=1)
k = tk.Frame(root, relief="sunken", bd=3)
k.pack()
for i in range(10):
    tk.Button(k, text=str(i),
              command=lambda n=i: p.insert(tk.END, str(n))
              ).grid(row=i//3, column=i%3)
t = tk.Text(root, height=3, width=30)
t.pack()
def submit():
    t.insert(tk.END, "Account: " + a.get() + "\nPIN setup complete!")
tk.Button(root, text="Submit", command=submit).pack()
root.mainloop()