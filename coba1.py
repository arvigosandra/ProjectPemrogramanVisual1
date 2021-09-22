import tkinter as tk

	def createName():
		name = inputName.get()
		ortu = inputOrtu.get()
		tk.Label(master, text="Nama: " + name).grid(row=4, column=1, sticky=tk.W)

master = tk.Tk()
master.title("Belum Terpikirkan Data KTP")
master.geometry("500x300")

inputName = tk.Entry(master)
inputOrtu = tk.Entry(master)

tk.Label(master, text="Nama: ").grid(row=0, column=0)
inputName.grid(row=0, column=1)
tk.Label(master, text="Nama Ortu: ").grid(row=0, column=1)
inputOrtu.grid(row=1, column=1)
tk.Button(master, text='Tampilkan', command=createName).grid(row=0, column=2)

tk.mainloop()
