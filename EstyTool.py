from PyQt5 import QtCore, QtGui, QtWidgets
from ChangeGmailSelenium import ChangeGmailSelenium
from GmailSelenium import GmailSelenium
import os, time
from LoginSelenium import LoginSelenium
from VerrifyBankSelenium import VerifyBankSelenium
import threading
import random
import time
import string
class EstyTool(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1064, 885)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 0, 341, 171))
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
        self.hidden_chrome.setGeometry(QtCore.QRect(150, 60, 91, 20))
        self.hidden_chrome.setChecked(True)
        self.hidden_chrome.setObjectName("hidden_chrome")
        self.proxy_combobox = QtWidgets.QComboBox(self.groupBox_2)
        self.proxy_combobox.setGeometry(QtCore.QRect(50, 130, 81, 20))
        self.proxy_combobox.setObjectName("proxy_combobox")
        self.proxy_combobox.addItem("")
        self.proxy_combobox.addItem("")
        self.delayLD_label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.delayLD_label_3.setGeometry(QtCore.QRect(10, 130, 41, 20))
        self.delayLD_label_3.setObjectName("delayLD_label_3")
        self.input_proxy = QtWidgets.QLineEdit(self.groupBox_2)
        self.input_proxy.setGeometry(QtCore.QRect(140, 130, 191, 20))
        self.input_proxy.setObjectName("input_proxy")
        self.update_info_mail = QtWidgets.QCheckBox(self.groupBox_2)
        self.update_info_mail.setGeometry(QtCore.QRect(150, 90, 101, 20))
        self.update_info_mail.setChecked(True)
        self.update_info_mail.setObjectName("update_info_mail")
        self.tab_easty_data = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_easty_data.setGeometry(QtCore.QRect(10, 220, 1051, 621))
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
        self.btn_stop.setGeometry(QtCore.QRect(130, 180, 51, 31))
        self.btn_stop.setObjectName("btn_stop")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(70, 180, 51, 31))
        self.btn_start.setObjectName("btn_start")
        self.btn_verify_bank = QtWidgets.QPushButton(self.centralwidget)
        self.btn_verify_bank.setGeometry(QtCore.QRect(190, 180, 71, 31))
        self.btn_verify_bank.setObjectName("btn_verify_bank")
        self.btn_check_live = QtWidgets.QPushButton(self.centralwidget)
        self.btn_check_live.setGeometry(QtCore.QRect(270, 180, 71, 31))
        self.btn_check_live.setObjectName("btn_check_live")
        self.btn_load = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load.setGeometry(QtCore.QRect(10, 180, 51, 31))
        self.btn_load.setObjectName("btn_load")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(375, 190, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(490, 190, 51, 16))
        self.label_2.setObjectName("label_2")
        self.label_success = QtWidgets.QLabel(self.centralwidget)
        self.label_success.setGeometry(QtCore.QRect(440, 190, 51, 16))
        self.label_success.setObjectName("label_success")
        self.label_error = QtWidgets.QLabel(self.centralwidget)
        self.label_error.setGeometry(QtCore.QRect(538, 190, 51, 16))
        self.label_error.setObjectName("label_error")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(582, 190, 51, 16))
        self.label_5.setObjectName("label_5")
        self.label_running_status = QtWidgets.QLabel(self.centralwidget)
        self.label_running_status.setGeometry(QtCore.QRect(640, 190, 191, 16))
        self.label_running_status.setObjectName("label_running_status")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setEnabled(True)
        self.groupBox_3.setGeometry(QtCore.QRect(360, 0, 681, 171))
        self.groupBox_3.setInputMethodHints(QtCore.Qt.ImhNone)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_3)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 661, 151))
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1064, 21))
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
        self.proxy_combobox.setItemText(0, _translate("MainWindow", "Tinsoft"))
        self.proxy_combobox.setItemText(1, _translate("MainWindow", "ShopLike"))
        self.delayLD_label_3.setText(_translate("MainWindow", "Proxy:"))
        self.update_info_mail.setText(_translate("MainWindow", "Update info mail"))
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
        self.runningJob = False
        self.indexsuccess = 0
        self.indexerror = 0
        self.listthread = []
        self.listAccountRunning = []
        self.list_hostmail = []
        self.dataExcute = []
        self.runCount = 0
        self.index = 0
        self.lastIndex = 0   
        self.threadIndex = 0
        self.runType = 0
        self.run_option = 0
        self.row_selected = None
        self.list_selected = []
        self.row_index = None
        self.btn_load.clicked.connect(self.LoadHotMail)
        self.btn_LD_link.clicked.connect(self.FileDialogLD)
        self.btn_stop.clicked.connect(self.ActionStop)
        self.btn_start.clicked.connect(self.StartRegAction)
        self.btn_verify_bank.clicked.connect(self.VerifyBankAction)
        self.btn_check_live.clicked.connect(self.OpenEsty)
        self.table_email.cellClicked.connect(self.getClickedCell)        
        self.tabWidget.currentChanged.connect(self.changeOptionsTab)
        if os.path.exists("keyproxy.txt"): self.input_proxy.setText(open("keyproxy.txt").read())

    def changeOptionsTab(self, index):
        print(index)
        self.run_option = index

    def getClickedCell(self, row, column):
        if row < len(self.list_hostmail) and self.list_hostmail[row]:
            self.row_selected = self.list_hostmail[row]
            self.row_index = row
        if row < len(self.list_hostmail) and self.list_hostmail[row]:
            if self.list_hostmail[row] not in self.list_selected:
                self.list_selected.append(self.list_hostmail[row])
            else:
                self.list_selected.remove(self.list_hostmail[row])
            
    def closeEvent(self, event):
        sys.exit()
    
    def Mesagebox(self, title="Thông báo", text=""):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Warning)
        self.msg.setWindowTitle(title)
        self.msg.setText(text)
        self.msg.show()
                
    def LoadHotMail(self):
        try:
            self.index = 0
            self.runCount = 0
            self.indexsuccess = 0
            self.indexerror = 0
            self.runningJob = False
            self.index = 0
            self.runCount = 0
            self.indexsuccess = 0
            self.indexerror = 0
            self.listthread = []
            self.list_selected = []
            self.row_selected = None
            self.threadreg = None
            self.label_success.setText(f"<p><span style=\" color:#00aa00;\"> {self.indexsuccess} </span></p>")
            self.label_error.setText(f"<p><span style=\" color:#ff0000;\"> {self.indexerror} </span></p>")
            self.label_running_status.setText(f"<p><span style=\" color:#00aa00;\"> Chưa chạy </span></p>")
            
            if len(self.LD_link.text()) <= 1 or not os.path.exists(self.LD_link.text()):
                self.Mesagebox(text="Chọn file dữ liệu !")
            else:
                self.list_hostmail = []
                accountFile = open(self.LD_link.text(), 'r')
                if accountFile: 
                    data = accountFile.readlines()
                    data.pop(0)
                    if data and len(data) > 0:
                        for mail in data:
                            if mail and len(mail) > 50:
                                self.list_hostmail.append(str(mail).replace("\n", ""))
                        self.showAccounts()
        except Exception as e:
            print(e)
            self.Mesagebox(text="Load dữ liệu lỗi! Vui lòng kiểm tra lại.")

    def showAccounts(self):
        self.table_email.setRowCount(0)
        self.table_mail_change.setRowCount(0)
        i = 0
        for account in self.list_hostmail:
            mail = str(account).split("|")
            self.table_email.insertRow(i)
            self.ShowTable(i, 0, f"{mail[0]}:{mail[1]}:{mail[2]}:{mail[3]}")
            self.ShowTable(i, 1, mail[4])
            self.ShowTable(i, 2, mail[5])
            self.ShowTable(i, 3, mail[6])
            self.ShowTable(i, 4, f"{mail[7]} {mail[8]}")
            self.ShowTable(i, 5, mail[9])
            self.ShowTable(i, 6, mail[10])
            self.ShowTable(i, 7, mail[11])
            self.ShowTable(i, 8, mail[12])
            self.ShowTable(i, 9, mail[13])
            self.ShowTable(i, 10, mail[14])
            self.ShowTable(i, 11, mail[15])
            self.ShowTable(i, 12, mail[16])
            self.ShowTable(i, 13, mail[17])
            self.ShowTable(i, 14, mail[18])
            self.ShowTable(i, 15, mail[19])
            self.ShowTable(i, 16, f"{mail[20]}/{mail[21]}")
            self.ShowTable(i, 17, mail[22])
            try:
                self.ShowTable(i, 18, mail[23])
                self.ShowTable(i, 19, mail[24])
                self.ShowTable(i, 21, mail[25])
            except:pass

            #table mail change
            self.table_mail_change.insertRow(i)
            self.ShowTableMailChange(i, 0, f"{mail[0]}:{mail[1]}:{mail[2]}:{mail[3]}")
            self.ShowTableMailChange(i, 1, mail[4])
            self.ShowTableMailChange(i, 2, mail[5])
            self.ShowTableMailChange(i, 3, mail[6])
            i += 1                

    def FileDialogLD(self):
        self.filepath2 = QtWidgets.QFileDialog()
        self.filepath2.setFileMode(QtWidgets.QFileDialog.FileMode.AnyFile)
        self.filepath2.show()
        if self.filepath2.exec_() == QtWidgets.QDialog.Accepted: 
            folder = self.filepath2.selectedFiles()[0]
            self.LD_link.setText(folder)

    def LDViewer(self):
        from Viewer import Ui_LDPlayerViewer
        global LDPlayerViewer
        LDPlayerViewer = QtWidgets.QWidget()
        self.view = Ui_LDPlayerViewer()
        self.view.setupUi(LDPlayerViewer)
        LDPlayerViewer.show()
        
    def Delay(self, countdelay):
        loop = QtCore.QEventLoop()
        QtCore.QTimer.singleShot(int(countdelay*1000), loop.quit)
        loop.exec()

    def ShowTable(self, row, column, text):
        self.table_email.setItem(row, column, QtWidgets.QTableWidgetItem(text))

    def ShowTableMailChange(self, row, column, text):
        self.table_mail_change.setItem(row, column, QtWidgets.QTableWidgetItem(text))

    def ChangeTextSuccessAndError(self, check, row, status):
        print("status", status)
        if check == True:
            self.indexsuccess += 1
            self.label_success.setText(f"<p><span style=\" color:#00aa00;\"> {self.indexsuccess} </span></p>")
        else:
            self.indexerror += 1
            self.label_error.setText(f"<p><span style=\" color:#ff0000;\"> {self.indexerror} </span></p>")

        if self.run_option == 0: #run options easty
            if (self.index == len(self.list_hostmail) or (self.threadIndex == len(self.list_selected) and len(self.list_selected) > 0)) and self.runType == 1:
                self.runningJob = False
                self.label_running_status.setText(f"<p><span style=\" color:#00aa00;\"> Hoàn thành </span></p>")
                dataSave = list(self.retriveTableData())
                if os.path.exists(f'{self.LD_link.text().replace(".txt", "")}_finished.txt'):
                    os.remove(f'{self.LD_link.text().replace(".txt", "")}_finished.txt')
                open(f'{self.LD_link.text().replace(".txt", "")}_finished.txt', 'a+').write("%s\n"%("Proxy|proxy Port|proxy User|proxy Pass|Email|Passmail|email KP|Fname|Lname|ssn|dl|add|city|state|zipcode|phone|dob|ACH roughting number| Bank account number|card Number| Expriation month | Expriation day | CCV | LoginSuccess | Request Status | VerifyCode | Status"))
                index = 0
                for data in dataSave:
                    str = ""
                    for i in data:
                        if index == 0: #proxy
                            for proxy in i.split(":"):
                                if len(str) > 0:
                                    str += f"|{proxy}"
                                else: str += proxy
                        elif index == 4: # Name
                            str += f"|{i.split(' ')[0]} {i.split(' ')[1]}"
                            try:
                                str += f"|{i.split(' ')[2]} {i.split(' ')[3]}"
                            except:
                                str += f"|{i.split(' ')[2]}"
                        elif index == 16: # card date
                            str +=  f"|{i.split('/')[0]}"
                            str +=  f"|{i.split('/')[1]}"
                        else: 
                            if len(str) > 0:
                                str += f"|{i}"
                            else: str += i
                    open(f'{self.LD_link.text().replace(".txt", "")}_finished.txt', 'a+', encoding="utf-8").write("%s\n"%(str))

            if (self.index == len(self.dataExcute) or (self.threadIndex == len(self.list_selected) and len(self.list_selected) > 0)) and self.runType == 2:
                self.runningJob = False
                self.label_running_status.setText(f"<p><span style=\" color:#00aa00;\"> Hoàn thành </span></p>")
                dataSave = list(self.retriveTableData())
                if os.path.exists(fr'{self.LD_link.text().replace(".txt", "")}_finished.txt'):
                    os.remove(fr'{self.LD_link.text().replace(".txt", "")}_finished.txt')
                open(f'{self.LD_link.text().replace(".txt", "")}_finished.txt', 'a+').write("%s\n"%("Proxy|proxy Port|proxy User|proxy Pass|Email|Passmail|email KP|Fname|Lname|ssn|dl|add|city|state|zipcode|phone|dob|ACH roughting number| Bank account number|card Number| Expriation month | Expriation day | CCV | LoginSuccess | Request Status | VerifyCode | Status"))
                for data in dataSave:
                    str = ""
                    for i in data:
                        if index == 0: #proxy
                            for proxy in i.split(":"):
                                if len(str) > 0:
                                    str += f"|{proxy}"
                                else: str += proxy
                        elif index == 4: # Name
                            str += f"|{i.split(' ')[0]} {i.split(' ')[1]}"
                            try:
                                str += f"|{i.split(' ')[2]} {i.split(' ')[3]}"
                            except:
                                str += f"|{i.split(' ')[2]}"
                        elif index == 16: # card date
                            str +=  f"|{i.split('/')[0]}"
                            str +=  f"|{i.split('/')[1]}"
                        else: 
                            if len(str) > 0:
                                str += f"|{i}"
                            else: str += i
                    open(f'{self.LD_link.text().replace(".txt", "")}_finished.txt', 'a+').write("%s\n"%(str))
        else: #handle for mail
            if (self.index == len(self.list_hostmail) or (self.threadIndex == len(self.list_selected) and len(self.list_selected) > 0)):
                self.runningJob = False
                self.label_running_status.setText(f"<p><span style=\" color:#00aa00;\"> Hoàn thành </span></p>")
                dataGmail = list(self.retriveTableDataGmail())
                dataSave = list(self.retriveTableData())
                if os.path.exists(fr'{self.LD_link.text().replace(".txt", "")}_changemail_finished.txt'):
                    os.remove(fr'{self.LD_link.text().replace(".txt", "")}_changemail_finished.txt')
                open(f'{self.LD_link.text().replace(".txt", "")}_changemail_finished.txt', 'a+').write("%s\n"%("Proxy|proxy Port|proxy User|proxy Pass|Email|Passmail|email KP|Fname|Lname|ssn|dl|add|city|state|zipcode|phone|dob|ACH roughting number| Bank account number|card Number| Expriation month | Expriation day | CCV | LoginSuccess | Request Status | VerifyCode | Status"))
                rowIndex = 0
                for data in dataSave:
                    str = ""
                    index = 0
                    for i in data:
                        if index == 0: #proxy
                            for proxy in i.split(":"):
                                if len(str) > 0:
                                    str += f"|{proxy}"
                                else: str += proxy
                        elif index == 4: # Name
                            str += f"|{i.split(' ')[0]} {i.split(' ')[1]}"
                            try:
                                str += f"|{i.split(' ')[2]} {i.split(' ')[3]}"
                            except:
                                str += f"|{i.split(' ')[2]}"
                        elif index == 16: # card date
                            str +=  f"|{i.split('/')[0]}"
                            str +=  f"|{i.split('/')[1]}"
                        else: 
                            if len(str) > 0:
                                if index == 2 and check == True:
                                    if status.split("|")[0] == 'True': #password success
                                        if self.change_password.isChecked():
                                            if self.pass_general.isChecked():
                                                #pass chung
                                                str += f"|{self.input_pass_general.text()}"
                                            if self.pass_random.isChecked() or self.pass_specific.isChecked():
                                                str += f"|{dataGmail[rowIndex][4]}"
                                    else:
                                        str += f"|{i}"
                                elif index == 3 and check == True:                    
                                    if status.split("|")[1] == 'True': #mail success
                                        if self.change_mail_2.isChecked():
                                            if self.gmail_general.isChecked():
                                                #mail chung
                                                str += f"|{self.input_gmail_general.text()}"
                                            if self.gmail_random.isChecked() or self.gmail_specific.isChecked():
                                                str += f"|{dataGmail[rowIndex][5]}"
                                    else:
                                        str += f"|{i}"
                                else:
                                    str += f"|{i}"
                            else: str += i
                        index += 1
                    rowIndex += 1
                    open(f'{self.LD_link.text().replace(".txt", "")}_changemail_finished.txt', 'a+').write("%s\n"%(str))
                self.LoadHotMail()

        self.runCount -= 1
        if self.runType == 1:
            self.StartReg()
        if self.runType == 2:
            self.VerifyBank()

    def retriveTableData(self):
        model = self.table_email.model()
        data = []
        for row in range(model.rowCount()):
            data.append([])
            for column in range(model.columnCount()):
                index = model.index(row, column)
                # We suppose data are strings
                data[row].append(str(model.data(index)))
        return data

    def retriveTableDataGmail(self):
        model = self.table_mail_change.model()
        data = []
        for row in range(model.rowCount()):
            data.append([])
            for column in range(model.columnCount()):
                index = model.index(row, column)
                # We suppose data are strings
                data[row].append(str(model.data(index)))
        return data
      
    def OpenEsty(self):
        self.threadRun = None
        if self.row_selected is None:
            self.Mesagebox(text="Vui lòng chọn tài khoản !")
            return
        self.threadRun = StartQ(self, self.row_index, self.row_selected, "Login", False, False)
        self.threadRun.start()
        self.threadRun.show.connect(self.ShowTable)
        self.threadRun.checksuccess.connect(self.ChangeTextSuccessAndError)

    def OpenEsty2(self):
        if self.row_selected is None:
            self.Mesagebox(text="Vui lòng chọn tài khoản !")
            return
        thread = threading.Thread(target=self.LoginEsty)
        thread.start()

    def LoginEsty(self):
        login = LoginSelenium(self, self.row_selected)
        login.run()

    def ActionStop(self):
        self.runningJob = False
    
    def VerifyBankAction(self):
        if self.runningJob == False:
            tableData = self.retriveTableData()
            self.dataExcute = list(filter(lambda x: x[18] is not None and x[18] != 'None', tableData))
            if len(self.dataExcute)  == 0:
                self.Mesagebox(text="Không có mã code để thực hiện verify vui lòng cập nhật !")
                return
            self.runType = 2
            self.index = 0
            self.runCount = 0
            self.threadIndex = 0
            self.indexsuccess = 0
            self.indexerror = 0
            self.lastIndex = 0             
            self.listthread = []
            self.threadreg = None
            self.label_running_status.setText(f"<p><span style=\" color:#ff0000;\"> Đang chạy... </span></p>")
            self.runningJob = True
            self.VerifyBank()

    def StartRegAction(self):
        if self.runningJob == False:
            self.runType = 1
            self.index = 0
            self.indexsuccess = 0
            self.indexerror = 0
            self.runCount = 0
            self.lastIndex = 0
            self.listthread = []
            self.threadIndex = 0
            self.threadreg = None
            self.label_running_status.setText(f"<p><span style=\" color:#ff0000;\"> Đang chạy... </span></p>")
            self.runningJob = True
            self.StartReg()

    def randomword(self, length):
        letters = string.ascii_lowercase
        return str(''.join(random.choice(letters) for i in range(length))).upper()

    def StartReg(self):
        if self.run_option == 0: # run easty
            if self.list_selected is None or len(self.list_selected) == 0:
                if len(self.list_hostmail) > self.index:
                    for vm in self.list_hostmail:
                        if self.runningJob == True and self.runCount < int(self.threadCount.text()) and len(self.list_hostmail) > self.index:
                            data = self.list_hostmail[self.index]
                            self.threadreg = StartQ(self, self.index, data, self.stepComboBox.currentText(), self.hidden_chrome.isChecked(), self.update_info_mail.isChecked())
                            self.threadreg.start()
                            self.threadreg.show.connect(self.ShowTable)
                            self.threadreg.checksuccess.connect(self.ChangeTextSuccessAndError)
                            self.listthread.append(self.threadreg)
                            self.runCount += 1
                            self.Delay(1)
                            self.index += 1
                            print('self', self.index, self.runCount)
            else:
                if len(self.list_selected) > self.threadIndex:
                    index = 0
                    for vm in self.list_hostmail:
                        index += 1
                        item = next((x for x in self.list_selected if str(vm).split("|")[4] in x), None)
                        if self.runCount < int(self.threadCount.text()) and index > self.threadIndex and item is not None and index > self.lastIndex:
                            self.lastIndex = index
                            data = self.list_hostmail[index - 1]
                            self.threadreg = StartQ(self, index - 1, data, self.stepComboBox.currentText(), self.hidden_chrome.isChecked(), self.update_info_mail.isChecked())
                            self.threadreg.show.connect(self.ShowTable)
                            self.threadreg.checksuccess.connect(self.ChangeTextSuccessAndError)
                            self.listthread.append(self.threadreg)
                            self.threadreg.start()
                            self.runCount += 1
                            self.threadIndex += 1
                            print('self', index, self.runCount)
                            self.Delay(self.delayLD_input.value())
        else: #run change mail
            if self.list_selected is None or len(self.list_selected) == 0:
                if len(self.list_hostmail) > self.index:
                    for vm in self.list_hostmail:
                        if self.runningJob == True and self.runCount < int(self.threadCount.text()) and len(self.list_hostmail) > self.index:
                            data = self.list_hostmail[self.index]
                            changePasswordType = "Random" if self.pass_random.isChecked() else "General" if self.pass_general.isChecked() else "Specific"
                            changeMailType = "Random" if self.gmail_random.isChecked() else "General" if self.gmail_general.isChecked() else "Specific"
                            passwordUpdate = None
                            if changePasswordType == "Specific":
                                tableData = self.retriveTableDataGmail()
                                passwordUpdate = tableData[self.index][4]
                            elif changePasswordType == "General":
                                passwordUpdate = self.input_pass_general.text()
                            else:
                                passwordUpdate = self.randomword(10)
                            self.ShowTableMailChange(self.index, 4, passwordUpdate)
                            mailUpdate = None
                            if changeMailType == "Specific":
                                tableData = self.retriveTableDataGmail()
                                mailUpdate = tableData[self.index][5]
                            elif changeMailType == "General":
                                mailUpdate = self.input_gmail_general.text()
                            else:
                                mailUpdate = self.input_gmail_general.text()
                            self.ShowTableMailChange(self.index, 5, mailUpdate)
                            self.threadreg = StartQChangeMail(self, self.index, self.proxy_combobox.currentText(), 
                                                              self.input_proxy.text(), data,
                                                              self.stepComboBox.currentText(), self.hidden_chrome.isChecked(), self.update_info_mail.isChecked(),
                                                              self.change_password.isChecked(), changePasswordType, passwordUpdate,
                                                              self.change_mail_2.isChecked(), changeMailType, mailUpdate)
                            self.threadreg.start()
                            self.threadreg.show.connect(self.ShowTableMailChange)
                            self.threadreg.checksuccess.connect(self.ChangeTextSuccessAndError)
                            self.listthread.append(self.threadreg)
                            self.runCount += 1
                            self.Delay(1)
                            self.index += 1
                            print('self', self.index, self.runCount)
            else:
                if len(self.list_selected) > self.threadIndex:
                    index = 0
                    for vm in self.list_hostmail:
                        index += 1
                        item = next((x for x in self.list_selected if str(vm).split("|")[4] in x), None)
                        if self.runCount < int(self.threadCount.text()) and index > self.threadIndex and item is not None and index > self.lastIndex:
                            self.lastIndex = index
                            data = self.list_hostmail[index - 1]
                            changePasswordType = "Random" if self.pass_random.isChecked() else "General" if self.pass_general.isChecked() else "Specific"
                            changeMailType = "Random" if self.gmail_random.isChecked() else "General" if self.gmail_general.isChecked() else "Specific"
                            passwordUpdate = None
                            if changePasswordType == "Specific":
                                tableData = self.retriveTableDataGmail()
                                passwordUpdate = tableData[self.index - 1][4]
                            elif changePasswordType == "General":
                                passwordUpdate = self.input_pass_general.text()
                            else:
                                passwordUpdate = self.randomword(8, 15)
                            self.ShowTableMailChange(self.index - 1, 4, passwordUpdate)
                            mailUpdate = None
                            if changeMailType == "Specific":
                                tableData = self.retriveTableDataGmail()
                                mailUpdate = tableData[self.index - 1][5]
                            elif changeMailType == "General":
                                mailUpdate = self.input_gmail_general.text()
                            else:
                                mailUpdate = self.input_gmail_general.text()
                            self.ShowTableMailChange(self.index - 1, 5, mailUpdate)
                            self.threadreg = StartQChangeMail(self, index - 1, self.proxy_combobox.currentText(), 
                                                              self.input_proxy.text(), data, self.stepComboBox.currentText(), self.hidden_chrome.isChecked(), self.update_info_mail.isChecked(),
                                                              self.change_password.isChecked(), changePasswordType, passwordUpdate,
                                                              self.change_mail_2.isChecked(), changeMailType, mailUpdate)
                            self.threadreg.show.connect(self.ShowTableMailChange)
                            self.threadreg.checksuccess.connect(self.ChangeTextSuccessAndError)
                            self.listthread.append(self.threadreg)
                            self.threadreg.start()
                            self.runCount += 1
                            self.threadIndex += 1
                            print('self', index, self.runCount)
                            self.Delay(self.delayLD_input.value())

    def VerifyBank(self):
        if len(self.list_hostmail) > self.index:
            for vm in self.list_hostmail:
                #find item
                self.index += 1
                item = next((x for x in self.dataExcute if x[1] == str(vm).split("|")[4]), None)
                if self.runningJob == True and self.runCount < int(self.threadCount.text()) and len(self.list_hostmail) > self.index - 1 and item is not None:
                    data = self.list_hostmail[self.index - 1]
                    self.threadreg = StartQVerify(self, self.index - 1, data, self.hidden_chrome.isChecked(), item[18])
                    self.threadreg.start()
                    self.threadreg.show.connect(self.ShowTable)
                    self.threadreg.checksuccess.connect(self.ChangeTextSuccessAndError)
                    self.runCount += 1
                    self.Delay(self.delayLD_input.value())
                    print('self', self.index - 1, self.runCount)  


