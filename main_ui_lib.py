# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'template.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1287, 824)
        MainWindow.setToolTipDuration(-3)
        MainWindow.setWhatsThis("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 20, 681, 182))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.basic_info = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.basic_info.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.basic_info.setContentsMargins(0, 0, 0, 0)
        self.basic_info.setObjectName("basic_info")
        self.txt_name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_name.setInputMask("")
        self.txt_name.setText("")
        self.txt_name.setPlaceholderText("Type Full Name")
        self.txt_name.setObjectName("txt_name")
        self.basic_info.addWidget(self.txt_name, 0, 1, 1, 1)
        self.lbl_position = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_position.setObjectName("lbl_position")
        self.basic_info.addWidget(self.lbl_position, 1, 0, 1, 1)
        self.lbl_git = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_git.setObjectName("lbl_git")
        self.basic_info.addWidget(self.lbl_git, 5, 0, 1, 1)
        self.lbl_email = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_email.setObjectName("lbl_email")
        self.basic_info.addWidget(self.lbl_email, 3, 0, 1, 1)
        self.lbl_name = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_name.setObjectName("lbl_name")
        self.basic_info.addWidget(self.lbl_name, 0, 0, 1, 1)
        self.lbl_linkd = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_linkd.setObjectName("lbl_linkd")
        self.basic_info.addWidget(self.lbl_linkd, 4, 0, 1, 1)
        self.lbl_loc = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_loc.setObjectName("lbl_loc")
        self.basic_info.addWidget(self.lbl_loc, 2, 0, 1, 1)
        self.txt_position = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_position.setInputMask("")
        self.txt_position.setText("")
        self.txt_position.setPlaceholderText("The Position you are applying for")
        self.txt_position.setObjectName("txt_position")
        self.basic_info.addWidget(self.txt_position, 1, 1, 1, 1)
        self.txt_loc = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_loc.setInputMask("")
        self.txt_loc.setText("")
        self.txt_loc.setPlaceholderText("The Place you are currently located")
        self.txt_loc.setObjectName("txt_loc")
        self.basic_info.addWidget(self.txt_loc, 2, 1, 1, 1)
        self.txt_email = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.txt_email.setFont(font)
        self.txt_email.setInputMask("")
        self.txt_email.setText("")
        self.txt_email.setPlaceholderText("john.smith09@gmail.com")
        self.txt_email.setObjectName("txt_email")
        self.basic_info.addWidget(self.txt_email, 3, 1, 1, 1)
        self.txt_linkd = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.txt_linkd.setFont(font)
        self.txt_linkd.setInputMask("")
        self.txt_linkd.setText("")
        self.txt_linkd.setPlaceholderText("john.smith")
        self.txt_linkd.setObjectName("txt_linkd")
        self.basic_info.addWidget(self.txt_linkd, 4, 1, 1, 1)
        self.txt_git = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.txt_git.setFont(font)
        self.txt_git.setInputMask("")
        self.txt_git.setText("")
        self.txt_git.setPlaceholderText("john-smith09")
        self.txt_git.setObjectName("txt_git")
        self.basic_info.addWidget(self.txt_git, 5, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(40, 240, 711, 103))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.skills = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.skills.setContentsMargins(0, 0, 0, 0)
        self.skills.setObjectName("skills")
        self.tbl_skills = QtWidgets.QTableWidget(self.gridLayoutWidget_2)
        self.tbl_skills.setGridStyle(QtCore.Qt.SolidLine)
        self.tbl_skills.setRowCount(1)
        self.tbl_skills.setObjectName("tbl_skills")
        self.tbl_skills.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_skills.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_skills.setHorizontalHeaderItem(1, item)
        self.skills.addWidget(self.tbl_skills, 0, 0, 1, 1)
        self.toolbtn_skills = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        self.toolbtn_skills.setToolTip("<html><head/><body><p>Add or Remove rows</p></body></html>")
        self.toolbtn_skills.setText("...")
        self.toolbtn_skills.setObjectName("toolbtn_skills")
        self.skills.addWidget(self.toolbtn_skills, 0, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.btn_make = QtWidgets.QPushButton(self.centralwidget)
        self.btn_make.setGeometry(QtCore.QRect(950, 310, 221, 121))
        self.btn_make.setObjectName("btn_make")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(40, 380, 711, 103))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.courses = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.courses.setContentsMargins(0, 0, 0, 0)
        self.courses.setObjectName("courses")
        self.tbl_courses = QtWidgets.QTableWidget(self.gridLayoutWidget_3)
        self.tbl_courses.setToolTipDuration(-1)
        self.tbl_courses.setStatusTip("")
        self.tbl_courses.setWhatsThis("")
        self.tbl_courses.setAccessibleName("")
        self.tbl_courses.setAccessibleDescription("")
        self.tbl_courses.setGridStyle(QtCore.Qt.SolidLine)
        self.tbl_courses.setRowCount(1)
        self.tbl_courses.setObjectName("tbl_courses")
        self.tbl_courses.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_courses.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_courses.setHorizontalHeaderItem(1, item)
        self.courses.addWidget(self.tbl_courses, 0, 0, 1, 1)
        self.toolbtn_courses = QtWidgets.QToolButton(self.gridLayoutWidget_3)
        self.toolbtn_courses.setToolTip("<html><head/><body><p>Add or Remove rows</p></body></html>")
        self.toolbtn_courses.setText("...")
        self.toolbtn_courses.setObjectName("toolbtn_courses")
        self.courses.addWidget(self.toolbtn_courses, 0, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(40, 520, 711, 103))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.education = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.education.setContentsMargins(0, 0, 0, 0)
        self.education.setObjectName("education")
        self.tbl_edu = QtWidgets.QTableWidget(self.gridLayoutWidget_4)
        self.tbl_edu.setToolTip("")
        self.tbl_edu.setToolTipDuration(-1)
        self.tbl_edu.setStatusTip("")
        self.tbl_edu.setWhatsThis("")
        self.tbl_edu.setAccessibleName("")
        self.tbl_edu.setAccessibleDescription("")
        self.tbl_edu.setGridStyle(QtCore.Qt.SolidLine)
        self.tbl_edu.setRowCount(1)
        self.tbl_edu.setObjectName("tbl_edu")
        self.tbl_edu.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_edu.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_edu.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_edu.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_edu.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_edu.setHorizontalHeaderItem(4, item)
        self.education.addWidget(self.tbl_edu, 0, 0, 1, 1)
        self.toolbtn_edu = QtWidgets.QToolButton(self.gridLayoutWidget_4)
        self.toolbtn_edu.setToolTip("<html><head/><body><p>Add or Remove rows</p></body></html>")
        self.toolbtn_edu.setText("...")
        self.toolbtn_edu.setObjectName("toolbtn_edu")
        self.education.addWidget(self.toolbtn_edu, 0, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(40, 660, 711, 103))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.job_history = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.job_history.setContentsMargins(0, 0, 0, 0)
        self.job_history.setObjectName("job_history")
        self.tbl_jobs = QtWidgets.QTableWidget(self.gridLayoutWidget_5)
        self.tbl_jobs.setToolTip("")
        self.tbl_jobs.setToolTipDuration(-1)
        self.tbl_jobs.setStatusTip("")
        self.tbl_jobs.setWhatsThis("")
        self.tbl_jobs.setAccessibleName("")
        self.tbl_jobs.setAccessibleDescription("")
        self.tbl_jobs.setGridStyle(QtCore.Qt.SolidLine)
        self.tbl_jobs.setRowCount(1)
        self.tbl_jobs.setObjectName("tbl_jobs")
        self.tbl_jobs.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_jobs.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_jobs.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_jobs.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_jobs.setHorizontalHeaderItem(3, item)
        self.job_history.addWidget(self.tbl_jobs, 0, 0, 1, 1)
        self.toolbtn_jobs = QtWidgets.QToolButton(self.gridLayoutWidget_5)
        self.toolbtn_jobs.setToolTip("<html><head/><body><p>Add or Remove rows</p></body></html>")
        self.toolbtn_jobs.setText("...")
        self.toolbtn_jobs.setObjectName("toolbtn_jobs")
        self.job_history.addWidget(self.toolbtn_jobs, 0, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1287, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionRecents = QtWidgets.QAction(MainWindow)
        self.actionRecents.setObjectName("actionRecents")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionRecents)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_position.setText(_translate("MainWindow", "Position:"))
        self.lbl_git.setText(_translate("MainWindow", "GitHub Username:"))
        self.lbl_email.setText(_translate("MainWindow", "Email Address: "))
        self.lbl_name.setText(_translate("MainWindow", "Full Name: "))
        self.lbl_linkd.setText(_translate("MainWindow", "Linkedin Username: "))
        self.lbl_loc.setText(_translate("MainWindow", "Location: "))
        self.tbl_skills.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Enter Skills &amp; Strengths in a comma seperated list</span></p><p><span style=\" font-style:italic;\">Python, SQL, MongoDB</span></p></body></html>"))
        item = self.tbl_skills.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Category"))
        item = self.tbl_skills.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Skills"))
        self.btn_make.setText(_translate("MainWindow", "MAKE DOCX"))
        self.tbl_courses.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Enter Courses in a comma seperated list</span></p><p><span style=\" font-style:italic;\">Calculus, Calculus 2, Linear Algebra</span></p></body></html>"))
        item = self.tbl_courses.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Subject"))
        item = self.tbl_courses.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Course"))
        self.toolbtn_courses.setWhatsThis(_translate("MainWindow", "d"))
        item = self.tbl_edu.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "School Name"))
        item = self.tbl_edu.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Location"))
        item = self.tbl_edu.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Major"))
        item = self.tbl_edu.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "GPA"))
        item = self.tbl_edu.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Start & End"))
        self.toolbtn_edu.setWhatsThis(_translate("MainWindow", "d"))
        item = self.tbl_jobs.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Job Title"))
        item = self.tbl_jobs.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Company"))
        item = self.tbl_jobs.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Start & End"))
        item = self.tbl_jobs.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Description"))
        self.toolbtn_jobs.setWhatsThis(_translate("MainWindow", "d"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionSave_As.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionRecents.setText(_translate("MainWindow", "Recents"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
