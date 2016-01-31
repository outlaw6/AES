
import Tkinter, sys, os, base64, hashlib
from Crypto import Random
from Crypto.Cipher import AES
from ScrolledText import *


BLOCK_SIZE = 32

PADDING = '{'

pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)


def getText():
    global tekst, textPad
    secret = '123456'
    cipher = AES.new(pad(secret))

    txt = textPad.get('1.0',Tkinter.END)
    encoded = EncodeAES(cipher, txt)
    
    textPad2.insert(Tkinter.INSERT, encoded)	
    pass


root = Tkinter.Tk()
root.geometry("1000x330+300+300")


textPad = ScrolledText(root, width=50, height=20, bg='grey')
textPad.grid(padx=15, pady=5, row=0, column=0)

textPad2 = ScrolledText(root, width=50, height=20, bg='grey')
textPad2.grid(padx=100, pady=5, row=0, column=4)

dugme = Tkinter.Button(root, text='Get Text', width=5, command=getText)
dugme.grid(padx=5, pady=5, row=0, column=2)


tekst = Tkinter.StringVar()
label1 = Tkinter.Label(root, textvariable=tekst)
label1.grid(row=0, column=3)
root.mainloop() 
