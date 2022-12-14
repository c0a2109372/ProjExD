import tkinter as tk
import math

flag = True
def button_click(event):
    global flag
    btn = event.widget
    txt = btn["text"]
    if flag == False: #空白状態で計算されないようにする
        flag = True
        entry.delete(0,tk.END)
    if txt == "=":
        siki = entry.get()
        try:#=連打によるエラー回避
            res = eval(siki)
            entry.delete(0,tk.END)
            entry.insert(tk.END, res)
            flag = False
        except(SyntaxError):
            pass
    elif txt == "x²": #２乗の計算
        entry.insert(tk.END, "**")
    elif txt == "√": #２乗根の計算
        siki = entry.get()
        entry.delete(0,tk.END)
        res = eval(siki)
        rs = math.sqrt(res) #mathモジュールで計算を行う
        entry.insert(tk.END, rs)
        flag = False
    elif txt == "AC":#全部消す
        entry.delete(0,tk.END)
    elif txt == "x": #乗算
        entry.insert(tk.END,"*")
    else:
        entry.insert(tk.END, txt)

root = tk.Tk()
root.geometry("400x900")

entry = tk.Entry(root, justify="right", width=10, font=("",40))
entry.grid(row = 0, column=0,columnspan=3)

r, c = 1, 0
flag = True

command_list = ["AC", "/","x²"]
for cm in command_list:
    button = tk.Button(root, text=cm, width=4, height=2, font=("",30))
    button.grid(row=r, column=c)
    button.bind("<1>",button_click)
    c+=1
    if c%3 == 0:
        r += 1
        c = 0
        
command_list = ["-", "x", "%", "√"]
c = 4
r -= 1
for cm in command_list:
    button = tk.Button(root, text=cm, width=4, height=2, font=("",30))
    button.grid(row=r, column=c)
    button.bind("<1>",button_click)
    r+=1
r = 2
c = 0
num = 7
for i in range(10):
    button = tk.Button(root, text=f"{num+i}", width=4, height=2, font=("",30))
    button.grid(row = r, column=c)
    button.bind("<1>",button_click)
    c+=1
    if i%3==2 and i != 0:
        num -= 6
        r+=1
        c=0
    if i == 8:
        num = -9
        
ope = ["+", "="]
for op in ope:
    button = tk.Button(root, text=f"{op}", width=4, height=2, font=("", 30))
    button.grid(row=r, column=c)
    button.bind("<1>",button_click)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0



root.mainloop()