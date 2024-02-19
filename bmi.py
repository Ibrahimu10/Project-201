from tkinter import *
window=Tk()

# add widgets here


window.title('BMI Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')

def calculate_interest():
    p = int(principal_entry.get())
    r = int(rate_entry.get())
    t = int(time_entry.get())
    i = (p*r*t)/100
    interest = round (i, 2)
    result_label.destroy()
    output_message = Label(result_frame,"Your interest rate is "+str(interest), bg = "lightcyan", font=("Calibri", 12), width=42)
    output_message.place(x=20,y=40)
    output_message.pack()


app_label=Label(window, text="Caculate Interest", fg = "black", bg = "lightcyan", font=("Calibri", 30),bd=5)
app_label.place(x=50, y=20)

principal_label=Label(window, text="Principal", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
principal_label.place(x=20, y=90)

principal_entry=Entry(window, text="", bd=2, width=22)
principal_entry.place(x=150, y=92)

rate_label=Label(window, text="Rate", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
rate_label.place(x=20, y=140)

rate_entry=Entry(window, text="", bd=2, width=15)
rate_entry.place(x=150, y=142)

time_label=Label(window, text="Time", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
time_label.place(x=20, y=185)

time_entry=Entry(window, text="", bd=2, width=15)
time_entry.place(x=150, y=187)

calculate_button = Button(window,text="Calculate", fg = "black", bg = "cyan", bd = 4, command=calculate_interest)
calculate_button.place(x=20,y=250)

result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()