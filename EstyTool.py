from PyQt5 import QtCore, QtGui, QtWidgets
from GmailSelenium import GmailSelenium
import os, time, subprocess
import pathlib, random
from LoginSelenium import LoginSelenium
from VerrifyBankSelenium import VerifyBankSelenium
class EstyTool(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1069, 796)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 1041, 71))
        self.groupBox_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(290, 20, 51, 20))
        self.label_15.setObjectName("label_15")
        self.threadCount = QtWidgets.QSpinBox(self.groupBox_2)
        self.threadCount.setGeometry(QtCore.QRect(340, 20, 42, 20))
        self.threadCount.setProperty("value", 2)
        self.threadCount.setObjectName("threadCount")
        self.LD_link = QtWidgets.QLineEdit(self.groupBox_2)
        self.LD_link.setGeometry(QtCore.QRect(58, 20, 161, 20))
        self.LD_link.setObjectName("LD_link")
        self.btn_LD_link = QtWidgets.QToolButton(self.groupBox_2)
        self.btn_LD_link.setGeometry(QtCore.QRect(230, 20, 31, 21))
        self.btn_LD_link.setObjectName("btn_LD_link")
        self.thread_label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.thread_label_2.setGeometry(QtCore.QRect(25, 20, 31, 20))
        self.thread_label_2.setObjectName("thread_label_2")
        self.delayLD_input = QtWidgets.QSpinBox(self.groupBox_2)
        self.delayLD_input.setGeometry(QtCore.QRect(460, 20, 42, 20))
        self.delayLD_input.setProperty("value", 1)
        self.delayLD_input.setObjectName("delayLD_input")
        self.delayLD_label = QtWidgets.QLabel(self.groupBox_2)
        self.delayLD_label.setGeometry(QtCore.QRect(410, 20, 47, 20))
        self.delayLD_label.setObjectName("delayLD_label")
        self.hidden_chrome = QtWidgets.QCheckBox(self.groupBox_2)
        self.hidden_chrome.setGeometry(QtCore.QRect(540, 20, 151, 20))
        self.hidden_chrome.setChecked(True)
        self.hidden_chrome.setObjectName("hidden_chrome")
        self.update_info_mail = QtWidgets.QCheckBox(self.groupBox_2)
        self.update_info_mail.setGeometry(QtCore.QRect(660, 20, 151, 20))
        self.update_info_mail.setChecked(True)
        self.update_info_mail.setObjectName("update_info_mail")
        self.tab_data = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_data.setGeometry(QtCore.QRect(10, 130, 1051, 621))
        self.tab_data.setObjectName("tab_data")
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
        self.table_email.setColumnCount(20)
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
        self.table_email.horizontalHeader().setDefaultSectionSize(170)
        self.table_email.verticalHeader().setStretchLastSection(True)
        self.tab_data.addTab(self.tab, "")
        self.btn_stop = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stop.setGeometry(QtCore.QRect(130, 90, 51, 31))
        self.btn_stop.setObjectName("btn_stop")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(70, 90, 51, 31))
        self.btn_start.setObjectName("btn_start")
        self.btn_verify_bank = QtWidgets.QPushButton(self.centralwidget)
        self.btn_verify_bank.setGeometry(QtCore.QRect(190, 90, 71, 31))
        self.btn_verify_bank.setObjectName("btn_verify_bank")
        self.btn_check_live = QtWidgets.QPushButton(self.centralwidget)
        self.btn_check_live.setGeometry(QtCore.QRect(270, 90, 71, 31))
        self.btn_check_live.setObjectName("btn_check_live")
        self.btn_load = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load.setGeometry(QtCore.QRect(10, 90, 51, 31))
        self.btn_load.setObjectName("btn_load")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(375, 100, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(490, 100, 51, 16))
        self.label_2.setObjectName("label_2")
        self.label_success = QtWidgets.QLabel(self.centralwidget)
        self.label_success.setGeometry(QtCore.QRect(440, 100, 51, 16))
        self.label_success.setObjectName("label_success")
        self.label_error = QtWidgets.QLabel(self.centralwidget)
        self.label_error.setGeometry(QtCore.QRect(538, 100, 51, 16))
        self.label_error.setObjectName("label_error")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(582, 100, 51, 16))
        self.label_5.setObjectName("label_5")
        self.label_running_status = QtWidgets.QLabel(self.centralwidget)
        self.label_running_status.setGeometry(QtCore.QRect(640, 100, 191, 16))
        self.label_running_status.setObjectName("label_running_status")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1069, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab_data.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_15.setText(_translate("MainWindow", "Số luồng"))
        self.LD_link.setText(_translate("MainWindow", "D:\\anyfolder"))
        self.btn_LD_link.setText(_translate("MainWindow", "..."))
        self.thread_label_2.setText(_translate("MainWindow", "Path:"))
        self.delayLD_label.setText(_translate("MainWindow", "Delay:"))
        self.hidden_chrome.setText(_translate("MainWindow", "Ẩn trình duyệt"))
        self.update_info_mail.setText(_translate("MainWindow", "Update info mail"))
        item = self.table_email.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Proxy"))
        item = self.table_email.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Email"))
        item = self.table_email.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Password"))
        item = self.table_email.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Name"))
        item = self.table_email.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "SSN"))
        item = self.table_email.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "DL"))
        item = self.table_email.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Address"))
        item = self.table_email.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "City"))
        item = self.table_email.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "State"))
        item = self.table_email.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Zip code"))
        item = self.table_email.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Phone"))
        item = self.table_email.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Birthday"))
        item = self.table_email.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "ACH Route"))
        item = self.table_email.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "BankAccount"))
        item = self.table_email.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "CardNumber"))
        item = self.table_email.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "Expired Date"))
        item = self.table_email.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "Card Code"))
        item = self.table_email.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "Created Date"))
        item = self.table_email.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "Verify Code"))
        item = self.table_email.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "Status"))
        self.tab_data.setTabText(self.tab_data.indexOf(self.tab), _translate("MainWindow", "Mail tab"))
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
        self.runningJob = False
        self.indexsuccess = 0
        self.indexerror = 0
        self.listthread = []
        self.listAccountRunning = []
        self.list_hostmail = []
        self.dataExcute = []
        self.runCount = 0
        self.index = 0
        self.runType = 0
        self.row_selected = None
        self.btn_load.clicked.connect(self.LoadHotMail)
        self.btn_LD_link.clicked.connect(self.FileDialogLD)
        self.btn_stop.clicked.connect(self.ActionStop)
        self.btn_start.clicked.connect(self.StartRegAction)
        self.btn_verify_bank.clicked.connect(self.VerifyBankAction)
        self.btn_check_live.clicked.connect(self.OpenEsty)
        self.table_email.cellClicked.connect(self.getClickedCell)

    def getClickedCell(self, row, column):
        if row < len(self.list_hostmail) and self.list_hostmail[row]:
            self.row_selected = self.list_hostmail[row]
            
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
        i = 0
        for account in self.list_hostmail:
            mail = str(account).split("|")
            self.table_email.insertRow(i)
            self.ShowTable(i, 0, f"{mail[0]}:{mail[1]}:{mail[2]}:{mail[3]}")
            self.ShowTable(i, 1, mail[4])
            self.ShowTable(i, 2, mail[5])
            self.ShowTable(i, 3, f"{mail[6]} {mail[7]}")
            self.ShowTable(i, 4, mail[8])
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
            self.ShowTable(i, 15, f"{mail[19]}/{mail[20]}")
            self.ShowTable(i, 16, mail[21])
            try:
                self.ShowTable(i, 17, mail[22])
                self.ShowTable(i, 19, mail[23])
            except:pass
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
        
    def ChangeTextSuccessAndError(self, check, row, status):
        time.sleep(3)
        if check == True:
            self.indexsuccess += 1
            self.label_success.setText(f"<p><span style=\" color:#00aa00;\"> {self.indexsuccess} </span></p>")
        else:
            self.indexerror += 1
            self.label_error.setText(f"<p><span style=\" color:#ff0000;\"> {self.indexerror} </span></p>")
        self.runCount -= 1
        if self.runType == 1:self.StartReg()
        if self.runType == 2:self.VerifyBank()

        if self.index == len(self.list_hostmail) and self.runType == 1:
            self.runningJob = False
            self.label_running_status.setText(f"<p><span style=\" color:#00aa00;\"> Hoàn thành </span></p>")
            dataSave = list(self.retriveTableData())
            if os.path.exists(f'{self.LD_link.text().replace(".txt", "")}_finished.txt'):
                os.remove(f'{self.LD_link.text().replace(".txt", "")}_finished.txt')
            for data in dataSave:
                str = ""
                for i in data:
                    if len(str) > 0:str += f"|{i}"
                    else: str += i
                open(f'{self.LD_link.text().replace(".txt", "")}_finished.txt', 'a+', encoding="utf-8").write("%s\n"%(str))

        if self.index == len(self.dataExcute) and self.runType == 2:
            self.runningJob = False
            self.label_running_status.setText(f"<p><span style=\" color:#00aa00;\"> Hoàn thành </span></p>")
            dataSave = list(self.retriveTableData())
            if os.path.exists(fr'{self.LD_link.text().replace(".txt", "")}_finished.txt'):
                os.remove(fr'{self.LD_link.text().replace(".txt", "")}_finished.txt')
            for data in dataSave:
                str = ""
                for i in data:
                    if len(str) > 0:str += f"|{i}"
                    else: str += i
                open(f'{self.LD_link.text().replace(".txt", "")}_finished.txt', 'a+').write("%s\n"%(str))

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
    
    def OpenEsty(self):
        if self.row_selected is None:
            self.Mesagebox(text="Vui lòng chọn tài khoản !")
            return
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
            self.indexsuccess = 0
            self.indexerror = 0
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
            self.label_running_status.setText(f"<p><span style=\" color:#ff0000;\"> Đang chạy... </span></p>")
            self.runningJob = True
            self.StartReg()

    def StartReg(self):
        if len(self.list_hostmail) > self.index:
            for vm in self.list_hostmail:
                if self.runningJob == True and self.runCount < int(self.threadCount.text()) and len(self.list_hostmail) > self.index:
                    data = self.list_hostmail[self.index]
                    self.threadreg = StartQ(self, self.index, data, self.hidden_chrome.isChecked(), self.update_info_mail.isChecked())
                    self.threadreg.start()
                    self.threadreg.show.connect(self.ShowTable)
                    self.threadreg.checksuccess.connect(self.ChangeTextSuccessAndError)
                    self.listthread.append(self.threadreg)
                    self.index += 1
                    self.runCount += 1
                    time.sleep(1)
                    print('self', self.index, self.runCount)


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
                    time.sleep(1)
                    print('self', self.index - 1, self.runCount)  


class StartQ(QtCore.QThread):
    delete = QtCore.pyqtSignal()
    show = QtCore.pyqtSignal(int, int, str)
    checkRegisterSuccess = QtCore.pyqtSignal(int, int, str)
    checksuccess = QtCore.pyqtSignal(bool, int, str)
    def __init__(self, ref, index, data, hiddenBrowser, changeInfoMail) -> None:
        super().__init__()
        self.ref = ref
        self.index = index
        self.data = data
        self.hiddenBrowser = hiddenBrowser
        self.changeInfoMail = changeInfoMail

    def run(self):
        self.reg = GmailSelenium(self.index, self.data, self.hiddenBrowser, self.changeInfoMail)
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