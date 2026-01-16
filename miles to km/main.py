from tkinter import *

def m_km():
    m=float(miles_input.get())
    km=(m * 1.609)
    km_label_result.config(text=f"{km}")
window=Tk()
window.title("mile to km converter")
window.config(padx=20,pady=20)
miles_input=Entry(width=7)
miles_input.grid(column=1,row=0)

mile_label=Label(text="Miles")
mile_label.grid(column=2,row=0)

is_equal_label=Label(text=" is equal  to")
is_equal_label.grid(column=0,row=1)

km_label_result=Label(text="0")
km_label_result.grid(column=1,row=1)

km_label=Label(text="Km")
km_label.grid(column=2,row=1)

calculate=Button(text="Calculate",command=m_km)
calculate.grid(column=1,row=2)




window.mainloop()