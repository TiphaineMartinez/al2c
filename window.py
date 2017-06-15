#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from Tkinter import * 

fenetre = Tk()
fenetre.geometry("800x600+300+100")
fenetre['bg']='white'

texte = "Tp"

label = Label(fenetre, text=texte)
label.pack()

fenetre.mainloop()
