from codecs import BufferedIncrementalDecoder
from doctest import master
from textwrap import fill
import tkinter 

#--------------------------------------------------------------------------------------------------
screen=tkinter.Tk()
screen.configure(bg="black")
# screen.iconphoto(False,tkinter.PhotoImage('calcl_ogo.png'))

screen.geometry("400x550")
screen.maxsize(width=400,height=600)
screen.title("Siddhant's  calculator")
#------------------------------------------------------------------------------------------------------
show=tkinter.StringVar()
#------------------------------------------------------------------------------------------------------
# DISPLAY
en1=tkinter.Entry(master=screen,textvariable=show,font=("Times", "30", "bold italic"))
en1.grid(rowspan=3,columnspan=5,pady=2)
en1.focus_set()


#NUM PAD
but7=tkinter.Button(master=screen,text="7",width=15,height=4,fg="yellow",bg="black",cursor="plus",command=lambda :en1.insert("end",but7["text"]))
but7.grid(row=3,column=0,sticky="nw",pady=5)
but8=tkinter.Button(master=screen,text="8",width=15,height=4,fg="yellow",bg="black",cursor="plus",command=lambda :en1.insert("end",but8["text"]))
but8.grid(row=3,column=1,sticky="nw",pady=5)
but9=tkinter.Button(master=screen,text="9",width=15,height=4,fg="yellow",bg="black",cursor="plus",command=lambda :en1.insert("end",but9["text"]))
but9.grid(row=3,column=2,sticky="nw",pady=5)
but6=tkinter.Button(master=screen,text="6",width=15,height=4,fg="yellow",bg="black",cursor="plus",command=lambda :en1.insert("end",but6["text"]))
but6.grid(row=4,column=0,sticky="nw",pady=5)
but5=tkinter.Button(master=screen,text="5",width=15,height=4,fg="yellow",bg="black",cursor="plus",command=lambda :en1.insert("end",but5["text"]))
but5.grid(row=4,column=1,sticky="nw",pady=5)
but4=tkinter.Button(master=screen,text="4",width=15,height=4,fg="yellow",bg="black",cursor="plus",command=lambda :en1.insert("end",but4["text"]))
but4.grid(row=4,column=2,sticky="nw",pady=5)
but3=tkinter.Button(master=screen,text="3",width=15,height=4,fg="yellow",bg="black",cursor="plus",command=lambda :en1.insert("end",but3["text"]))
but3.grid(row=5,column=0,sticky="nw",pady=5)
but2=tkinter.Button(master=screen,text="2",width=15,height=4,fg="yellow",bg="black",cursor="plus",command=lambda :en1.insert("end",but2["text"]))
but2.grid(row=5,column=1,sticky="nw",pady=5)
but1=tkinter.Button(master=screen,text="1",width=15,height=4,fg="yellow",bg="black",cursor="plus",command=lambda :en1.insert("end",but1["text"]))
but1.grid(row=5,column=2,sticky="nw",pady=5)
but0=tkinter.Button(master=screen,text="0",width=15,height=4,fg="yellow",bg="black",cursor="plus",command=lambda :en1.insert("end",but0["text"]))
but0.grid(row=6,column=1,sticky="nw",pady=5)
dot=tkinter.Button(master=screen,text=".",width=15,height=4,fg="red",bg="black",cursor="plus",command=lambda :en1.insert("end",dot["text"]))
dot.grid(row=6,column=0,sticky="nw",pady=5)
#calcs
clear=tkinter.Button(master=screen,text="CE",width=15,height=4,fg="red",bg="black",cursor="hand1",command=lambda  :en1.delete(0,"end"))
clear.grid(row=6,column=2,sticky="nw",pady=5)
add=tkinter.Button(master=screen,text="+",width=15,height=4,fg="green",bg="black",cursor="hand1",command=lambda :en1.insert("end","+"))
add.grid(row=7,column=0,sticky="nw",pady=5)
subtract=tkinter.Button(master=screen,text="-",width=15,height=4,fg="green",bg="black",cursor="hand1",command=lambda :en1.insert("end","-"))
subtract.grid(row=7,column=1,sticky="nw",pady=5)
multiply=tkinter.Button(master=screen,text="X",width=15,height=4,fg="green",bg="black",cursor="hand1",command=lambda: en1.insert("end","*"))
multiply.grid(row=7,column=2,sticky="nw",pady=5)
Divide=tkinter.Button(master=screen,text="÷",width=15,height=4,fg="green",bg="black",cursor="hand1",command=lambda: en1.insert("end","/"))
Divide.grid(row=8,column=0,sticky="nw",pady=5)   # symbol not available ÷
#EQUAL  
equals=tkinter.Button(master=screen,text="Equals",width=25,height=3,bg="black",fg="blue",cursor="hand1",font=("arial",0,"bold italic"),command=lambda :en1.insert("end","="+str(eval(en1.get()))))
equals.grid(row=8,column=1,columnspan=2)


#____________________________________________________________________________________________________________
screen.mainloop()


# done 