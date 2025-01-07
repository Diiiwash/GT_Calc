

import tkinter as tk
from tkinter import ttk
from tkinter import Frame
import sys 
import os

global na
global nb 
global na1
global nb1 
root= tk.Tk()
root.title('Oddoment Method')

def oddoment():
    
    a = int(bentry1.get())
    b = int(bentry2.get())
    c = int(bentry3.get())

    a1 = int(centry1.get())
    b1 = int(centry2.get())
    c1 = int(centry3.get())

    a2 = int(dentry1.get())
    b2 = int(dentry2.get())
    c2 = int(dentry3.get())

    

    c1 = max(a,a1,a2)
    c2 = max(b,b1,b2)
    c3 = max(c,c1,c2)

    r1 = min(a,b,c)
    r2 = min(a1,b1,c1)
    r3 = min(a2,b2,c2)

    Cmin = min(c1,c2,c3)
    Rmax = max(r1,r2,r3)
    
    

    if(Cmin == Rmax):
        print("Saddle point exist")
        print("End of process")
        
    else:
        if(a>=b and a1 >= b1 and a2> b2):
            a = b
            a1= b1
            a2 = b2
        
        if(b >= c and b1>= c1 and b2>=c2):
          
            b = c
            b1 = c1
            b2 = c2
        O1 = "first process"
        O2 = "|{} {}|".format(a,b)
        O3 ="|{} {}|".format(a1,b1)
        O4= "|{} {}|".format(a2,c2)
        print(a,b)
        print(a1,b1)
        print(a2,b2)

        if(a<=a1 and b<=b1):
            a = a1
            b = b1
        
        if(a1<=a2 and b1 <= c2):
            a1 = a2
            b1 = b2
        print(a,b)
        print(a1,b1)
           
        #for determinant



        #append Y1,Y2,Y3,Y4
        O7 = "Second & Final Step"
        O5 = "|{} {}|".format(a,b)
        O6 = "|{} {}|".format(a1,b1)

        

        Olabel1 = tk.Label(root, text=O1,fg='black',bg='white')
        Olabel1.config(font=('helvetica', 17))
        canvas1.create_window(225+190, 305+225, window=Olabel1)

        Olabel2 = tk.Label(root, text=O2,fg='black',bg='white')
        Olabel2.config(font=('helvetica', 17))
        canvas1.create_window(225+190, 305+250, window=Olabel2)
        
        Olabel3 = tk.Label(root, text=O3,fg='black',bg='white')
        Olabel3.config(font=('helvetica', 17))
        canvas1.create_window(225+190, 305+275, window=Olabel3)

        Olabel4 = tk.Label(root, text=O4,fg='black',bg='white')
        Olabel4.config(font=('helvetica', 17))
        canvas1.create_window(225+190, 305+300, window=Olabel4)

        Olabel5 = tk.Label(root, text=O5,fg='black',bg='white')
        Olabel5.config(font=('helvetica', 17))
        canvas1.create_window(225+190, 305+375, window=Olabel5)

        Olabel6 = tk.Label(root, text=O6,fg='black',bg='white')
        Olabel6.config(font=('helvetica', 17))
        canvas1.create_window(225+190, 305+400, window=Olabel6)
        
        
        Olabel7 = tk.Label(root, text=O7,fg='black',bg='white')
        Olabel7.config(font=('helvetica', 17))
        canvas1.create_window(225+190, 305+350, window=Olabel7)
            

canvas1 = tk.Canvas(root, width = 800, height = 1000,  relief = 'raised')
canvas1.pack()
#Heading
label1 = tk.Label(root, text='Game Theory-Dominance Method Rule',fg='white',bg='#218B82')
label1.config(font=('helvetica', 20))
canvas1.create_window(400, 30, window=label1)
#Credit
label2 = tk.Label(root, text='Submitted By: Diwash Bhattarai',fg='black',bg='green')
label2.config(font=('helvetica', 14))
canvas1.create_window(200, 70, window=label2)

label3 = tk.Label(root, text='Submitted To: Durga Prasad Dhakal',fg='black',bg='green')
label3.config(font=('helvetica', 14))
canvas1.create_window(550, 70, window=label3)

label4 = tk.Label(root, text='Input the 3x3 matrix data in the following entry boxes.',fg='black',bg='white')
label4.config(font=('helvetica', 16))
canvas1.create_window(350, 70+80, window=label4)





#creating entry lable and entry for 1st equation
#1
bentry1 = tk.Entry (root) 
canvas1.create_window(180+50, 160+50, window=bentry1,height=40,width=40)

#2
bentry2 = tk.Entry (root) 
canvas1.create_window(180+50+90, 160+50, window=bentry2,height=40,width=40)

#3
bentry3 = tk.Entry (root) 
canvas1.create_window(180+50+90+90, 160+50, window=bentry3,height=40,width=40)





#creating entry lable and entry for 2nd equation
#1
centry1 = tk.Entry (root) 
canvas1.create_window(180+50, 160+50+50, window=centry1,height=40,width=40)

#2
centry2 = tk.Entry (root) 
canvas1.create_window(180+50+90, 160+50+50, window=centry2,height=40,width=40)

#3
centry3 = tk.Entry (root) 
canvas1.create_window(180+50+90+90, 160+50+50, window=centry3,height=40,width=40)


#creating entry lable and entry for 3rd equation
#1
dentry1 = tk.Entry (root) 
canvas1.create_window(180+50, 160+150, window=dentry1,height=40,width=40)

#2
dentry2 = tk.Entry (root) 
canvas1.create_window(180+50+90, 160+150, window=dentry2,height=40,width=40)

#3
dentry3 = tk.Entry (root) 
canvas1.create_window(180+50+90+90, 160+150, window=dentry3,height=40,width=40)




canvas1.create_rectangle(0, 450, 800, 800,fill='white')
def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)



#Reset button
button1 = tk.Button(text='Optimize',  bg='blue', fg='white', font=('helvetica', 15, 'bold'),relief = 'solid',command=simplex)
canvas1.create_window(250, 365+50, window=button1,height=50,width=100)

#Optimize button
button2 = tk.Button(text='Reset',  bg='red', fg='white', font=('helvetica', 15, 'bold'),relief = 'solid',command=restart_program)
canvas1.create_window(480, 365+50, window=button2,height=50,width=100)



root.mainloop()
