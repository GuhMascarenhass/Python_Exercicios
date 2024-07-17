from tkinter import *
import webbrowser

app = Tk()

frame = Frame(app)
frame.pack()

url = "https://pt.duolingo.com/"


def OpenUrl():
    webbrowser.open_new(url)


button = Button(frame, text="Duolingo PT", command=lambda aurl=url: OpenUrl())
button.pack(side="left", padx=20, pady=20)

app.mainloop()
