import tkinter as tk
from tkinter import filedialog


win = tk.Tk()
win.title('일정관리')
win.geometry('400x650')
win.resizable(False, False)

task_list = []

def openTaskFile():
    
    try:
        global task_list

        file = open('taskfile.txt', 'r', encoding='utf-8')
        tasks = file.readlines() # 리스트
        file.close()

        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(tk.END, task)
    
    except:
        file = open('taskfile.txt', 'w', encoding='utf-8')
        file.close()
        
def add_task():
    global task_list
    
    task = task_entry.get()
    task = task.strip()
    task_entry.delete(0, tk.END)

    if task:
        file = open('taskfile.txt', 'a', encoding='utf-8') 
        file.write(f'\n{task}') 
        file.close()

        task_list.append(task)
        listbox.insert(tk.END, task)

# 아이콘
image_icon = tk.PhotoImage(file='image/task.png')
win.iconphoto(False, image_icon)

# 타이틀 이미지
top_image = tk.PhotoImage(file='image/topbar.png')
top_image_label = tk.Label(win, image=top_image)
top_image_label.pack()

# dock 이미지
dock_image = tk.PhotoImage(file='image/dock.png')
dock_image_label = tk.Label(win, image=dock_image, bg='#32405B')
dock_image_label.place(x=30, y=25)

# note 이미지
note_image = tk.PhotoImage(file='image/task.png')
note_image_label = tk.Label(win, image=note_image, bg='#32405B')
note_image_label.place(x=340, y=25)

# 제목
heading_label = tk.Label(win, text='ALL TASK', font='arial 20 bold', 
                         fg='#FFFFFF', bg='#32405B') 
heading_label.place(x=130, y=20)

# main 
frame = tk.Frame(win, width=400, height=50, bg='#FFFFFF')
frame.place(x=0, y=180)

# 할일 입력
task_entry = tk.Entry(frame, width=18, font='arial 20', bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

# 할일 등록 버튼
button = tk.Button(frame, text='ADD', font='arial 20 bold', 
                   fg='#FFFFFF', bg='#5a95ff', command=add_task)
button.place(x=300, y=0)

# 리스트 박스, 스크롤바 프레임
frame1 = tk.Frame(win, width=700, height=280, bg='#32405B')
frame1.place(x=0, y=243)

# 리스트박스
listbox = tk.Listbox(frame1, font=('arial', 12), width=40, height=16, 
                     bg='#32405B', fg='#FFFFFF', cursor='hand2', 
                     selectbackground='#5a95ff')

listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=2)

# 스크롤 바
scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

delete_image = tk.PhotoImage(file='image/delete.png')
delete_button = tk.Button(win, image=delete_image, bd=0) 
delete_button.place(x=165, y=580)



win.mainloop()
