from tkinter import *
from tkinter import messagebox
import random
import time


class Puzzle(Tk):
    numbers = [i for i in range(1, 10)]
    random.shuffle(numbers)
    numbers[numbers.index(9)] = numbers[0]
    numbers2 = [i for i in range(1, 10)]
    numbers2.reverse()
    easy_solution = [9, 5, 7, 8, 6, 4, 3, 2, 1]

    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk",
                 useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.title('8 PUZZLE GAME')
        self.geometry(f'484x694+{self.width // 2 - 242}+{self.height // 2 - 346}')
        self.iconbitmap("E:\\mahdi\\python projects\\GUI 8 puzzle ICON.ico")
        self.resizable(0, 0)
        self.config(bg='black')

        for i in range(1, 4):
            for j in range(1, 4):
                a = Button(self, text=Puzzle.numbers2.pop(), font=('Arial', 21, 'bold'), width=9, height=5, border=1,
                           bg='#5D2E1E', fg='#D2AF68', activebackground='#5D2E1E', activeforeground='#D2AF68',
                           state='disable')
                a.grid(row=i, column=j)
        a.config(text='')
        a.config(bg='black')
        Puzzle.numbers2 = [i for i in range(1, 10)]
        Puzzle.numbers2.reverse()

        self.start = Button(self, text='SHUFFLE !!', font=('GAbriola', 24, 'bold'), bg='#5D2E1E', fg='#D2AF68',
                            width=17, borderwidth=4, command=self.lets_go)
        self.start.grid(row=4, column=0, columnspan=300, pady=10)
        self.mainloop()

    def lets_go(self):
        global a
        for i in range(1, 4):
            for j in range(1, 4):
                a = Button(self, text=f'{Puzzle.numbers.pop()}', font=('Arial', 21, 'bold'), width=9, height=5,
                           border=1, bg='#5D2E1E', fg='#D2AF68', activebackground='#5D2E1E', activeforeground='#D2AF68')
                a.grid(row=i, column=j)
                j = Puzzle.numbers2.pop()
                globals()['btn%s' % j] = a
        Puzzle.numbers = [i for i in range(1, 10)]
        random.shuffle(Puzzle.numbers)
        Puzzle.numbers[Puzzle.numbers.index(9)] = Puzzle.numbers[0]
        btn9.config(text='')
        btn9.config(bg='black')
        btn9.config(activebackground='black')
        btn9.config(state='disable')
        Puzzle.numbers2 = [i for i in range(1, 10)]
        Puzzle.numbers2.reverse()
        btn1.config(command=lambda: self.swap(btn1))
        btn2.config(command=lambda: self.swap(btn2))
        btn3.config(command=lambda: self.swap(btn3))
        btn4.config(command=lambda: self.swap(btn4))
        btn5.config(command=lambda: self.swap(btn5))
        btn6.config(command=lambda: self.swap(btn6))
        btn7.config(command=lambda: self.swap(btn7))
        btn8.config(command=lambda: self.swap(btn8))
        btn9.config(command=lambda: self.swap(btn9))

    def swap(self, value):
        names = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]

        for i in range(len(names)):
            if names[i].cget('text') == '':
                t1 = names[i].cget('text')
                t2 = value.cget('text')
                c1 = names[i].cget('bg')
                c2 = value.cget('bg')
                s1 = names[i].cget('state')
                s2 = value.cget('state')
                cWhite = names[i].cget('activebackground')
                cValue = value.cget('activebackground')
                x1 = names[i].grid_info()['row']
                y1 = names[i].grid_info()['column']
                x2 = value.grid_info()['row']
                y2 = value.grid_info()['column']

                if x2 + y2 != (x1 + y1) + 1 and x2 + y2 != (x1 + y1) - 1:
                    messagebox.showerror('INVALID BUTTON', 'Select buttons that are next to the empty button :) ')
                    return

                elif x2 != x1 and y2 != y1:
                    messagebox.showerror('INVALID BUTTON', 'Select buttons that are next to the empty button :) ')
                    return

                else:
                    value.config(text=t1)
                    value.config(bg=c1)
                    value.config(activebackground=cWhite)
                    value.config(state=s1)
                    names[i].config(text=t2)
                    names[i].config(bg=c2)
                    names[i].config(activebackground=cValue)
                    names[i].config(state=s2)

                    time.sleep(0.1)
                    if btn1.cget('text') == '1' and btn2.cget('text') == '2' and btn3.cget('text') == '3' and btn4.cget(
                            'text') == '4' and btn5.cget('text') == '5' and btn6.cget('text') == '6' and btn7.cget(
                            'text') == '7' and btn8.cget('text') == '8' and btn9.cget('text') == '':
                        messagebox.showinfo('WIN', """WoWwWw !!! you wonnn !!!
                                        Click on ( SHUFFLE !! ) to start again""")
                    return


game = Puzzle()
