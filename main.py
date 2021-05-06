from PyQt5 import QtCore, QtGui, QtWidgets
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement, BatchStatement
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QTableWidgetItem
import dbmanager
import file_browser 
import gui, scan, calendar, time, os
from subprocess import Popen, PIPE

scans = []

#Clicking Save in the Configuration Run Window
def saveConfigurationRun(Ui_RunWindow):
    
    run_name = Ui_RunWindow.textEdit_12.toPlainText()
    run_description = Ui_RunWindow.textEdit_13.toPlainText()
    whitelisted_ip = Ui_RunWindow.textEdit_14.toPlainText()
    blacklisted_ip = Ui_RunWindow.textEdit_15.toPlainText()

    # scan_type = Ui_RunWindow.comboBox.currentText()
    # configuration_file = Ui_RunWindow.textEdit_16.toPlainText()

    
    print(run_name)
    print(run_description)
    print(whitelisted_ip)
    print(blacklisted_ip)

    # print(scan_type)
    # print(configuration_file)

    
    dbmanager.insertQuery(
        "INSERT INTO Configuration_Run (run_name, run_description, whitelisted_ip, blacklisted_ip) VALUES (%s, %s, %s, %s)",
        (run_name, run_description, whitelisted_ip, blacklisted_ip))
    
    updateRunListAddedTool(Ui_RunWindow, run_name, run_description)
    
    # clear text boxes
    Ui_RunWindow.textEdit_12.clear()
    Ui_RunWindow.textEdit_13.clear()
    Ui_RunWindow.textEdit_14.clear()
    Ui_RunWindow.textEdit_15.clear()
    Ui_RunWindow.textEdit_16.clear()
    

#Return the next available row for the Tool List table
def nextAvailableRowToolSpecification(Ui_RunWindow):
    
    count = 0 
    
    statement = SimpleStatement("SELECT * FROM tutorialspoint.tool_specification", fetch_size=10)
    for user_row in dbmanager.selectQuery(statement):
        count += 1
        
    return count
  
#Return the next available row for the Run List table 
def nextAvailableRowConfigRun(Ui_RunWindow):
    
    count = 0 
    
    statement = SimpleStatement("SELECT * FROM tutorialspoint.configuration_run", fetch_size=10)
    for user_row in dbmanager.selectQuery(statement):
        count += 1
        
    return count  


#Update the run list table when there's a new value
def updateRunListAddedTool(Ui_RunWindow, run_name, description):
    
    row = nextAvailableRowConfigRun(Ui_RunWindow)
    
    print("new available row is", row)
    
    row = row - 1
    
    item = Ui_RunWindow.RunListTable.item(row, 0)
    
    Ui_RunWindow.comboBox_2.addItem(run_name)

    print("Run added: ", run_name)
    
    _translate = QtCore.QCoreApplication.translate
    
    item.setText(_translate("RunWindow", run_name))
    
    item = Ui_RunWindow.RunListTable.item(row, 1)
    
    print("Description: ", description)
    
    _translate = QtCore.QCoreApplication.translate
    
    item.setText(_translate("RunWindow", description))
    
    statement = f"SELECT scan_type FROM configuration_run WHERE run_name = '{run_name}'"
    tool_list = dbmanager.selectQuery(statement)[0][0]
    for tool in tool_list:
        updateScanTable(Ui_RunWindow, tool)


#Update the tool list table when there's a new value
def updateToolListAddedTool(Ui_RunWindow, new_tool, description):
    
    row = nextAvailableRowToolSpecification(Ui_RunWindow)
    
    row = row - 1
    
    item = Ui_RunWindow.RunListTable_2.item(row, 0)
    
    print("Tool added: ", new_tool)
    
    _translate = QtCore.QCoreApplication.translate
    
    Ui_RunWindow.comboBox.setItemText(row, _translate("RunWindow", new_tool))
    
    item.setText(_translate("RunWindow", new_tool))
    
    item = Ui_RunWindow.RunListTable_2.item(row, 1)
    
    print("Description: ", description)
    
    _translate = QtCore.QCoreApplication.translate
    
    item.setText(_translate("RunWindow", description))
    
    

