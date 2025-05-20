import tkinter as tk

window = tk.Tk()
window.title("BMI")
window.minsize(400, 400)
window.maxsize(400, 400)

#Weight Section

weight = tk.Label(text = "Weight" , font = "Arial")
weight.place(x = 165, y = 100)

enter_weight = tk.Entry(width = 20)
enter_weight.place(x = 135, y = 150)
#-------------------------------------------------------


window.mainloop()