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

#Height Section
height = tk.Label(text = "Height" , font = "Arial")
height.place(x = 165, y = 200)

enter_height = tk.Entry(width = 20)
enter_height.place(x = 135, y = 250)

window.mainloop()