#Update the scan list table when there's a new run 
def updateScanTable(Ui_RunWindow, new_tool):
    rows = Ui_RunWindow.tableWidget.rowCount()
    occupied = 0
    
    for i in range(rows):
        cell = Ui_RunWindow.tableWidget.item(i,0)
        if cell and cell.text():
            occupied = occupied + 1

    Ui_RunWindow.tableWidget.setItem(occupied,0, QTableWidgetItem(new_tool))
    Ui_RunWindow.tableWidget.setItem(occupied,1, QTableWidgetItem(str(occupied)))
    print(f"ADDED .... Tool: {new_tool}")
    #_translate = QtCore.QCoreApplication.translate
    
    '''if row == 0:
        #Ui_RunWindow.tabWidget.addTab(Ui_RunWindow.scan_1, new_tool)
        Ui_RunWindow.tabWidget.setTabText(Ui_RunWindow.tabWidget.indexOf(Ui_RunWindow.scan_1), _translate("RunWindow", new_tool))
    else:
        Ui_RunWindow.tabWidget.setTabText(Ui_RunWindow.tabWidget.indexOf(Ui_RunWindow.scan_2), _translate("RunWindow", new_tool))
        #Ui_RunWindow.tabWidget.addTab(Ui_RunWindow.scan_2, new_tool)'''
    

#Update the scan list table start time when scan starts
def scanTableEndTime(Ui_RunWindow, success, output, row):
    
    ts = calendar.timegm(time.gmtime())

    
    Ui_RunWindow.tableWidget.setItem(row,3, QTableWidgetItem(str(ts)))
    if success is True:
        Ui_RunWindow.tableWidget.setItem(row,4, QTableWidgetItem("Success"))
        if row == 0:
             Ui_RunWindow.textEdit_2.setText(output)
        if row == 1:
             Ui_RunWindow.textEdit_5.setText(output)
        if row == 2:
             Ui_RunWindow.textEdit_122.setText(output)
    else:
        Ui_RunWindow.tableWidget.setItem(row,4, QTableWidgetItem("Failure"))
        if row == 0:
             Ui_RunWindow.textEdit_2.setText(output)
        if row == 1:
             Ui_RunWindow.textEdit_5.setText(output)
        if row == 2:
             Ui_RunWindow.textEdit_122.setText(output)

        
#Update the scan list table start time when scan starts
def scanTableStartTime(Ui_RunWindow, row):
    
    ts = calendar.timegm(time.gmtime())
    
    Ui_RunWindow.tableWidget.setItem(row,2, QTableWidgetItem(str(ts)))
    
    
#Get Description for Run List Table   
def getDescriptionConfigRun(self, row):
        
        count = 0
        
        statement = SimpleStatement("SELECT * FROM tutorialspoint.configuration_run", fetch_size=10)
        for user_row in dbmanager.selectQuery(statement):
            count += 1
    
        if row >= count:
            
            return ""
        
        else:
            data = dbmanager.selectQuery("SELECT run_description FROM tutorialspoint.configuration_run;")   
        
            tool = data[row]
        
            return tool.run_description
        
        
#Get Description for Run List Table   
def getDescriptionToolSpecification(self, row):
        
        count = 0
        
        statement = SimpleStatement("SELECT * FROM tutorialspoint.tool_specification", fetch_size=10)
        for user_row in dbmanager.selectQuery(statement):
            count += 1
    
        if row >= count:
            
            return ""
        
        else:
            data = dbmanager.selectQuery("SELECT tool_description FROM tutorialspoint.tool_specification;")   
        
            tool = data[row]
        
            return tool.tool_description
    
    
