# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 15:46:08 2022

@author: zhap048
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 12:01:58 2022

@author: zhap048
"""

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


#set some demo values for the potental and call it demov
demov = ([1,2,3,4,5,6,7,8,9])


#if they select to use demo data, the two types of data we'll offer will be simple harmonic or fitite square well
#if simple harmonic then choice = 1, if finite then choice = 2
#if they select to use their own data then they will be asked what the name of their data file is
#whatever they pick, they will then be asked to input a value for the springconstant k
#they will than be asked, whatever they're previous choices, do they wantto save the plot after it has been printed
#if they put shouldsave = 0 it will not save, if = 1 it will save
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
        
        
    def sh(self): #window 6
        self.w6 = Tk()
        self.w6.title("6. simple harmonic")
        self.w6.geometry("500x350")
#        self.w6.attributes('-fullscreen', True)
        t6 = Label(self.w6, text="you have asked to plot a simple harmonic function", )
        self.choice=1
        t6.pack()    
        self.path = 3
        b8 = Button(self.w6, text="Continue", command= lambda:[self.w6.destroy(),self.continue_name()])           
        b8.pack() 
        
    def main(self):   #window1
        self.w1=Tk()
        self.w1.title("1. Opening page")
        self.w1.geometry("800x400")
#        self.w1.attributes('-fullscreen', True)
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
        self.w1.mainloop()
        
    def dontsave(self):          #not saving
        self.shouldsave = 0
        self.springconst = int(self.entry3.get())
        self.saveas = self.entry2.get()
        self.export
        
        
    def mp4(self):               #saving as mp4
        self.shouldsave = 1
        self.filetype = 1
        self.springconst = int( self.entry3.get())
        self.saveas = self.entry2.get()
        command = self.export
        
    def gif(self):               #saving as gif
        self.shouldsave = 1
        self.filetype = 2
        self.springconst = int(self.entry3.get())
        self.saveas = self.entry2.get()
        command = self.export
        
        
    def continue_name(self): #window 7
        self.w7 = Tk()
        self.w7.title("7. final inputs")
        self.w7.geometry("800x400")
#        self.w7.attributes('-fullscreen', True)
        t7 = Label(self.w7, text="Please input the name you want to save the plot as", )
        t7.pack()
        self.entry2 = Entry(self.w7, width=40)
        self.entry2.focus_set()
        self.entry2.pack()            
        #
        t8 = Label(self.w7, text="Please input the spring constant, k, you would like to use. \n If you dont have a value then set this to 1", )
        t8.pack()
        self.entry3 = Entry(self.w7, width=40)
        self.entry3.focus_set()
        self.entry3.pack()
        #
        t9 = Label(self.w7, text="Would you like to save the file? And if so, \n do you want to save it as a mp4 file or gif?", )
        t9.pack()
        b9 = Button(self.w7, text="Dont save", command = lambda:[self.dontsave(), self.w7.destroy()])    
        b9.pack()
        b10 = Button(self.w7, text="Save as mp4", command = lambda:[self.mp4(), self.w7.destroy(), ])
        b10.pack()
        b11 = Button(self.w7, text="Save as gif", command= lambda:[self.w7.destroy(), self.gif(), ])
        b11.pack()
        t11 = Label(self.w7, text = "Once you have made your choice, close the first window to finish the program.")
        t11.pack()
    
        
#    def destroyall(self):
#        if self.path == 1:
#            self.w1.destroy(), self.w2.destroy(), self.w4.destroy(), self.w7.destroy(),  
#        if self.path == 2:
#            self.w1.destroy(),  self.w3.destroy(), self.w5.destroy(),self.w7.destroy(),  
#        if self.path== 3:
#            self.w1.destroy(), self.w3.destroy(), self.w6.destroy(), self.w7.destroy(),  
       
        
    def useowndata(self):  # window 2
        self.w2 = Tk()
        self.w2.title("2.use own data")
        self.w2.geometry("600x350")
#        self.w2.attributes('-fullscreen', True)
        t2 = Label(self.w2, text="Your Data needs to be saved in a txt file. \n What is your file called? \n Please give your answer in the form of 'title.txt' (such as testingdata.txt) and make sure your values \n for the Potental are writen out on the first line of the document and seperated by a comma", )
        t2.pack()
        self.entry = Entry(self.w2, width=40)
        self.entry.focus_set()
        self.entry.pack()     
        b3 = Button(self.w2, text="search", command= lambda:[self.w2.destroy(), self.search()])
        b3.pack()
    
    def infos(self): # window 8 info
        self.w8 = Tk()
        self.w8.title("Info")
        self.w8.geometry("400x450")
        t10 = Label(self.w8, text="This program is used to help you...")
        t10.pack()
        
        
    def search(self): #window 4
        self.w4 = Tk()
        self.w4.title("4. search")
        self.w4.geometry("500x350")
#        self.w4.attributes('-fullscreen', True)
        string = self.entry.get()
        self.string = string
        mydata = []
        with open(string, "rt") as myfile:
            for myline in myfile:
                mydata.append(myline)
        self.v = (mydata[0]).split()       
        t4 = Label(self.w4, text=string, )
        t4.pack()        
        t45 = Label(self.w4, text= self.v, )
        t45.pack()
        self.path = 1
        b6 = Button(self.w4, text="Continue", command= lambda:[self.w4.destroy(), self.continue_name()])        
        b6.pack() 
        
        
    def usedemodata(self): # window 3
        self.w3 = Tk()
        self.w3.title("3. using demo data")
        self.v = demov
        self.w3.geometry("500x350")
#        self.w3.attributes('-fullscreen', True)
        t3 = Label(self.w3, text="You have selected the demo data", )
        t3.pack()
        b4 = Button(self.w3, text="i want to plot a finite square well", command= lambda:[self.w3.destroy(), self.fsw()])
        b4.pack()
        b5 = Button(self.w3, text="i want to plot a simple harmonic function", command = lambda:[self.w3.destroy(), self.sh()])
        b5.pack()
        
    def fsw(self): #window 5
        self.w5 = Tk()
        self.w5.title("5. finite square well")
        self.w5.geometry("500x350")
#        self.w5.attributes('-fullscreen', True)
        t5 = Label(self.w5, text="you have asked to plot a finite square well", )
        self.choice=2
        t5.pack()
        self.path = 2
        b7 = Button(self.w5, text="Continue", command= lambda:[self.w5.destroy(), self.continue_name()])           
        b7.pack() 
    
    def export(self):
        return self.choice, self.shouldsave, self.springconst, self.filetype, self.saveas, self.v
        
    
        
        
runclass=firstq(0, 0, 0, 0, 0, 0)
runclass.main()
print("the values of: choice, shouldsave, springconst, filetype, saveas, v")
print("the updated values are ", runclass.export())

