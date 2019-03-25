from tkinter import *
from tkinter import ttk


def enable_text():
    firstEntry.config(state='normal')
    lastEntry.config(state='normal')


root = Tk()
frame = Frame(root)
a = IntVar()
labelText = StringVar()
Label(root, text='First Name').grid(row=3, sticky=W, padx=4)
firstEntry = Entry(root)
firstEntry.grid(row=3, column=1, sticky=E, pady=4)
firstEntry.config(state='disabled')

Label(root, text='Last Name').grid(row=4, sticky=W, padx=4)
lastEntry = Entry(root)
lastEntry.grid(row=4, column=1, sticky=E, pady=4)
lastEntry.config(state='disabled')

Radiobutton(root, variable=a, text='Squad 1', value='squad1').grid(row=0, column=0)
Radiobutton(root, variable=a, text='Squad 2', value='squad2').grid(row=0, column=1)
Radiobutton(root, variable=a, text='CATM', value='catm').grid(row=0, column=2)
Radiobutton(root, variable=a, text='Indv.', value='indv', command=enable_text).grid(row=0, column=3)
Radiobutton(root, variable=a, text='Fire 1-1', value='fire11').grid(row=1, column=0)
Radiobutton(root, variable=a, text='Fire 1-2', value='fire12').grid(row=1, column=1)
Radiobutton(root, variable=a, text='Fire 1-3', value='fire13').grid(row=1, column=2)
Radiobutton(root, variable=a, text='Fire 1-4', value='fire14').grid(row=1, column=3)
Radiobutton(root, variable=a, text='Fire 2-1', value='fire21').grid(row=2, column=0)
Radiobutton(root, variable=a, text='Fire 2-2', value='fire22').grid(row=2, column=1)
Radiobutton(root, variable=a, text='Fire 2-3', value='fire23').grid(row=2, column=2)
Radiobutton(root, variable=a, text='Fire 2-4', value='fire24').grid(row=2, column=3)




Button(root, text='Process reports').grid(row=5)
# button = Button(frame, text='b1').pack(side=LEFT, fill=Y)
# button = Button(frame, text='b2').pack(side=TOP, fill=X)
# button = Button(frame, text='b3').pack(side=RIGHT, fill=X)
# button = Button(frame, text='b4').pack(side=BOTTOM, fill=X)

root.title('Squadron Readiness')
root.mainloop()