# Create Save function for Tool Specification
def saveToolSpecification(Ui_RunWindow):

    tool_name = Ui_RunWindow.textEdit_4.toPlainText()
    tool_description = Ui_RunWindow.textEdit_7.toPlainText()
    tool_path = Ui_RunWindow.textEdit_8.toPlainText()
    option_argument = Ui_RunWindow.textEdit_9.toPlainText()
    tool_data_specification = Ui_RunWindow.textEdit_11.toPlainText()
    tool_specification_file = Ui_RunWindow.textEdit_10.toPlainText()

    dbmanager.insertQuery(
        "INSERT INTO Tool_Specification (tool_name, tool_description, tool_path, option_argument, tool_data_specification, tool_specification_file) VALUES (%s, %s, %s, %s, %s, %s)",
        (tool_name, tool_description, tool_path, option_argument, tool_data_specification,
         tool_specification_file))

    # Ui_RunWindow.retranslateUi.addTooldependency()
    updateToolListAddedTool(Ui_RunWindow, tool_name, tool_description)

    # clear text boxes
    Ui_RunWindow.textEdit_4.clear()
    Ui_RunWindow.textEdit_7.clear()
    Ui_RunWindow.textEdit_8.clear()
    Ui_RunWindow.textEdit_9.clear()
    Ui_RunWindow.textEdit_11.clear()
    Ui_RunWindow.textEdit_10.clear()  
    
    
#Remove from Tool List      
def removeToolList(Ui_RunWindow, button):
    
    tool = Ui_RunWindow.RunListTable_2.item(button, 0)
    
    statement = SimpleStatement("SELECT tool_name FROM tutorialspoint.tool_specification", fetch_size=10)
    for row in dbmanager.selectQuery(statement):
        if row.tool_name == tool.text():
            remove_tool = row.tool_name
    
    tool = Ui_RunWindow.RunListTable_2.item(button, 0)
    
    print("Tool to be removed:", remove_tool)
    
    dbmanager.deleteQuery("DELETE FROM Tool_Specification WHERE tool_name=%s", ([remove_tool]))
    
    if button == 0:
        item = Ui_RunWindow.RunListTable_2.item(0, 0)
        item_description = Ui_RunWindow.RunListTable_2.item(0, 1)
    if button == 1:
        item = Ui_RunWindow.RunListTable_2.item(1, 0)
        item_description = Ui_RunWindow.RunListTable_2.item(1, 1)
    if button == 2:
        item = Ui_RunWindow.RunListTable_2.item(2, 0)
        item_description = Ui_RunWindow.RunListTable_2.item(2, 1)
    if button == 3:
        item = Ui_RunWindow.RunListTable_2.item(3, 0)
        item_description = Ui_RunWindow.RunListTable_2.item(3, 1)
    if button == 4:
        item = Ui_RunWindow.RunListTable_2.item(4, 0)
        item_description = Ui_RunWindow.RunListTable_2.item(4, 1)
    
    item.setText("")
    item_description.setText("")
    
    updateToolListRemovedTool(Ui_RunWindow)   
    
    
# Browse Button
def getFilePath(Ui_RunWindow, button):
    browser = file_browser.App()

    file_path = browser.file_path

    # Tool path browse file browse button
    if button == 17:
        Ui_RunWindow.textEdit_8.setText(file_path)
    # Tool specification file browse button
    if button == 19:
        Ui_RunWindow.textEdit_10.setText(file_path)
    # Run configuration file browse button
    if button == 22:
        Ui_RunWindow.textEdit_16.setText(file_path)   
    
    
    
#Return the tool name of the added tool      
def getNewToolNameToolSpecification(row):
    
    count = 0
    
    statement = SimpleStatement("SELECT * FROM tutorialspoint.tool_specification", fetch_size=10)
    for user_row in dbmanager.selectQuery(statement):
        count += 1

    if row >= count:
        
        return ""
    
    else:

        data = dbmanager.selectQuery("SELECT tool_name FROM tutorialspoint.tool_specification;")        
    
        tool = data[row]
           
        return tool.tool_name   
    
    
    
