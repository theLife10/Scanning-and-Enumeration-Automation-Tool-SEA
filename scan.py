from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, QThread
import os

global playButton, pauseButton, stopButton

class worker(QThread):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    filepath = ''
    params = ''
    def run(self):
       os.system(self.filepath+' '+self.params)
    

class scan(QObject):
    def __init__(self):
        self.name = ''
        self.row = -1
        #states 0 = paused 1 = running -1 = finished
        self.state = -2
        self.file = ''
        self.params = ''
        self.thread = worker()
    
    
    #jacob's startRunList()
    def start(self):
        self.state = 1
        import traceback
        try:
            #self.thread = QtCore.QThread()
            #self.worker = worker()

            #self.moveToThread(self.thread)
            #self.thread.started.connect(self.run_file)
            #self.finished.connect(self.stop())
            self.thread.filepath = self.file
            self.thread.params = self.params
            self.thread.start()
            print('scan: ...Starting')

        except:
            traceback.print_exc()
            print('DNE')

    def pause(self):
        self.state = 0
        while(self.state == 0 ):
            self.thread.wait(1)
    
    def resume(self):
        self.state = 1
        self.thread.wait(1)

    def stop(self):    
        self.state = -1
        self.thread.terminate()
        #self.deleteLater()
        #print('scan: ' + self.name + '...Ended')

    def manage_state(self, stop):
        if(stop == 0):
            if(self.state < 0):
                self.start()
            elif(self.state == 0):
                self.resume()
            elif(self.state == 1):
                self.pause()
        else:
            self.stop()

    def set_name(self, name):
        self.name = name

    def set_filepath(self, path):
        self.file = path

    #jacob's worker.run and run_file
    def run_file(self):
        os.system(self.file+' '+self.params)
