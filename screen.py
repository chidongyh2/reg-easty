# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1069, 855)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 341, 131))
        self.groupBox_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(30, 60, 51, 20))
        self.label_15.setObjectName("label_15")
        self.threadCount = QtWidgets.QSpinBox(self.groupBox_2)
        self.threadCount.setGeometry(QtCore.QRect(90, 60, 42, 20))
        self.threadCount.setProperty("value", 2)
        self.threadCount.setObjectName("threadCount")
        self.LD_link = QtWidgets.QLineEdit(self.groupBox_2)
        self.LD_link.setGeometry(QtCore.QRect(58, 20, 221, 20))
        self.LD_link.setObjectName("LD_link")
        self.btn_LD_link = QtWidgets.QToolButton(self.groupBox_2)
        self.btn_LD_link.setGeometry(QtCore.QRect(290, 20, 31, 21))
        self.btn_LD_link.setObjectName("btn_LD_link")
        self.thread_label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.thread_label_2.setGeometry(QtCore.QRect(25, 20, 31, 20))
        self.thread_label_2.setObjectName("thread_label_2")
        self.delayLD_input = QtWidgets.QSpinBox(self.groupBox_2)
        self.delayLD_input.setGeometry(QtCore.QRect(90, 90, 41, 20))
        self.delayLD_input.setProperty("value", 1)
        self.delayLD_input.setObjectName("delayLD_input")
        self.delayLD_label = QtWidgets.QLabel(self.groupBox_2)
        self.delayLD_label.setGeometry(QtCore.QRect(39, 90, 47, 20))
        self.delayLD_label.setObjectName("delayLD_label")
        self.hidden_chrome = QtWidgets.QCheckBox(self.groupBox_2)
        self.hidden_chrome.setGeometry(QtCore.QRect(188, 75, 91, 20))
        self.hidden_chrome.setChecked(True)
        self.hidden_chrome.setObjectName("hidden_chrome")
        self.tab_easty_data = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_easty_data.setGeometry(QtCore.QRect(10, 190, 1051, 621))
        self.tab_easty_data.setObjectName("tab_easty_data")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.table_email = QtWidgets.QTableWidget(self.tab)
        self.table_email.setGeometry(QtCore.QRect(10, 10, 1025, 581))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_email.sizePolicy().hasHeightForWidth())
        self.table_email.setSizePolicy(sizePolicy)
        self.table_email.setMinimumSize(QtCore.QSize(0, 1))
        self.table_email.setMaximumSize(QtCore.QSize(1025, 16777215))
        self.table_email.setMouseTracking(False)
        self.table_email.setTabletTracking(False)
        self.table_email.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.table_email.setLineWidth(1)
        self.table_email.setAutoScrollMargin(16)
        self.table_email.setDragEnabled(False)
        self.table_email.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.table_email.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_email.setShowGrid(True)
        self.table_email.setObjectName("table_email")
        self.table_email.setColumnCount(22)
        self.table_email.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_email.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_email.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_email.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_email.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_email.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_email.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_email.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_email.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_email.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_email.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_email.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_email.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_email.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_email.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_email.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_email.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_email.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_email.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_email.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_email.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_email.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_email.setHorizontalHeaderItem(21, item)
        self.table_email.horizontalHeader().setDefaultSectionSize(170)
        self.table_email.verticalHeader().setStretchLastSection(True)
        self.tab_easty_data.addTab(self.tab, "")
        self.tab_change_mail = QtWidgets.QWidget()
        self.tab_change_mail.setObjectName("tab_change_mail")
        self.table_mail_change = QtWidgets.QTableWidget(self.tab_change_mail)
        self.table_mail_change.setGeometry(QtCore.QRect(10, 10, 1025, 581))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_mail_change.sizePolicy().hasHeightForWidth())
        self.table_mail_change.setSizePolicy(sizePolicy)
        self.table_mail_change.setMinimumSize(QtCore.QSize(0, 1))
        self.table_mail_change.setMaximumSize(QtCore.QSize(1025, 16777215))
        self.table_mail_change.setMouseTracking(False)
        self.table_mail_change.setTabletTracking(False)
        self.table_mail_change.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.table_mail_change.setLineWidth(1)
        self.table_mail_change.setAutoScrollMargin(16)
        self.table_mail_change.setDragEnabled(False)
        self.table_mail_change.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.table_mail_change.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_mail_change.setShowGrid(True)
        self.table_mail_change.setObjectName("table_mail_change")
        self.table_mail_change.setColumnCount(7)
        self.table_mail_change.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_mail_change.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_mail_change.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_mail_change.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_mail_change.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_mail_change.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_mail_change.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_mail_change.setHorizontalHeaderItem(6, item)
        self.table_mail_change.horizontalHeader().setDefaultSectionSize(170)
        self.table_mail_change.verticalHeader().setStretchLastSection(True)
        self.tab_easty_data.addTab(self.tab_change_mail, "")
        self.btn_stop = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stop.setGeometry(QtCore.QRect(130, 150, 51, 31))
        self.btn_stop.setObjectName("btn_stop")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(70, 150, 51, 31))
        self.btn_start.setObjectName("btn_start")
        self.btn_verify_bank = QtWidgets.QPushButton(self.centralwidget)
        self.btn_verify_bank.setGeometry(QtCore.QRect(190, 150, 71, 31))
        self.btn_verify_bank.setObjectName("btn_verify_bank")
        self.btn_check_live = QtWidgets.QPushButton(self.centralwidget)
        self.btn_check_live.setGeometry(QtCore.QRect(270, 150, 71, 31))
        self.btn_check_live.setObjectName("btn_check_live")
        self.btn_load = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load.setGeometry(QtCore.QRect(10, 150, 51, 31))
        self.btn_load.setObjectName("btn_load")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(375, 160, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(490, 160, 51, 16))
        self.label_2.setObjectName("label_2")
        self.label_success = QtWidgets.QLabel(self.centralwidget)
        self.label_success.setGeometry(QtCore.QRect(440, 160, 51, 16))
        self.label_success.setObjectName("label_success")
        self.label_error = QtWidgets.QLabel(self.centralwidget)
        self.label_error.setGeometry(QtCore.QRect(538, 160, 51, 16))
        self.label_error.setObjectName("label_error")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(582, 160, 51, 16))
        self.label_5.setObjectName("label_5")
        self.label_running_status = QtWidgets.QLabel(self.centralwidget)
        self.label_running_status.setGeometry(QtCore.QRect(640, 160, 191, 16))
        self.label_running_status.setObjectName("label_running_status")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setEnabled(True)
        self.groupBox_3.setGeometry(QtCore.QRect(360, 0, 681, 151))
        self.groupBox_3.setInputMethodHints(QtCore.Qt.ImhNone)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_3)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 661, 131))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_easty = QtWidgets.QWidget()
        self.tab_easty.setObjectName("tab_easty")
        self.view_btn_user_views = QtWidgets.QToolButton(self.tab_easty)
        self.view_btn_user_views.setGeometry(QtCore.QRect(710, 50, 31, 21))
        self.view_btn_user_views.setObjectName("view_btn_user_views")
        self.delayLD_label_2 = QtWidgets.QLabel(self.tab_easty)
        self.delayLD_label_2.setGeometry(QtCore.QRect(20, 40, 51, 20))
        self.delayLD_label_2.setObjectName("delayLD_label_2")
        self.stepComboBox = QtWidgets.QComboBox(self.tab_easty)
        self.stepComboBox.setGeometry(QtCore.QRect(74, 40, 111, 20))
        self.stepComboBox.setObjectName("stepComboBox")
        self.stepComboBox.addItem("")
        self.stepComboBox.addItem("")
        self.stepComboBox.addItem("")
        self.stepComboBox.addItem("")
        self.stepComboBox.addItem("")
        self.stepComboBox.addItem("")
        self.update_info_mail = QtWidgets.QCheckBox(self.tab_easty)
        self.update_info_mail.setGeometry(QtCore.QRect(210, 40, 101, 20))
        self.update_info_mail.setChecked(True)
        self.update_info_mail.setObjectName("update_info_mail")
        self.tabWidget.addTab(self.tab_easty, "")
        self.tab_gmail = QtWidgets.QWidget()
        self.tab_gmail.setObjectName("tab_gmail")
        self.select_password = QtWidgets.QSplitter(self.tab_gmail)
        self.select_password.setGeometry(QtCore.QRect(110, 10, 71, 91))
        self.select_password.setOrientation(QtCore.Qt.Vertical)
        self.select_password.setObjectName("select_password")
        self.pass_random = QtWidgets.QRadioButton(self.select_password)
        self.pass_random.setChecked(True)
        self.pass_random.setObjectName("pass_random")
        self.pass_general = QtWidgets.QRadioButton(self.select_password)
        self.pass_general.setObjectName("pass_general")
        self.pass_specific = QtWidgets.QRadioButton(self.select_password)
        self.pass_specific.setObjectName("pass_specific")
        self.input_pass_general = QtWidgets.QLineEdit(self.tab_gmail)
        self.input_pass_general.setGeometry(QtCore.QRect(190, 50, 111, 20))
        self.input_pass_general.setObjectName("input_pass_general")
        self.label_8 = QtWidgets.QLabel(self.tab_gmail)
        self.label_8.setGeometry(QtCore.QRect(190, 30, 111, 16))
        self.label_8.setObjectName("label_8")
        self.select_gmail = QtWidgets.QSplitter(self.tab_gmail)
        self.select_gmail.setGeometry(QtCore.QRect(420, 10, 80, 91))
        self.select_gmail.setOrientation(QtCore.Qt.Vertical)
        self.select_gmail.setObjectName("select_gmail")
        self.gmail_random = QtWidgets.QRadioButton(self.select_gmail)
        self.gmail_random.setChecked(True)
        self.gmail_random.setObjectName("gmail_random")
        self.gmail_general = QtWidgets.QRadioButton(self.select_gmail)
        self.gmail_general.setObjectName("gmail_general")
        self.gmail_specific = QtWidgets.QRadioButton(self.select_gmail)
        self.gmail_specific.setObjectName("gmail_specific")
        self.label_9 = QtWidgets.QLabel(self.tab_gmail)
        self.label_9.setGeometry(QtCore.QRect(510, 30, 111, 16))
        self.label_9.setObjectName("label_9")
        self.input_gmail_general = QtWidgets.QLineEdit(self.tab_gmail)
        self.input_gmail_general.setGeometry(QtCore.QRect(510, 50, 141, 20))
        self.input_gmail_general.setObjectName("input_gmail_general")
        self.change_password = QtWidgets.QCheckBox(self.tab_gmail)
        self.change_password.setGeometry(QtCore.QRect(10, 45, 91, 17))
        self.change_password.setObjectName("change_password")
        self.change_mail_2 = QtWidgets.QCheckBox(self.tab_gmail)
        self.change_mail_2.setGeometry(QtCore.QRect(330, 45, 81, 17))
        self.change_mail_2.setObjectName("change_mail_2")
        self.tabWidget.addTab(self.tab_gmail, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1069, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab_easty_data.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_15.setText(_translate("MainWindow", "Số luồng:"))
        self.LD_link.setText(_translate("MainWindow", "D:\\anyfolder"))
        self.btn_LD_link.setText(_translate("MainWindow", "..."))
        self.thread_label_2.setText(_translate("MainWindow", "Path:"))
        self.delayLD_label.setText(_translate("MainWindow", "Delay:"))
        self.hidden_chrome.setText(_translate("MainWindow", "Ẩn trình duyệt"))
        item = self.table_email.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Proxy"))
        item = self.table_email.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Email"))
        item = self.table_email.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Password"))
        item = self.table_email.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Emai KP"))
        item = self.table_email.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Name"))
        item = self.table_email.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "SSN"))
        item = self.table_email.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "DL"))
        item = self.table_email.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Address"))
        item = self.table_email.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "City"))
        item = self.table_email.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "State"))
        item = self.table_email.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Zip code"))
        item = self.table_email.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Phone"))
        item = self.table_email.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Birthday"))
        item = self.table_email.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "ACH Route"))
        item = self.table_email.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "BankAccount"))
        item = self.table_email.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "CardNumber"))
        item = self.table_email.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "Expired Date"))
        item = self.table_email.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "Card Code"))
        item = self.table_email.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "LoginSuccess"))
        item = self.table_email.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "RequestStatus"))
        item = self.table_email.horizontalHeaderItem(20)
        item.setText(_translate("MainWindow", "Verify Code"))
        item = self.table_email.horizontalHeaderItem(21)
        item.setText(_translate("MainWindow", "Status"))
        self.tab_easty_data.setTabText(self.tab_easty_data.indexOf(self.tab), _translate("MainWindow", "Easty"))
        item = self.table_mail_change.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Proxy"))
        item = self.table_mail_change.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Email"))
        item = self.table_mail_change.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Password"))
        item = self.table_mail_change.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Emai KP"))
        item = self.table_mail_change.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Password"))
        item = self.table_mail_change.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Mail KP"))
        item = self.table_mail_change.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Status"))
        self.tab_easty_data.setTabText(self.tab_easty_data.indexOf(self.tab_change_mail), _translate("MainWindow", "Change mail"))
        self.btn_stop.setText(_translate("MainWindow", "Stop"))
        self.btn_start.setText(_translate("MainWindow", "Start"))
        self.btn_verify_bank.setText(_translate("MainWindow", "Verify Bank"))
        self.btn_check_live.setText(_translate("MainWindow", "Check Live"))
        self.btn_load.setText(_translate("MainWindow", "Load"))
        self.label.setText(_translate("MainWindow", "Thành công:"))
        self.label_2.setText(_translate("MainWindow", "Thất bại:"))
        self.label_success.setText(_translate("MainWindow", "0"))
        self.label_error.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "Thực hiện:"))
        self.label_running_status.setText(_translate("MainWindow", "0"))
        self.view_btn_user_views.setText(_translate("MainWindow", "..."))
        self.delayLD_label_2.setText(_translate("MainWindow", "Quy trình:"))
        self.stepComboBox.setItemText(0, _translate("MainWindow", "Login"))
        self.stepComboBox.setItemText(1, _translate("MainWindow", "AddName"))
        self.stepComboBox.setItemText(2, _translate("MainWindow", "CreateShop"))
        self.stepComboBox.setItemText(3, _translate("MainWindow", "Full"))
        self.stepComboBox.setItemText(4, _translate("MainWindow", "Khang: Check Live"))
        self.stepComboBox.setItemText(5, _translate("MainWindow", "Khang: Request"))
        self.update_info_mail.setText(_translate("MainWindow", "Update info mail"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_easty), _translate("MainWindow", "Easty"))
        self.pass_random.setText(_translate("MainWindow", "Random"))
        self.pass_general.setText(_translate("MainWindow", "Chung"))
        self.pass_specific.setText(_translate("MainWindow", "Riêng"))
        self.label_8.setText(_translate("MainWindow", "Pass chung"))
        self.gmail_random.setText(_translate("MainWindow", "Random"))
        self.gmail_general.setText(_translate("MainWindow", "Chung"))
        self.gmail_specific.setText(_translate("MainWindow", "Riêng"))
        self.label_9.setText(_translate("MainWindow", "Mail Chung"))
        self.change_password.setText(_translate("MainWindow", "Đổi  Password"))
        self.change_mail_2.setText(_translate("MainWindow", "Đổi  Mail KP"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_gmail), _translate("MainWindow", "Gmail"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
