from PyQt5 import QtCore, QtGui, QtWidgets
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement, BatchStatement
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
import dbmanager
import file_browser
   

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

    #data = dbmanager.selectQuery("SELECT dependent_data, relational_operator, dependent_value FROM tutorialspoint.tool_dependency;")
    
    _translate = QtCore.QCoreApplication.translate
    count  = 0
    
    statement = SimpleStatement("SELECT * FROM tutorialspoint.tool_specification", fetch_size=10)
    for user_row in dbmanager.selectQuery(statement):
        count += 1
    
    data = dbmanager.selectQuery("SELECT tool_name FROM tutorialspoint.tool_specification;")  
    
    for i in range(count):
        
        tool = data[i]
             
        Ui_RunWindow.comboBox_7.setItemText(i, _translate("RunWindow", tool.tool_name))
        

    # print(str(data))

   #for row in data:
        # for i in row:
        # print(row, i)
        # Ui_RunWindow.comboBox_5.addItem(row[0])
        # Ui_RunWindow.comboBox_6.addItem(row[1])


def addTooldependency(Ui_RunWindow):

    tool_name = Ui_RunWindow.comboBox_7.currentText()
    data = Ui_RunWindow.comboBox_5.currentText()
    operator = Ui_RunWindow.comboBox_6.currentText()
    value = Ui_RunWindow.textEdit_17.toPlainText()
    
    dependency_expression = Ui_RunWindow.textEdit_6

    dbmanager.insertQuery(
        "INSERT INTO Tool_dependency (tool_name, dependent_data, relational_operator, dependent_value) VALUES (%s, %s, %s, %s);",
        (tool_name, data, operator, value))

    #Clear text boxes
    Ui_RunWindow.textEdit_17.clear()
    dependency_expression.setText(tool_name + " -> " + data + operator + value)
    refreshToolDependecy(Ui_RunWindow)


def removeTooldependency(Ui_RunWindow):
    data = Ui_RunWindow.comboBox_5.currentText()
    print(data)
    dbmanager.deleteQuery("DELETE FROM Tool_dependency WHERE dependent_data=%s", (str(data)))
    Ui_RunWindow.refreshToolDependecy()


