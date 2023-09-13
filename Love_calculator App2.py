from tkinter import *
import random
import hashlib

root = Tk()
root.geometry('400x240')
root.title('LOVE 0__0 calculator')

def calculate_love():                                    #plesh thish full whatch thish program video plesh  subscrebe thish video
                                                             #coding line 77  name love calculater THANK YOU THISH VIDEO
    name1_str = name1.get().lower()
    name2_str = name2.get().lower()
    combined_names = name1_str + 'loves' + name2_str
    love_score = int(hashlib.sha256(combined_names.encode()).hexdigest(), 16) % 101
    
    result.config(text=str(love_score))


#b1= Label(root, text='sasikumar python',fg='red',height=50,width=50,font=('arail',10,'bold',))
#b1.place(x=20,y=10)
#b1.place(x=315,y=200)

b4Photo = PhotoImage(file='as.PNG')
b4=b3=Label(root,font="Times 200 bold",image=b4Photo ,bg='#FF1493',fg='white',height=1000,width=1000)
b4.grid(row=70,column=70,padx=70,pady=70,sticky='snew')
b4.place(x=-450,y=-375)

b2Photo = PhotoImage(file='uu.PNG')
b2=Label(root,font="Times 200 bold",image=b2Photo ,bg='#FF1493',fg='#030303',height=100,width=100)
b2.grid(row=50,column=50,padx=50,pady=50,sticky='snew')
b2.place(x=270,y=10)



b3Photo = PhotoImage(file='ftyui.PNG')
b3=Label(root,font="Times 200 bold",image=b3Photo ,bg='#FF1493',fg='#030303',height=100,width=100)
b3.grid(row=55,column=55,padx=55,pady=55,sticky='snew')
b3.place(x=270,y=100)


b5Photo = PhotoImage(file='nn.PNG')
b5=Label(root,font="Times 200 bold",image=b5Photo ,bg='#A52A2A',fg='#030303',height=80,width=100)
b5.grid(row=80,column=80,padx=80,pady=80,sticky='snew')
b5.place(x=150,y=170)



heading = Label(root, text='love calculator',bg='#FF1493',fg='#030303',height=0,width=13,font=('arail',10,'bold'))
heading .grid(row=70,column=70,padx=70,pady=70)
heading .place(x=315,y=100)
heading.pack()

slot1 = Label(root, text="enter your name:",bg='#FF1493',fg='#030303',height=0,width=15,font=('arail',10,'bold'))
slot1.pack()
name1 = Entry(root, border=5)
name1.pack()

slot2 = Label(root, text="enter your partner name:",bg='#FF1493',fg='#030303',height=0,width=20,font=('arail',10,'bold'))
slot2.pack()
name2 = Entry(root, border=5)
name2.pack()

result = Label(root, text="",bg='#0000FF',fg='#030303',height=0,width=5,font=('arail',10,'bold'))
result.pack()

btn = Button(root, text="calculate", command=calculate_love,bg='#0000FF',fg='#030303',height=1,width=10,font=('arail',10,'bold'))
heading .place(x=800,y=600)
heading.pack()
btn.pack()

root.config(bg='#FF1493')
root.mainloop()
