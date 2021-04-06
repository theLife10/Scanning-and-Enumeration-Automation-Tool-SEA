from PyQt5.uic.properties import QtCore
from cassandra.query import SimpleStatement
import Ui_RunWindow
import dbmanager
import file_browser


def saveConfigurationRun(Ui_RunWindow):

    run_name = Ui_RunWindow.retranslateUi.textEdit_12.toPlainText()
    run_description = Ui_RunWindow.retranslateUi.textEdit_13.toPlainText()
    whitelisted_ip = Ui_RunWindow.retranslateUi.textEdit_14.toPlainText()
    blacklisted_ip = Ui_RunWindow.retranslateUi.textEdit_15.toPlainText()
    scan_type = Ui_RunWindow.retranslateUi.comboBox.currentText()
    configuration_file = Ui_RunWindow.retranslateUi.textEdit_16.toPlainText()
    statement = "INSERT INTO Configuration_Run (run_name, run_description, whitelisted_ip, blacklisted_ip, scan_type, configuration_file) VALUES (%s, %s, %s, %s, %s, %s)"
    variables = [(run_name, run_description, whitelisted_ip, blacklisted_ip, scan_type, configuration_file)]
    dbmanager.query(
        statement,variables)
    # clear text boxes
    Ui_RunWindow.retranslateUi.textEdit_12.clear()
    Ui_RunWindow.retranslateUi.textEdit_13.clear()
    Ui_RunWindow.retranslateUi.textEdit_14.clear()
    Ui_RunWindow.retranslateUi.textEdit_15.clear()
    Ui_RunWindow.retranslateUi.textEdit_16.clear()


# Update the tool list table when there's a new value
def newValueToolList(Ui_RunWindow):
    row = Ui_RunWindow.retranslateUi.nextAvailableRow()

    item = Ui_RunWindow.retranslateUi.RunListTable_2.item(row, 0)

    row_value = Ui_RunWindow.retranslateUi.updateToolList(row)

    _translate = QtCore.QCoreApplication.translate

    item.setText(_translate("RunWindow", row_value))


# Return the next available row
def nextAvailableRow():
    count = 0
    statement = "SELECT * FROM tutorialspoint.tool_specification"
    for user_row in dbmanager.selectQuery(statement):
        count += 1

    print("New row position: ", count)
    return count

    # Tool Dependency


def refreshToolDependecy(Ui_RunWindow):

    data = dbmanager.query(
        "SELECT dependent_data, relational_operator, dependent_value FROM tutorialspoint.tool_dependency;")

    print(str(data))

    # dependent_data, opperator, value = data[]
    cnt = 0
    for row in data:
        # for i in row:
        # print(row, i)
        Ui_RunWindow.retranslateUi.comboBox_5.addItem(row[0])
        Ui_RunWindow.retranslateUi.comboBox_6.addItem(row[1])
        # Ui_RunWindow.retranslateUi.textEdit_5.setPlainText(i)


def addTooldependency(Ui_RunWindow):

    # tool_name = Ui_RunWindow.retranslateUi.textEdit_4.toPlainText()
    dependency_expression = Ui_RunWindow.retranslateUi.textEdit_6.toPlainText()
    # print(dependency_expression)
    tool_name, data, operator, value = dependency_expression.split(' ', 4)
    # print(f' Data : {data} OPP: {operator} Value: {value}')

    dbmanager.insertQuery(
        "INSERT INTO Tool_dependency (tool_name, dependent_data, relational_operator, dependent_value) VALUES (%s, %s, %s, %s)",
        (tool_name, data, operator, value))

    # clear text boxes
    Ui_RunWindow.retranslateUi.textEdit_6.clear()
    Ui_RunWindow.retranslateUi.refreshToolDependecy()


def removeTooldependency(Ui_RunWindow):
    data = Ui_RunWindow.retranslateUi.comboBox_5.currentText()
    print(data)
    dbmanager.query("DELETE FROM Tool_dependency WHERE dependent_data=%s", (str(data)))
    Ui_RunWindow.retranslateUi.refreshToolDependecy()


# Create Save function for Tool Specification
def saveToolSpecification(Ui_RunWindow):

    tool_name = Ui_RunWindow.retranslateUi.textEdit_4.toPlainText()
    tool_description = Ui_RunWindow.retranslateUi.textEdit_7.toPlainText()
    tool_path = Ui_RunWindow.retranslateUi.textEdit_8.toPlainText()
    option_argument = Ui_RunWindow.retranslateUi.textEdit_9.toPlainText()
    tool_data_specification = Ui_RunWindow.retranslateUi.textEdit_11.toPlainText()
    tool_specification_file = Ui_RunWindow.retranslateUi.textEdit_10.toPlainText()

    dbmanager.query(
        "INSERT INTO Tool_Specification (tool_name, tool_description, tool_path, option_argument, tool_data_specification, tool_specification_file) VALUES (%s, %s, %s, %s, %s, %s)",
        (tool_name, tool_description, tool_path, option_argument, tool_data_specification,
         tool_specification_file))

    # Ui_RunWindow.retranslateUi.addTooldependency()

    # clear text boxes
    Ui_RunWindow.retranslateUi.textEdit_4.clear()
    Ui_RunWindow.retranslateUi.textEdit_7.clear()
    Ui_RunWindow.retranslateUi.textEdit_8.clear()
    Ui_RunWindow.retranslateUi.textEdit_9.clear()
    Ui_RunWindow.retranslateUi.textEdit_11.clear()
    Ui_RunWindow.retranslateUi.textEdit_10.clear()


# Remove from Tool List
def removeToolList(Ui_RunWindow, button):
    data = dbmanager.selectQuery("SELECT tool_name FROM tutorialspoint.tool_specification;")
    print(button)
    tool = data[button]
    print(tool)

    dbmanager.deleteQuery("DELETE FROM Tool_Specification WHERE tool_name=%s", ([tool.tool_name]))

    item = Ui_RunWindow.RunListTable_2.item(0, 0)

    if button == 1:
        item = Ui_RunWindow.RunListTable_2.item(1, 0)
    if button == 2:
        item = Ui_RunWindow.RunListTable_2.item(2, 0)
    if button == 3:
        item = Ui_RunWindow.RunListTable_2.item(3, 0)
    if button == 4:
        item = Ui_RunWindow.RunListTable_2.item(4, 0)

    item.setText("")


# Update Tool List
def updateToolList(row):
    count = 0
    statement = ("SELECT * FROM tutorialspoint.tool_specification")
    for user_row in dbmanager.selectQuery(statement):
        count += 1
    # print(count)
    if count <= row:
        # Close connection
        #session.shutdown()
        return "null"
    else:
        data = dbmanager.selectQuery("SELECT tool_name FROM tutorialspoint.tool_specification;")
        tool = data[row]
        # Close connection
        #session.shutdown()
        # print(tool.tool_name)

        return tool.tool_name


# Browse Button
def getFilePath(Ui_RunWindow, button):
    browser = file_browser.App()

    file_path = browser.file_path

    # Tool path browse button
    if button == 17:
        Ui_RunWindow.retranslateUi.textEdit_8.setText(file_path)
    # Tool specification Browse button
    if button == 19:
        Ui_RunWindow.retranslateUi.textEdit_10.setText(file_path)
    # Run configuration file browse button
    if button == 22:
        Ui_RunWindow.retranslateUi.textEdit_16.setText(file_path)