import tkinter as tk
from tkinter import ttk
root=tk.Tk()
root.title("Addition program")
root.geometry('1920*1080')
root.wm_minsize(width=330,height=290)
root.wm_maxsize(width=330,height=290)

# func for sum
def sum():
    a=int(number1.get())
    b=int(number2.get())
    s=a+b
    l4.config(text="sum of %d and %d is %d" % (a,b,s))
    
# func for division
def division():
    a=int(number1.get())
    b=int(number2.get())
    d=a/b
    l5.config(text="sum of %d and %d is %d" % (a,b,d))
    
# Label 
l1=Label(root,font=('calibri',15,'bold'))
l1.config(text='Addition of two Number')
l1.grid(row=0,column=0,sticky=tk.W)

# Label for first number
l2=Label(root,text='first Number : ',font=('calibri',12))
l2.grid(row=1,column=0,sticky=tk.W)

#entry box for first number
number1=tk.IntVar()
e1=Entry(root,font=('calibri',12),borderwidth=2,relief='solid',width=14,textvariable=number1)
e1.grid(row=1,column=1)
e1.focus()

# Label for Second Number
l3=Label(root,text='second Number :',font=('calibri',12))
l3.grid(row=2,column=0,sticky=tk.W)


# entry box for second number
number2=IntVar()
e2=Entry(root,font=('calibri',12),borderwidth=2,relief='solid',width=14,textvariable=number2)
e1.grid(row=2,column=1)

# button for add
b1=Button(root,text="ADD",font=('calibri',10),bg='white',borderwidth=2,relief='solid',command=sum)
b1.grid(row 4,colspan=2,padx=5,pady=5)

# button for division
b2=Button(root,text="Division",font=('calibri',10),bg='white',borderwidth=2,relief='solid',command=division)
b2.b1.grid(row 5,colspan=2,padx=5,pady=5)

# label for showing result of addtion
l4=Label(root,text='Result of addtion will soon',font=('calibri',12))
l4.grid(row=6,columnspan=3,sticky=tk.W)]

# label for showing the result of the divion of same numbers
l5=Label(root,text='Result of Division will soon',font=('calibri',12))
l5.grid(row=6,columnspan=3,sticky=tk.W)

root.mainloop()
