from PyQt5 import QtCore, QtGui, QtWidgets
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement, BatchStatement
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
import dbmanager
import file_browser 
import gui, scan

scans = []

#Clicking Save in the Configuration Run Window
def saveConfigurationRun(Ui_RunWindow):
    
    run_name = Ui_RunWindow.textEdit_12.toPlainText()
    run_description = Ui_RunWindow.textEdit_13.toPlainText()
    whitelisted_ip = Ui_RunWindow.textEdit_14.toPlainText()
    blacklisted_ip = Ui_RunWindow.textEdit_15.toPlainText()
    scan_type = Ui_RunWindow.comboBox.currentText()
    configuration_file = Ui_RunWindow.textEdit_16.toPlainText()
    
    print(run_name)
    print(run_description)
    print(whitelisted_ip)
    print(blacklisted_ip)
    print(scan_type)
    print(configuration_file)
    
    dbmanager.insertQuery(
        "INSERT INTO Configuration_Run (run_name, run_description, whitelisted_ip, blacklisted_ip, scan_type, configuration_file) VALUES (%s, %s, %s, %s, %s, %s)",
        (run_name, run_description, whitelisted_ip, blacklisted_ip, scan_type, configuration_file))
    
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
def updateRunListAddedTool(Ui_RunWindow, new_tool, description):
    
    row = nextAvailableRowConfigRun(Ui_RunWindow)
    
    print("new available row is", row)
    
    row = row - 1
    
    item = Ui_RunWindow.RunListTable.item(row, 0)

    print("Tool added: ", new_tool)
    
    _translate = QtCore.QCoreApplication.translate
    
    item.setText(_translate("RunWindow", new_tool))
    
    item = Ui_RunWindow.RunListTable.item(row, 1)
    
    print("Description: ", description)
    
    _translate = QtCore.QCoreApplication.translate
    
    item.setText(_translate("RunWindow", description))


#Update the tool list table when there's a new value
def updateToolListAddedTool(Ui_RunWindow, new_tool, description):
    
    row = nextAvailableRowToolSpecification(Ui_RunWindow)
    
    row = row - 1
    
    item = Ui_RunWindow.RunListTable_2.item(row, 0)
    
    print("Tool added: ", new_tool)
    
    _translate = QtCore.QCoreApplication.translate
    
    item.setText(_translate("RunWindow", new_tool))
    
    item = Ui_RunWindow.RunListTable_2.item(row, 1)
    
    print("Description: ", description)
    
    _translate = QtCore.QCoreApplication.translate
    
    item.setText(_translate("RunWindow", description))
    
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
    
 
#Confirmation delete window
def showDialog(Ui_RunWindow):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Are you sure you want to remove this tool?")
        msgBox.setWindowTitle("QMessageBox Example")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')  
 
    
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
    #name = Ui_RunWindow.RunListTable.item(row,0).text()
    exists = 0
    thisScan = scan.scan()

    for i in scans:
        if( row == i.row):
            scans.manage_state(instruction)
            exists = 1
    if(exists == 0):
        #thisScan.name = name

        cluster = Cluster(['127.0.0.1'], port=9042)
        # Database Credentials
        session = cluster.connect()
        statement = None
        try:
            statement = SimpleStatement("SELECT tool_path FROM tutorialspoint.tool_specification WHERE tool_name = '{}';".format(nameOfRun), fetch_size=10)
            filepath = session.execute(statement)[0][0]
            statement = SimpleStatement("SELECT option_argument FROM tutorialspoint.tool_specification WHERE tool_name = '{}';".format(nameOfRun), fetch_size=10)
            params = session.execute(statement)[0][0]

            thisScan.file = filepath
            thisScan.row = row
            thisScan.manage_state(0)
        except:
            print("File Not found")
        scans.append(thisScan)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RunWindow = QtWidgets.QWidget()
    ui = gui.Ui_RunWindow()
    ui.setupUi(RunWindow)
    RunWindow.show()
    sys.exit(app.exec_())