#Return the tool name of the added tool      
def getNewToolNameConfigurationRun(row):
    
    count = 0
    
    statement = SimpleStatement("SELECT * FROM tutorialspoint.configuration_run", fetch_size=10)
    for user_row in dbmanager.selectQuery(statement):
        count += 1

    if row >= count:
        
        return ""
    
    else:

        data = dbmanager.selectQuery("SELECT run_name FROM tutorialspoint.configuration_run;")
    
        tool = data[row]
    
        return tool.run_name

     
#Pop up window base
def popWindow(title, text):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(text)
        msgBox.setWindowTitle(title)
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')  
 

#confirmation delete window
def deleteDialogue():
    title = "Delete Warning!"
    warning = "Are you sure you want to remove this tool?"
    popWindow(title, warning)

#midscan pause window
def pauseDialogue(Ui_RunWindow, row):
    title = "Mid-Scan Pause"
    warning = "This scan can not be paused after it has been started."
    popWindow(title, warning)
    runListAction(Ui_RunWindow, row,0)

    
#Update the tool list when a tool is removed    
def updateToolListRemovedTool(Ui_RunWindow): 
    
    count = 0
    
    statement = SimpleStatement("SELECT * FROM tutorialspoint.tool_specification", fetch_size=10)
    for user_row in dbmanager.selectQuery(statement):
        count += 1
    
    print(count)
    count = count + 1
    for i in range(count):
        
        item = Ui_RunWindow.RunListTable_2.item(i, 0)
    
        row_value = getNewToolNameToolSpecification(i)
        print("Row value: ", row_value)
        
        _translate = QtCore.QCoreApplication.translate
        
        print("Position", i)
        print("count", count)
        if i == count:
            item.setText(_translate("RunWindow", "")) 
        else:
            item.setText(_translate("RunWindow", row_value)) 
 
#Generate XML   
def generateXML(Ui_RunWindow):
    
    name = Ui_RunWindow.textEdit_3.toPlainText()
    description = Ui_RunWindow.textEdit.toPlainText()
    run = Ui_RunWindow.comboBox_2.currentText()
    
    output = generateXMLReport(Ui_RunWindow, run)
    
    import xml.etree.ElementTree as ET
  
    data = ET.Element('Report')
      
    s_elem1 = ET.SubElement(data, 'Report name')
    s_elem2 = ET.SubElement(data, 'Report description')
    s_elem3 = ET.SubElement(data, 'Run name')
    s_elem4 = ET.SubElement(data, 'Run output')
      
    s_elem1.text = name
    s_elem2.text = description
    s_elem3.text = run
    s_elem4.text = output
      
    b_xml = ET.tostring(data)
      
    with open("Report.xml", "wb") as f:
        f.write(b_xml)
    print("XML Report exported")
    
def generateXMLReport(Ui_RunWindow, run):
    
    tab1 = Ui_RunWindow.tableWidget.item(0,0).text()
    tab2 = Ui_RunWindow.tableWidget.item(1,0).text()
    tab3 = Ui_RunWindow.tableWidget.item(2,0).text()
    
    if (tab1 == run):
        return Ui_RunWindow.textEdit_2.toPlainText()
    if (tab2 == run):
        return Ui_RunWindow.textEdit_5.toPlainText()
    if (tab3 == run):
        return Ui_RunWindow.textEdit_122.toPlainText()
    else:
        return "No result found"
        
    

def refreshToolDependecy(Ui_RunWindow):
    
    _translate = QtCore.QCoreApplication.translate
    count  = 0
    
    statement = SimpleStatement("SELECT * FROM tutorialspoint.tool_dependency", fetch_size=10)
    for user_row in dbmanager.selectQuery(statement):
        count += 1
    
    data = dbmanager.selectQuery("SELECT tool_name FROM tutorialspoint.tool_dependency;")  
    
    for i in range(count):
        
        tool = data[i]
             
        Ui_RunWindow.comboBox_7.setItemText(i+1, _translate("RunWindow", tool.tool_name))
        
    data = dbmanager.selectQuery("SELECT dependent_data FROM tutorialspoint.tool_dependency;")  
    
    for i in range(count):
        
        tool = data[i]
             
        Ui_RunWindow.comboBox_5.setItemText(i+1, _translate("RunWindow", tool.dependent_data))
        
    
    data = dbmanager.selectQuery("SELECT relational_operator FROM tutorialspoint.tool_dependency;")  
    
    for i in range(count):
        
        tool = data[i]
             
        Ui_RunWindow.comboBox_6.setItemText(i+1, _translate("RunWindow", tool.relational_operator))
        

