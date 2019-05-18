#!usr/bin/env python3.5
# -*- coding: utf-8 -*-

import tkinter


units_order=['发射一营','发射二营','发射三营','发射四营','发射五营','发射六营','技术一营','技术二营','作战保障营','阵管防卫连','营区大门岗','家属院门岗','油库','机关楼','装备场区','共同训练场']

def get_wire_status():
    with open('terse_absence.txt','r')as f:
        status=f.read()
    return status

def show_status(status):
    color={'1':'red','0':'white'}
    for i in range(len(units_order)):
        if i<len(units_order)/2:
                tkinter.Label(root,bg=color[status[i]],width=2,height=1).place(x=44+i*53,y=135)
                
        if i>=len(units_order)/2:
                tkinter.Label(root,bg=color[status[i]],width=2,height=1).place(x=44+(i-len(units_order)/2)*53,y=215)

def show_change():
    
    status=get_wire_status()
    with open('terse_absence_add.txt','r')as f:
       status_add=f.read()
    if status_add!=status:
        show_status(status)
    with open('terse_absence_add.txt','w')as f:
       f.write(status)

    root.after(3000,show_change)     

status=get_wire_status()
with open('terse_absence_add.txt','w')as f:
    f.write(status)
   



root=tkinter.Tk()
root.geometry('480x320')
root.title("警戒系统")
root.resizable(0,0)
root.attributes('-topmost',1)
#root.attributes('-fullscreen',1)


photo=tkinter.PhotoImage(file="背景.png")
img=tkinter.Label(root,image=photo)
img.place(x=0,y=0)
show_status(status)

show_change()
root.update_idletasks()
root.mainloop()



















