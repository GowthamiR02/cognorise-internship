import time
import tkinter as tk

def countdown():
    if remaining_time := int(entry.get()):
        for i in range(remaining_time, -1, -1):
            time.sleep(1)
            label.config(text=i)
            root.update()
    label.config(text="Time's up!")

root = tk.Tk()
root.title("Countdown Timer")

label = tk.Label(root, font=("Helvetica", 48))
label.pack(padx=20, pady=20)

entry = tk.Entry(root, font=("Helvetica", 24))
entry.pack(padx=20, pady=20)

button = tk.Button(root, text="Start Countdown", command=countdown)
button.pack(padx=20, pady=20)

root.mainloop()