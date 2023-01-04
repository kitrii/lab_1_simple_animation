from math import sin, radians, cos
from time import strftime
from tkinter import *

window = Tk()
canvas = Canvas(window, width=400, height=400, bg="black")
canvas.grid()


def track_time(hour, minute, second):

    canvas.create_oval(40, 40, 350, 350, fill="black")

    line_hour = canvas.create_line(200, 200,
                                   200 + 70 * sin(radians(hour)),
                                   200 - 70 * cos(radians(hour)),
                                   width=6,
                                   fill="#40f759",
                                   arrow=LAST)

    line_minute = canvas.create_line(200, 200,
                                     200 + 80 * sin(radians(minute)),
                                     200 - 80 * cos(radians(minute)),
                                     fill="#ee40f7",
                                     width=6,
                                     arrow=LAST)
    line_second = canvas.create_line(200, 200,
                                     200 + 100 * sin(radians(second)),
                                     200 - 100 * cos(radians(second)),
                                     fill="#9f40f7",
                                     width=6,
                                     arrow=LAST)
    circle = canvas.create_oval(195, 195, 205, 205, fill="white")



def time():
    h = int(strftime('%H'))
    m = int(strftime('%M'))
    s = int(strftime('%S'))

    hr = (h / 12) * 360
    mi = (m / 60) * 360
    se = (s / 60) * 360

    track_time(hr, mi, se)
    canvas.after(1000, time)


time()
window.mainloop()