class StartQ(QtCore.QThread):
    delete = QtCore.pyqtSignal()
    show = QtCore.pyqtSignal(int, int, str)
    checkRegisterSuccess = QtCore.pyqtSignal(int, int, str)
    checksuccess = QtCore.pyqtSignal(bool, int, str)
    def __init__(self, ref, index, data, runType, hiddenBrowser, changeInfoMail) -> None:
        super().__init__()
        self.ref = ref
        self.index = index
        self.data = data
        self.runType = runType
        self.hiddenBrowser = hiddenBrowser
        self.changeInfoMail = changeInfoMail

    def run(self):
        self.reg = GmailSelenium(self.index, self.data, self.runType, self.hiddenBrowser, self.changeInfoMail)
        self.reg.ref = self
        self.reg.run()
        time.sleep(0.1)

class StartQChangeMail(QtCore.QThread):
    delete = QtCore.pyqtSignal()
    show = QtCore.pyqtSignal(int, int, str)
    checkRegisterSuccess = QtCore.pyqtSignal(int, int, str)
    checksuccess = QtCore.pyqtSignal(bool, int, str)
    def __init__(self, ref, index, proxyType, proxyKey, data, runType, hiddenBrowser, changeInfoMail, changePassword, changePasswordType, password, changeMail, changeMailType, mailKP) -> None:
        super().__init__()
        self.ref = ref
        self.proxyType = proxyType
        self.proxyKey = proxyKey
        self.index = index
        self.data = data
        self.runType = runType
        self.hiddenBrowser = hiddenBrowser
        self.changeInfoMail = changeInfoMail
        self.changePassword = changePassword
        self.changePasswordType = changePasswordType
        self.password = password
        self.changeMail = changeMail
        self.changeMailType = changeMailType
        self.mailKP = mailKP

    def run(self):
        self.reg = ChangeGmailSelenium(self.index, self.proxyType, self.proxyKey, self.data, self.runType, self.hiddenBrowser, 
            self.changeInfoMail, self.changePassword, self.changePasswordType, self.password, self.changeMail, self.changeMailType, self.mailKP)
        self.reg.ref = self
        self.reg.run()
        time.sleep(0.1)

class StartQVerify(QtCore.QThread):
    delete = QtCore.pyqtSignal()
    show = QtCore.pyqtSignal(int, int, str)
    checkRegisterSuccess = QtCore.pyqtSignal(int, int, str)
    checksuccess = QtCore.pyqtSignal(bool, int, str)
    def __init__(self, ref, index, data, hiddenBrowser, code) -> None:
        super().__init__()
        self.ref = ref
        self.index = index
        self.data = data
        self.hiddenBrowser = hiddenBrowser
        self.code = code

    def run(self):
        self.reg = VerifyBankSelenium(self.index, self.data, self.hiddenBrowser, self.code)
        self.reg.ref = self
        self.reg.run()
        time.sleep(0.1)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    RegTikTok = QtWidgets.QMainWindow()
    RegTikTok.setWindowIcon(QtGui.QIcon('icon.ico'))
    ui = EstyTool()
    ui.setupUi(RegTikTok)
    RegTikTok.show()
    sys.exit(app.exec_())
# 7h15