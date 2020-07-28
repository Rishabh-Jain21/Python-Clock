from datetime import date
import tkinter
import winsound
import time
import datetime

global endTime


h, m, s = map(int, input("Enter hour minute second for timer: ").split())
endTime = datetime.datetime.now()+datetime.timedelta(hours=h, minutes=m, seconds=s)


def quit(*args):
    root.destroy()


def cant_wait():
    timeleft = endTime-datetime.datetime.now()
    timeleft = timeleft-datetime.timedelta(microseconds=timeleft.microseconds)
    if timeleft < datetime.timedelta(0):
        lbl.config(text="Timeout")
        myalarm()
    else:
        lbl.config(text=timeleft)
        root.after(200, cant_wait)


def myalarm():
    frequebcy = 2500  # 25
    duration = 2000  # 1000ms=1s
    winsound.Beep(frequebcy, duration)


root = tkinter.Tk()
root.bind("x", quit)
lbl = tkinter.Label(root, font='ariel 80', bg='black', fg='red')
lbl.config(text=endTime-datetime.datetime.now())
root.after(200, cant_wait)
lbl.pack()
root.mainloop()
