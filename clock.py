import tkinter
import time


def display_time():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    my_window.after(200, display_time)  # Trigger after every 200ms


my_window = tkinter.Tk()
my_window.title("Current Time")
clock_label = tkinter.Label(my_window, font='ariel 80', bg='black', fg='red')
clock_label.pack()
display_time()
my_window.mainloop()
