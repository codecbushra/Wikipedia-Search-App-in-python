from tkinter import *
import wikipedia    
    
def onClick():
    q=get_q.get()    
    text.insert(INSERT,wikipedia.summary(q))

root=Tk()
root.title("Wikipedia Search App")
root.geometry("600x600")
titlelabel=Label(root,font='Helvetica 35 bold italic',text="Wikipedia Search App",fg='crimson')
titlelabel.pack()
question=Label(root,font=('Helvetica 16 bold italic'),text="Question",fg='deeppink')
question.pack()
get_q=Entry(root,bd=5)
get_q.pack()
submit=Button(root,font=('Helvetica 16 bold italic'),text="Search",fg='deeppink',command=onClick)
submit.pack()
text=Text(root)
text.pack()
   
root.mainloop()


