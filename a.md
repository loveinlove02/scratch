```python
import tkinter as tk

win = tk.Tk()
win.title('계산기')
win.geometry('570x600')
win.resizable(False, False)
win.configure(bg='#17161b')

equation = ''

def clear():
    global equation
    equation = ''
    lable_result.configure(text=equation)

def show(value):
    global equation
    equation = equation + value
    lable_result.configure(text=equation)

# 계산 결과 레이블
lable_result = tk.Label(win, width=25, height=2, text='', font='arial 30')
lable_result.pack()

# 버튼 : C / % *
clear_button = tk.Button(win, text='C', width=5, height=1, font='arial 30', 
                         bd=1, fg='#ffffff', bg='#3697f5', command=clear)
clear_button.place(x=10, y=100)

div_button = tk.Button(win, text='/', width=5, height=1, font='arial 30', 
                       bd=1, fg='#ffffff', bg='#2a2d36', command=lambda: show('/'))
div_button.place(x=150, y=100) 

divmod_button = tk.Button(win, text='%', width=5, height=1, font='arial 30', 
                          bd=1, fg='#ffffff', bg='#2a2d36', command=lambda: show('%'))
divmod_button.place(x=290, y=100)

muiti_button = tk.Button(win, text='*', width=5, height=1, font='arial 30', 
                         bd=1, fg='#ffffff', bg='#2a2d36', command=lambda: show('*'))
muiti_button.place(x=430, y=100)

# 버튼: 7 8 9 -
num7_button   = tk.Button(win, text='7', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', 
                          command=lambda: show('7'))
num7_button.place(x=10, y=200)

num8_button   = tk.Button(win, text='8', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('8')).place(x=150, y=200)
num9_button   = tk.Button(win, text='9', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('9')).place(x=290, y=200)
minus_button  = tk.Button(win, text='-', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('-')).place(x=430, y=200)


# 버튼 : 4 5 6 +
num4_button   = tk.Button(win, text='4', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('4')).place(x=10, y=300)
num5_button   = tk.Button(win, text='5', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('5')).place(x=150, y=300)
num6_button   = tk.Button(win, text='6', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('6')).place(x=290, y=300)
plus_button   = tk.Button(win, text='+', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('+')).place(x=430, y=300)

# 버튼: 1 2 3 0
num1_button   = tk.Button(win, text='1', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('1')).place(x=10, y=400)
num2_button   = tk.Button(win, text='2', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('2')).place(x=150, y=400)
num3_button   = tk.Button(win, text='3', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('3')).place(x=290, y=400)

num0_button  = tk.Button(win, text='0', width=11, height=1, 
                         font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('0'))
num0_button.place(x=10, y=500)

# . =
dot_button = tk.Button(win, text='.', width=5, height=1, font=('arial', 30, 'bold'), 
                       bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('.'))
dot_button.place(x=290, y=500)

equal_button = tk.Button(win, text='=', width=5, height=3, font=('arial', 30, 'bold'), 
                         bd=1, fg='#fff', bg='#fe9037')
equal_button.place(x=430, y=400)

win.mainloop()
```
