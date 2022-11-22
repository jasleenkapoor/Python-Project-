# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 15:46:08 2022

@author: zhap048
"""


import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk



demov = ([0,0,0,0,0,0,0,0,0])


#if they select to use demo data, the two types of data we'll offer will be simple harmonic or finite square well
#if simple harmonic then the variable 'choice' = 1, if finite square well then 'choice' = 2, and if they have input their own values for v, 'choice' will = 0 
#if they select to use their own data then they will be asked what the name of their data file is

#if they do not input their own values, the vareable 'v' will be set to 0. if the user inputs their own values for the potential, they will be saved as an array, equal to the vareable 'v' . 

#they will then be asked to input a value for the springconstant k

#they will than be asked if they want to save the plot after it has been printed
#if they select not to save then shouldsave = 0 and it will not save, if they do want to save, shouldsave = 1 it will save

#they will be asked if they want to save, to save as a mp4 or a gif
#filetype will be set to 1 for mp4, or 2 for saving as a gif, will remain 0 for not saving as anything

class firstq():
    
    def __init__(self,choice, shouldsave, springconst, filetype, saveas, v):
        self.choice = choice            #number
        self.shouldsave = shouldsave    #number
        self.springconst = springconst  #number
        self.filetype = filetype        #number
        self.v = v                      #array
        self.saveas = saveas            #word
        
        

        
    def main(self):   # "main" is the code to open window 1
        self.w1=Tk()    # this defines the content of window 1
        self.w1.title("1. Opening page")
        self.w1.geometry("800x400")
        b12 = Button(self.w1, text="info",  bg="lightblue", fg="blue", command = self.infos)
        b12.pack(side=TOP, anchor=NW)
        t1 = Label(self.w1, text= "Would you like to use our calculated values of V, or input \n your values of V for us to plot?")
        t1.pack()
        sourceofdata = tk.Button()
        self.w1=Frame(self.w1,)
        self.w1.pack()
        b1 = Button(self.w1, text="i want to input my own data", command =  self.useowndata)
        b1.pack()
        b2 = Button(self.w1, text="i want to use example data", command = self.usedemodata)
        b2.pack()
        t11 = Label(self.w1, text = "\n \n Once you have made your choices, close this first window to finish the program.")
        t11.pack()
        self.w1.mainloop()
        
    def useowndata(self):  #  "useowndata" is the code to open window 2
        self.w2 = Tk()      # this defines the content of window 2
        self.w2.title("2.use own data")
        self.w2.geometry("900x350")
        b13 = Button(self.w2, bg= "pink", text = "Back", command=self.w2.destroy)
        b13.pack(side=TOP, anchor=NW)
        t2 = Label(self.w2, text="Your Data needs to consist of 500 values saved in a txt file. \n \n What is your file called? \n Please give your answer in the form of 'title.txt' and make sure your values \n for the Potential are written out on the first line of the document and each is separated by a space", )
        t2.pack()
        self.e1 = Entry(self.w2, width=40)
        self.e1.focus_set()
        self.e1.pack()     
        b3 = Button(self.w2, text="search", command= lambda:[ self.search()])
        b3.pack()
        

        
    def usedemodata(self): #  "usedemodata" is the code to open window 3
        self.w3 = Tk()      # this defines the content of window 3
        self.w3.title("3. using demo data")
        self.v = demov
        self.w3.geometry("500x350")
        b13 = Button(self.w3, bg= "pink", text = "Back", command=self.w3.destroy)
        b13.pack(side=TOP, anchor=NW)
        t3 = Label(self.w3, text="You have selected the demo data", )
        t3.pack()
        b4 = Button(self.w3, text="i want to plot a finite square well", command= lambda:[self.w3.destroy(), self.fsw()])
        b4.pack()
        b5 = Button(self.w3, text="i want to plot a simple harmonic function", command = lambda:[self.w3.destroy(), self.sh()])
        b5.pack()
     
        
    def search(self): # "search" is the code to open window 4
         self.w4 = Tk()          # this defines the content of window 4
         self.w4.title("4. search")
         self.w4.geometry("500x350")
         string = self.e1.get()
         self.string = string
         mydata = []
         with open(string, "rt") as myfile:
             for myline in myfile:
                 mydata.append(myline)
         self.v = (mydata[0]).split()    
         b13 = Button(self.w4, bg= "pink", text = "Back", command= lambda:[self.w4.destroy(), self.useowndata()])
         b13.pack(side=TOP, anchor=NW)
         self.w2.destroy()
         t4 = Label(self.w4, text=string, )
         t4.pack()        
         t45 = Label(self.w4, text= self.v, )
         t45.pack()
         self.path = 1
         b6 = Button(self.w4, text="Continue", command= lambda:[self.w4.destroy(), self.continue_name()])        
         b6.pack() 
         
         
    def fsw(self): # "fsw" is the code to open window 5
        self.w5 = Tk()      # this defines the content of window 5
        self.w5.title("5. finite square well")
        self.w5.geometry("500x350")
        b13 = Button(self.w5, bg= "pink", text = "Back", command= lambda:[self.w5.destroy(), self.usedemodata()()])
        b13.pack(side=TOP, anchor=NW)
        t5 = Label(self.w5, text="You have asked to plot a finite square well", )
        self.choice=2
        t5.pack()
        self.path = 2
        b7 = Button(self.w5, text="Continue", command= lambda:[self.w5.destroy(), self.continue_name()])           
        b7.pack() 
    
    def sh(self):       # "sh" is the code to open window 6
        self.w6 = Tk()    # this defines the content of window 6
        self.w6.title("6. simple harmonic")
        self.w6.geometry("500x350")
        b13 = Button(self.w6, bg= "pink", text = "Back", command= lambda:[self.w6.destroy(), self.usedemodata()])
        b13.pack(side=TOP, anchor=NW)
        t6 = Label(self.w6, text="You have asked to plot a simple harmonic function", )
        self.choice=1
        t6.pack()    
        #
        t8 = Label(self.w6, text="Please input the spring constant, k, you would like to use. \n If you dont have a value then set this to 1", )
        t8.pack()
        self.entry3 = Entry(self.w6, width=40)
        self.entry3.focus_set()
        self.entry3.pack()
        #
        self.path = 3
        b8 = Button(self.w6, text="Continue", command= lambda:[self.savek(),  ])           
        b8.pack() 


    def continue_name(self): # "continue_name" is the code to open window 7
        self.w7 = Tk()          # this defines the content of window 7
        self.w7.title("7. final inputs")
        self.w7.geometry("700x450")
        b13 = Button(self.w7, bg= "pink", text = "Back", command= lambda:[self.w7.destroy(), self.backfrom7()])
        b13.pack(side=TOP, anchor=NW)
        t7 = Label(self.w7, text="Please input the name you want to save the plot as", )
        t7.pack()
        self.entry2 = Entry(self.w7, width=40)
        self.entry2.focus_set()
        self.entry2.pack()  
        t9 = Label(self.w7, text="Would you like to save the file? And if so, \n do you want to save it as a mp4 file or gif? \n \n Make sure you have at least one saved version of \n the file in order for the animation to play.", )
        t9.pack()
        b9 = Button(self.w7, text="Dont save", command = lambda:[ self.dontsave(), ])    
        b9.pack()
        b10 = Button(self.w7, text="Save as mp4", command = lambda:[ self.mp4(),  ])
        b10.pack()
        b11 = Button(self.w7, text="Save as gif", command= lambda:[ self.gif(), ])
        b11.pack()
        
    
    def infos(self): # "infos" is the code to open the info page, aka window 8
        self.w8 = Tk()      # this defines the content of window 8
        self.w8.title("Info")
        self.w8.geometry("460x730")
        b13 = Button(self.w8, bg= "pink", text = "Back", command=self.w8.destroy)
        b13.pack(side=TOP, anchor=NW)
        t10 = Label(self.w8, text="This is a program that can help you solve \n the Time-Dependent Schrödinger Equation for \n an arbitrary potential you have specified. \n \n  You also have the option to use demo \n values of the potential instead of entering your own. \n These can produce either a simple harmonic equation \n or a finite square well equation. \n \n  If you are entering your own values, \n you must save 500 values in a txt file, \n with all your values on the top row, each \n separated by a space. \n \n  There should be no characters other\n than numbers (except decimal points), \n no commas or letters etc. \n \n \n Created by: \n Emlyn Davies, \n Jamie-Gowers, \n jasleen Kapoor, \n Alex-Prowse, \n Jessica-Tucker, \n and Matthew Webb")
        t10.pack()


        
    def dontsave(self):          #for the final part of the code if they are not saving
        self.shouldsave = 0
        print("dont save")        
        self.saveas = self.entry2.get()
        self.w7.destroy()
        self.export
        
        
        
    def mp4(self):               #for the final part of the code if they are saving as mp4
        self.shouldsave = 1
        self.filetype = 1
        print("mp4")
        self.saveas = self.entry2.get()
        self.export
        self.w7.destroy()
        
    def gif(self):               #for the final part of the code if they are saving as gif
        self.shouldsave = 1
        self.filetype = 2
        print("gif")     
        self.saveas = self.entry2.get()
        self.export
        self.w7.destroy()

        
    def backfrom7(self):
        if self.path==1:
            self.search()
        if self.path==2:
            self.fsw()
        if self.path==3:
            self.sh()
    

    def export(self):
        return self.choice, self.shouldsave, self.springconst, self.filetype, self.saveas, self.v
    
    def savek(self):      #records the value of k if that is a value that needs to be input
        self.springconst = int(self.entry3.get())
        self.continue_name()
        self.w6.destroy()
        
    
        
