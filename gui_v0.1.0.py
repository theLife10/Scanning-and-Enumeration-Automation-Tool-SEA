# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 19:22:45 2021

@author: jacob
"""

import tkinter as tk
import threading
from tkinter import ttk

class Progress():
    
    def __init__(self):
        global label
        self.root = tk.Tk()
        self.root.title('Exporting')
        self.root.geometry('250x150')
        self.label = tk.Label(self.root, text='Progress').pack(fill=tk.Y, anchor=tk.CENTER, ipady=30)
        self.progress = ttk.Progressbar(self.root, orient=tk.HORIZONTAL,
                                        length=150, mode='determinate')
        self.progress.pack(side=tk.TOP)
        self.thread = threading.Thread(target=self.bar).start()
        self.cancel = tk.Button(self.root, text='Cancel', command=self.root.destroy)
        self.cancel.pack(side=tk.LEFT,expand=tk.YES)
        
        self.finish = tk.Button(self.root, text='Finish', state=tk.DISABLED, command=self.root.destroy)
        self.finish.pack(side=tk.LEFT,expand=tk.YES)
        
        self.root.mainloop()
        
    def completed(self):
        return self.progress['value'] == 100
    
    def bar(self): 
        import time

        for i in range(0,101,20):
            self.progress['value'] = i
            self.root.update_idletasks() 
            time.sleep(.2) 
        
        if self.completed:
            self.finish['state'] = 'normal'
        

class Export():
    root = None
    frame = None
    canvas = None
    scrollable = None
    
    def __init__(self, master=None):
        self.root = tk.Tk()
        self.frame = ttk.Frame(self.root)
        #self.frame.pack()
        self.canvas = tk.Canvas(self.frame)
        self.scrollbar = ttk.Scrollbar(self.frame, orient='vertical', command=self.canvas.yview)
        self.scrollable = ttk.Frame(self.canvas)
        self.scrollable.bind('<Configure>', lambda e: self.canvas.configure(
            scrollregion=self.canvas.bbox('all')))
        self.canvas.create_window((0,0), window=self.scrollable, anchor='nw')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        for i in range(50):
            ttk.Label(self.scrollable, text="Sample").pack()
        self.frame.pack()
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        self.button = tk.Button(self.root, text='Export', command=self.prog)
        self.button.pack(anchor=tk.SE,padx=10,pady=10)
        
        self.root.mainloop()
        
    def prog(self):
        progbar = Progress()
 
export_window = Export()