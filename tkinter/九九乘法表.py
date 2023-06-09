'''
print(5/3)#基本除法
print(5//3)#求商數
print(5%3)#求餘數
'''
'''
d = {1:"a",2:"b",3:"c"}
print(d[1])
print(d[2])
print(d[3])
'''
import tkinter

window = tkinter.Tk()
window.geometry('300x300')#設定視窗大小
window.title("九九乘法表")
'''
tkinter.Label(window,text='Top').pack(side='top')
tkinter.Label(window,text='Bottom').pack(side='bottom')
tkinter.Label(window,text='Left').pack(side='left')
tkinter.Label(window,text='Right').pack(side='right')
'''
#grid
for i in range(1,10):
    for j in range(1,10):
        label = tkinter.Label(window,text=i*j)
        label.grid(row=i,column=j,padx=6,pady=6)
window.mainloop()