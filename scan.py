from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, QThread
from PyQt5.QtWidgets import QTableWidgetItem
import os, time, calendar
from subprocess import Popen, PIPE

global playButton, pauseButton, stopButton

class worker(QThread):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    filepath = ''
    params = ''
    row = None
    ui = None
    output = None
    #main = None

    def run(self):
        sc = self.filepath+' '+self.params
        stdout = Popen(sc, shell=True, stdout=PIPE).stdout
        output = stdout.read().decode()
        if output == "":
            print("Nothing was returned")
            self.scanTableEndTime(self.ui, False, "Scan failed", self.row)
        else:
            self.scanTableEndTime(self.ui, True, output, self.row)
  
    #def run_deprecated(self):
        #os.system(self.filepath+' '+self.params)
    
    def scanTableEndTime(self, ui, success, output, row):
        
        ts = calendar.timegm(time.gmtime())
        ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(ts)))
        self.output = output
        if success:
            ui.tableWidget.setItem(row,4,QTableWidgetItem("Success"))
            if row == 0:
                ui.textEdit_2.setText(self.output)
            if row == 1:
                ui.textEdit_5.setText(self.output)
            if row == 2:
                ui.textEdit_122.setText(self.output)
        else:
            ui.tableWidget.setItem(row,4,QTableWidgetItem("Failure"))
            '''
            if row == 0:
                ui.textEdit_2.setText(output)
            if row == 1:
                ui.textEdit_5.setText(output)
            if row == 2:
                ui.textEdit_122.setText(output)
            '''
        self.output = output

class scan(QObject):
    def __init__(self):
        self.name = ''
        self.row = -1
        #states 0 = paused 1 = running -1 = finished
        self.state = -2
        self.file = ''
        self.params = ''
        self.row = None
        self.ui = None
        self.output = None
        #self.main = None
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
            self.thread.ui = self.ui
            self.thread.row = self.row
            #self.thread.main = self.main
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

   
