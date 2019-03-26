
from tkinter import *
from tkinter import ttk
from assignMembers import assign_members
import reports

main_file_path = 'C:\\Users\\Cyr1lfiggus1\\PycharmProjects\\SquadronReadinessPython\\'




def enable_text():
    firstEntry.config(state='normal')
    lastEntry.config(state='normal')

all_sfs_members = assign_members(main_file_path+'allSFSMembers.txt')
squad1 = assign_members(main_file_path+'SQUAD1.txt')
squad2 = assign_members(main_file_path+'SQUAD2.txt')
fire11 = assign_members(main_file_path+'fire1-1.txt')
fire12 = assign_members(main_file_path+'fire1-2.txt')
fire13 = assign_members(main_file_path+'fire1-3.txt')
fire14 = assign_members(main_file_path+'fire1-4.txt')
fire21 = assign_members(main_file_path+'fire2-1.txt')
fire22 = assign_members(main_file_path+'fire2-2.txt')
fire23 = assign_members(main_file_path+'fire2-3.txt')
fire24 = assign_members(main_file_path+'fire2-4.txt')

print(squad1)



root = Tk()
frame = Frame(root)
a = StringVar(value='indv')
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

fitness_report = []


def get_button_selected(a):
    selection = a.get()
    print('button pushed', selection)
    if selection == 'squad1':
        fitness_report = reports.process_fitness(squad1, main_file_path+'Fitness.xls')
        print(fitness_report)


process_button = Button(root, text='Process reports', command=lambda: get_button_selected(a))


process_button.grid(row=5)
# button = Button(frame, text='b1').pack(side=LEFT, fill=Y)
# button = Button(frame, text='b2').pack(side=TOP, fill=X)
# button = Button(frame, text='b3').pack(side=RIGHT, fill=X)
# button = Button(frame, text='b4').pack(side=BOTTOM, fill=X)





root.title('Squadron Readiness')
root.mainloop()