def addTooldependency(Ui_RunWindow):

    tool_name = Ui_RunWindow.comboBox_7.currentText()
    data = Ui_RunWindow.comboBox_5.currentText()
    operator = Ui_RunWindow.comboBox_6.currentText()
    value = Ui_RunWindow.textEdit_17.toPlainText()
    
    if tool_name == "":
        
        print("tool name is empty")
        dependency_expression = Ui_RunWindow.textEdit_6.toPlainText()
        tool_name, data, operator, value = dependency_expression.split(' ', 4)
        
        dbmanager.insertQuery(
        "INSERT INTO Tool_dependency (tool_name, dependent_data, relational_operator, dependent_value) VALUES (%s, %s, %s, %s);",
        (tool_name, data, operator, value))
        
    else:
        print("tool name is not empty")
        dbmanager.insertQuery(
            "INSERT INTO Tool_dependency (tool_name, dependent_data, relational_operator, dependent_value) VALUES (%s, %s, %s, %s);",
            (tool_name, data, operator, value))

    
    # clear text boxes
    Ui_RunWindow.textEdit_6.clear()
    Ui_RunWindow.textEdit_17.clear()
    refreshToolDependecy(Ui_RunWindow)    

def removeTooldependency(Ui_RunWindow):
    data = Ui_RunWindow.comboBox_7.currentText()
    dbmanager.deleteQuery("DELETE FROM tool_dependency WHERE tool_name=%s", ([data]))
    refreshToolDependecy(Ui_RunWindow)

def runListAction(Ui_RunWindow, row, instruction):
    exists = 0
    thisScan = scan.scan()

    for i in scans:
        if(row == i.row):
            i.manage_state(instruction)
            exists = 1
    if(exists == 0):
        print("THE ROW IT'S LOOKING AT IS", row)
        nameOfRun = Ui_RunWindow.RunListTable.item(row, 0).text()
        cluster = Cluster(['127.0.0.1'], port=9042)
        # Database Credentials
        session = cluster.connect()
        statement = None
        import traceback
         
        try:
            print(nameOfRun)
            statement = SimpleStatement("SELECT tool_path FROM tutorialspoint.tool_specification WHERE tool_name = '{}';".format(nameOfRun), fetch_size=10)
            filepath = session.execute(statement)[0][0]
            print(filepath)
            statement = SimpleStatement("SELECT option_argument FROM tutorialspoint.tool_specification WHERE tool_name = '{}';".format(nameOfRun), fetch_size=10)
            params = session.execute(statement)[0][0]
            scanTableStartTime(Ui_RunWindow, row)
        
            print(filepath,params)

            thisScan.file = filepath
            thisScan.params = params
            thisScan.row = row
            thisScan.manage_state(0)
            
            sc = filepath+' '+params
            stdout = Popen(sc, shell=True, stdout=PIPE).stdout
            output = stdout.read().decode()
            if (output == ""):
                print("Nothing was returned")
                scanTableEndTime(Ui_RunWindow, False, "Scan failed", row)
                traceback.print_exc()
            else:        
                scanTableEndTime(Ui_RunWindow, True, output, row)
    
        except:
            print("File Not found")
            scanTableEndTime(Ui_RunWindow, False, "Scan failed", row)
            traceback.print_exc()
        scans.append(thisScan)
        


def addToolToScanType(row,selection):
    dbmanager.updateList("configuration_run", "scan_type", "run_name", row, [selection])  


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RunWindow = QtWidgets.QWidget()
    ui = gui.Ui_RunWindow()
    ui.setupUi(RunWindow)
    RunWindow.show()
    sys.exit(app.exec_())
