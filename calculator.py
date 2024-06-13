from customtkinter import *

set_appearance_mode('dark')
set_default_color_theme('blue')

win = CTk()

win.title('Calculator')
win.geometry('300x350')

CurrentValue = StringVar(value='0')

def Update(val):
    CurrentValue.set(val)

def PressButton(val):
    cur = CurrentValue.get()
    if cur=='0':
        cur = val
    else:
        cur+=val
    Update(cur)

def clear():
    CurrentValue.set(value='0')

def CalculateResult():
    cur = CurrentValue.get()
    if 'x' in cur:
        cur = [i for i in cur]
        ind = cur.index('x')
        cur[ind] = '*'
        cur = ''.join(cur)
  
    try:
        result = eval(cur)
    except Exception as e:
        result = e
    Update(result)
    return result
    
def UpdatedResult():
    r = CalculateResult()
    r *= -1
    Update(r)

    
def square():
    cur = int(CurrentValue.get())
    result = str(cur**2)
    Update(result) 

def back():
    cur = CurrentValue.get()
    cur = [i for i in cur]
    cur[len(cur)-1]=''
    cur = ''.join(cur)
    Update(cur)     

DisplayFrame = CTkFrame(master=win,width=300,height=100,corner_radius=0)
DisplayFrame.place(relx=0,rely=0)

ButtonFrame = CTkFrame(master=win,width=300,height=250,corner_radius=0)
ButtonFrame.place(relx=0,rely=0.28)

buttons = [
    ('C', 0, 0), ('x^2', 0, 1), ('<--', 0, 2), ('+', 0, 3),
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('-', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('x', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('/', 3, 3),
    ('~', 4, 0), ('0', 4, 1), ('.', 4, 2), ('=', 4, 3)
]

Display = CTkEntry(DisplayFrame,width=300,height=100,fg_color='transparent',border_color='#2A2A2B',textvariable=CurrentValue,state=DISABLED,justify='right',font=('Arial',24))
Display.place(relx=0,rely=0)

for (txt,r,c) in buttons:
    if txt=='C':
        but = CTkButton(ButtonFrame,text= txt,width=75,height=50,corner_radius=5,font=('roboto',15),command = clear)
    elif txt=='=':
        but = CTkButton(ButtonFrame,text= txt,width=75,height=50,corner_radius=5,font=('roboto',15),command = lambda: CalculateResult())
    elif txt=='x^2':
        but = CTkButton(ButtonFrame,text= txt,width=75,height=50,corner_radius=5,font=('roboto',15),command = square)
    elif txt=='<--':
        but = CTkButton(ButtonFrame,text= txt,width=75,height=50,corner_radius=5,font=('roboto',15),command = back)
    elif txt=='~':
        but = CTkButton(ButtonFrame,text= txt,width=75,height=50,corner_radius=5,font=('roboto',15),command = UpdatedResult)
    else:
        but = CTkButton(ButtonFrame,text= txt,width=75,height=50,corner_radius=5,font=('roboto',15),command =lambda t=txt: PressButton(t))
    but.grid(row= r,column= c,pady=0.4,padx=0.4)
    


win.mainloop()