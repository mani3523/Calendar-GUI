from tkinter import *
import calendar

class Quitter(Button):
    def __init__(self, parent=None, **config):
        super().__init__(parent, config)
        self.config(text='Quit', command=self.quit)
    
    def quit(self):
        self.master.destroy()

def showCalendar():
    gui = Tk()
    gui.config(background='light cyan')
    gui.title("Calendar for the year")
    gui.geometry("1080x2160")
    year = int(year_field.get())
    gui_content = calendar.calendar(year)
    calYear = Label(gui, text=gui_content, font="Consolas 10 bold")
    calYear.grid(row=5, column=1, padx=30)
    gui.mainloop()

if __name__ == '__main__':
    new = Tk()
    new.config(background='grey')
    new.title("Calendar")
    new.geometry("250x140")
    cal = Label(new, text="Calendar", bg='grey', font=("times", 50, "bold"))
    year = Label(new, text="Enter year", bg='dark grey')
    year_field = Entry(new)
    button = Button(new, text='Show Calendar', fg='White', bg='Blue', command=showCalendar)
    quit_button = Quitter(new)
    
    # putting widgets in position
    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    button.grid(row=4, column=1)
    quit_button.grid(row=5, column=1)
    
    new.mainloop()

                    