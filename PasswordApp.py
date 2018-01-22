import tkinter as tk
import enchant
import re
from Crypto.Cipher import AES

class PasswordApp(tk.Tk):

	def __init__(self):

		tk.Tk.__init__(self)

		self.var = tk.StringVar()

		banimg = tk.PhotoImage(file="passbanner.gif")
		self.banner = tk.Label(self, image=banimg)
		self.banner.image = banimg

		self.entry = tk.Entry(self, width=200, show='*', justify='center')
		self.button = tk.Button(self, text="Check", command=self.CheckPassword)
		self.label1 = tk.Label(self, text="none", bg="#ecf0f1")
		self.label2 = tk.Label(self, text="none", bg="#ecf0f1")
		self.label3 = tk.Label(self, text="none", bg="#ecf0f1")
		self.label4 = tk.Label(self, text="none", bg="#ecf0f1")
		self.banner.pack(padx=0, pady=2)
		self.entry.pack()
		self.button.pack()
		self.label1.pack()
		self.label2.pack()
		self.label3.pack()
		self.label4.pack()

	def CheckSymbols(self, pw):
		s = 0
		listsymb = ['!', '"', '£', '$', '%', '^', '&', '*', '(', ')', '-', '-', '{', '}', '[', ']', ',', '+']
		length = len(listsymb)



		for char in listsymb:
			if (char in pw):
				s = s + 1
				print(s)

		if(s > 0):
			self.label4.config(text = "\n Password contains symbols! \n")
		else:
			self.label4.config(text = "\n Password contains no Symbols! \n Please add a special character to your password some examples are \n !£@*%+")







	def CheckLength(self, pw):

		y = len(pw)
		print("Y is equal to " + str(y))
		if(y < 8):
			self.label2.config(text = "\n Password too short! Less than 8 characters! \n Please ensure that your supplied password \n is at least 8 characters or more in length.")
		elif( y >= 8 ):
			self.label2.config(text = "\n Password length ok! Password more than 8 characters! \n")
		self.CheckForNumbers(pw)

	def CheckForNumbers(self, pw):

		num = 0
		for char in pw:
			if(char.isdigit()):
				num = num + 1

		if(num > 0):
			self.label3.config(text = "\n Password contains " + str(num) + " numbers! \n")
		elif(num == 0):
			self.label3.config(text = "\n Password does not contain any numbers! \n")

		self.CheckSymbols(pw)



	def CheckPassword(self):

		print(self.entry.get())
		pw = self.entry.get()
		print(pw)
		ChkPW = pw

		ChkPW = re.sub(r'[^\w]','',ChkPW)
		print("ChkPW = " + ChkPW)

		ChkPW = re.sub(r'\d+', '', ChkPW)

		print(ChkPW)

		

		l = len(ChkPW)
		x = 0
		w = 0
		d = enchant.Dict()

		






		while(x < l):
			b = d.check(ChkPW[x:l])
			if(b):
				print(b)
				w = w + 1
				print(w)

			x = x + 1

		if(w > 0):

			self.label1.config(text= str(w) + " dictionary words found in password! \n Avoid using dictionary words within \n your password, try replacing letters with symbols.")
		self.CheckLength(pw)










#End of Class

def WinCreate(w):
	w.geometry('502x400')



w = PasswordApp()
WinCreate(w)
w.configure(background = '#ecf0f1')
w.title("Password App")
w.mainloop()
