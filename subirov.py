import time
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2
import serial
from PyQt5 import QtCore, QtGui, QtWidgets
class MainWindow(QWidget):

    def __init__(self):
        self.a = 0
        super(MainWindow, self).__init__()
        self.setWindowIcon(QtGui.QIcon('Koala.jpg'))
        self.timer = QTimer(self)
        self.timer.setSingleShot(False)
        self.timer.setInterval(10) # in milliseconds, so 5000 = 5 seconds
        self.timer.timeout.connect(self.loop)
        self.timer.start()
        self.resize(1000, 700)
        self.VBL = QVBoxLayout()

        self.FeedLabel = QLabel()
        self.VBL.addWidget(self.FeedLabel)

        self.CancelBTN = QPushButton("Kapat")
        self.CancelBTN.clicked.connect(self.CancelFeed)
        self.VBL.addWidget(self.CancelBTN)

        self.Worker1 = Worker1()

        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.setLayout(self.VBL)
        self.arac_port_secim_label = QtWidgets.QLabel(self)
        self.arac_port_secim_label.setGeometry(QtCore.QRect(815, 50, 31, 20))
        self.arac_port_secim_label.setObjectName("port_secim_label")
        self.arac_Baudrate_label = QtWidgets.QLabel(self)
        self.arac_Baudrate_label.setGeometry(QtCore.QRect(815, 80, 101, 20))
        self.arac_Baudrate_label.setObjectName("Baudrate_label")
        self.arac_port_secim_ComboBox = QtWidgets.QComboBox(self)
        self.arac_port_secim_ComboBox.setGeometry(QtCore.QRect(875, 80, 69, 22))
        self.arac_port_secim_ComboBox.setObjectName("port_secim_ComboBox")
        self.arac_port_secim_ComboBox.addItem("")
        self.arac_port_secim_ComboBox.addItem("")
        self.arac_port_secim_ComboBox.addItem("")
        self.arac_port_secim_ComboBox.addItem("")
        self.arac_port_secim_ComboBox.addItem("")
        self.arac_port_secim_ComboBox.addItem("")
        self.arac_port_secim_ComboBox.addItem("")
        self.arac_port_secim_ComboBox.addItem("")
        self.arac_port_secim_ComboBox.addItem("")
        self.arac_Baudrate_ComboBox = QtWidgets.QComboBox(self)
        self.arac_Baudrate_ComboBox.setGeometry(QtCore.QRect(875, 50, 69, 22))
        self.arac_Baudrate_ComboBox.setObjectName("Baudrate_ComboBox")
        self.arac_Baudrate_ComboBox.addItem("")
        self.arac_Baudrate_ComboBox.addItem("")
        self.arac_Baudrate_ComboBox.addItem("")
        self.arac_Baudrate_ComboBox.addItem("")
        self.arac_Baudrate_ComboBox.addItem("")
        self.arac_Baudrate_ComboBox.addItem("")
        self.arac_Baudrate_ComboBox.addItem("")
        self.arac_Baudrate_ComboBox.addItem("")
        self.arac_Baudrate_ComboBox.addItem("")
        self.arac_Baudrate_ComboBox.addItem("")
        self.arac_Baudrate_ComboBox.addItem("")
        self.arac_Baudrate_ComboBox.addItem("")
        self.arac_Baudrate_ComboBox.addItem("")
        self.arac_Baudrate_ComboBox.addItem("")
        self.arac_Baudrate_ComboBox.addItem("")
        self.arac_baglan_buton = QtWidgets.QPushButton(self)
        self.arac_baglan_buton.setGeometry(QtCore.QRect(875, 120, 75, 23))
        self.arac_baglan_buton.setObjectName("arac_baglan_buton")
        self.arac_baglan_buton.clicked.connect(self.arac_baglan)


        self.kumanda_port_secim_label = QtWidgets.QLabel(self) 
        self.kumanda_port_secim_label.setGeometry(QtCore.QRect(615, 50, 31, 20))
        self.kumanda_port_secim_label.setObjectName("port_secim_label")
        self.kumanda_Baudrate_label = QtWidgets.QLabel(self)
        self.kumanda_Baudrate_label.setGeometry(QtCore.QRect(615, 80, 101, 20))
        self.kumanda_Baudrate_label.setObjectName("Baudrate_label")
        self.kumanda_port_secim_ComboBox = QtWidgets.QComboBox(self)
        self.kumanda_port_secim_ComboBox.setGeometry(QtCore.QRect(675, 80, 69, 22))
        self.kumanda_port_secim_ComboBox.setObjectName("port_secim_ComboBox")
        self.kumanda_port_secim_ComboBox.addItem("")
        self.kumanda_port_secim_ComboBox.addItem("")
        self.kumanda_port_secim_ComboBox.addItem("")
        self.kumanda_port_secim_ComboBox.addItem("")
        self.kumanda_port_secim_ComboBox.addItem("")
        self.kumanda_port_secim_ComboBox.addItem("")
        self.kumanda_port_secim_ComboBox.addItem("")
        self.kumanda_port_secim_ComboBox.addItem("")
        self.kumanda_port_secim_ComboBox.addItem("")
        self.kumanda_Baudrate_ComboBox = QtWidgets.QComboBox(self)
        self.kumanda_Baudrate_ComboBox.setGeometry(QtCore.QRect(675, 50, 69, 22))
        self.kumanda_Baudrate_ComboBox.setObjectName("Baudrate_ComboBox")
        self.kumanda_Baudrate_ComboBox.addItem("")
        self.kumanda_Baudrate_ComboBox.addItem("")
        self.kumanda_Baudrate_ComboBox.addItem("")
        self.kumanda_Baudrate_ComboBox.addItem("")
        self.kumanda_Baudrate_ComboBox.addItem("")
        self.kumanda_Baudrate_ComboBox.addItem("")
        self.kumanda_Baudrate_ComboBox.addItem("")
        self.kumanda_Baudrate_ComboBox.addItem("")
        self.kumanda_Baudrate_ComboBox.addItem("")
        self.kumanda_Baudrate_ComboBox.addItem("")
        self.kumanda_Baudrate_ComboBox.addItem("")
        self.kumanda_Baudrate_ComboBox.addItem("")
        self.kumanda_Baudrate_ComboBox.addItem("")
        self.kumanda_Baudrate_ComboBox.addItem("")
        self.kumanda_Baudrate_ComboBox.addItem("")
        self.kumanda_baglan_buton = QtWidgets.QPushButton(self)
        self.kumanda_baglan_buton.setGeometry(QtCore.QRect(675, 120, 75, 23))
        self.kumanda_baglan_buton.setObjectName("kumanda_baglan_buton")
        self.kumanda_baglan_buton.clicked.connect(self.kumanda_baglan)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(749, 230, 251, 251))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("pashala logo tasarım 1 (5).png"))
        self.arac_baglan_label = QtWidgets.QLabel(self)
        self.arac_baglan_label.setGeometry(QtCore.QRect(875, 140, 91, 20))
        self.arac_baglan_label.setObjectName("arac_baglan_label")
        self.arac_baglan_label.setText("Araç Bağlantısı...")
        self.arac_baglan_label2 = QtWidgets.QLabel(self)
        self.arac_baglan_label2.setGeometry(QtCore.QRect(875, 140, 91, 20))
        self.arac_baglan_label2.setObjectName("arac_baglan_label2")
        self.arac_baglan_label2.setText("Bağlantı Başarılı")
        self.arac_baglan_label2.setHidden(True)
        self.arac_baglan_label3 = QtWidgets.QLabel(self)
        self.arac_baglan_label3.setGeometry(QtCore.QRect(875, 140, 91, 20))
        self.arac_baglan_label3.setObjectName("arac_baglan_label3")
        self.arac_baglan_label3.setText("Bağlantı Başarısız")
        self.arac_baglan_label3.setHidden(True)

        self.kumanda_baglan_label = QtWidgets.QLabel(self) 
        self.kumanda_baglan_label.setGeometry(QtCore.QRect(675, 140, 91, 20))
        self.kumanda_baglan_label.setObjectName("kumanda_baglan_label")
        self.kumanda_baglan_label.setText("Kumanda Bağlantısı...")
        self.kumanda_baglan_label2 = QtWidgets.QLabel(self)
        self.kumanda_baglan_label2.setGeometry(QtCore.QRect(675, 140, 91, 20))
        self.kumanda_baglan_label2.setObjectName("kumanda_baglan_label2")
        self.kumanda_baglan_label2.setText("Bağlantı Başarılı")
        self.kumanda_baglan_label2.setHidden(True)
        self.kumanda_baglan_label3 = QtWidgets.QLabel(self)
        self.kumanda_baglan_label3.setGeometry(QtCore.QRect(675, 140, 91, 20))
        self.kumanda_baglan_label3.setObjectName("kumanda_baglan_label3")
        self.kumanda_baglan_label3.setText("Bağlantı Başarısız")
        self.kumanda_baglan_label3.setHidden(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(150, 70, 231, 271))
        self.retranslateUi(self)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Araç Kontrol Arayüzü"))
        self.arac_port_secim_label.setText(_translate("Dialog", "Port/"))
        self.arac_Baudrate_label.setText(_translate("Dialog", "BaudRate/"))
        self.arac_Baudrate_ComboBox.setCurrentText(_translate("Dialog", "9600"))
        self.arac_Baudrate_ComboBox.setItemText(0, _translate("Dialog", "4800"))
        self.arac_Baudrate_ComboBox.setItemText(1, _translate("Dialog", "9600"))
        self.arac_Baudrate_ComboBox.setItemText(2, _translate("Dialog", "14400"))
        self.arac_Baudrate_ComboBox.setItemText(3, _translate("Dialog", "19200"))
        self.arac_Baudrate_ComboBox.setItemText(4, _translate("Dialog", "28800"))
        self.arac_Baudrate_ComboBox.setItemText(6, _translate("Dialog", "38400"))       
        self.arac_Baudrate_ComboBox.setItemText(7, _translate("Dialog", "57600"))
        self.arac_Baudrate_ComboBox.setItemText(8, _translate("Dialog", "115200"))
        self.arac_port_secim_ComboBox.setItemText(0, _translate("Dialog", "COM1"))
        self.arac_port_secim_ComboBox.setItemText(1, _translate("Dialog", "COM2"))  
        self.arac_port_secim_ComboBox.setItemText(2, _translate("Dialog", "COM3")) 
        self.arac_port_secim_ComboBox.setItemText(3, _translate("Dialog", "COM4"))
        self.arac_port_secim_ComboBox.setItemText(4, _translate("Dialog", "COM5"))
        self.arac_port_secim_ComboBox.setItemText(5, _translate("Dialog", "COM6"))
        self.arac_port_secim_ComboBox.setItemText(6, _translate("Dialog", "COM7"))
        self.arac_port_secim_ComboBox.setItemText(7, _translate("Dialog", "COM8"))
        self.arac_port_secim_ComboBox.setItemText(8, _translate("Dialog", "COM9"))
        self.arac_port_secim_ComboBox.setItemText(9, _translate("Dialog", "COM10"))
        self.arac_port_secim_ComboBox.setItemText(10, _translate("Dialog", "COM11"))
        self.arac_port_secim_ComboBox.setItemText(11, _translate("Dialog", "COM12"))
        self.arac_port_secim_ComboBox.setItemText(12, _translate("Dialog", "COM13"))
        self.arac_port_secim_ComboBox.setItemText(13, _translate("Dialog", "COM14"))
        self.arac_port_secim_ComboBox.setItemText(14, _translate("Dialog", "COM15"))
        self.arac_baglan_buton.setText(_translate("Dialog", "Bağlan"))
    
        self.kumanda_port_secim_label.setText(_translate("Dialog", "Port/")) 
        self.kumanda_Baudrate_label.setText(_translate("Dialog", "BaudRate/"))
        self.kumanda_Baudrate_ComboBox.setCurrentText(_translate("Dialog", "9600"))
        self.kumanda_Baudrate_ComboBox.setItemText(0, _translate("Dialog", "4800"))
        self.kumanda_Baudrate_ComboBox.setItemText(1, _translate("Dialog", "9600"))
        self.kumanda_Baudrate_ComboBox.setItemText(2, _translate("Dialog", "14400"))
        self.kumanda_Baudrate_ComboBox.setItemText(3, _translate("Dialog", "19200"))
        self.kumanda_Baudrate_ComboBox.setItemText(4, _translate("Dialog", "28800"))
        self.kumanda_Baudrate_ComboBox.setItemText(6, _translate("Dialog", "38400"))       
        self.kumanda_Baudrate_ComboBox.setItemText(7, _translate("Dialog", "57600"))
        self.kumanda_Baudrate_ComboBox.setItemText(8, _translate("Dialog", "115200"))
        self.kumanda_port_secim_ComboBox.setItemText(0, _translate("Dialog", "COM1"))
        self.kumanda_port_secim_ComboBox.setItemText(1, _translate("Dialog", "COM2"))  
        self.kumanda_port_secim_ComboBox.setItemText(2, _translate("Dialog", "COM3")) 
        self.kumanda_port_secim_ComboBox.setItemText(3, _translate("Dialog", "COM4"))
        self.kumanda_port_secim_ComboBox.setItemText(4, _translate("Dialog", "COM5"))
        self.kumanda_port_secim_ComboBox.setItemText(5, _translate("Dialog", "COM6"))
        self.kumanda_port_secim_ComboBox.setItemText(6, _translate("Dialog", "COM7"))
        self.kumanda_port_secim_ComboBox.setItemText(7, _translate("Dialog", "COM8"))
        self.kumanda_port_secim_ComboBox.setItemText(8, _translate("Dialog", "COM9"))
        self.kumanda_port_secim_ComboBox.setItemText(9, _translate("Dialog", "COM10"))
        self.kumanda_port_secim_ComboBox.setItemText(10, _translate("Dialog", "COM11"))
        self.kumanda_port_secim_ComboBox.setItemText(11, _translate("Dialog", "COM12"))
        self.kumanda_port_secim_ComboBox.setItemText(12, _translate("Dialog", "COM13"))
        self.kumanda_port_secim_ComboBox.setItemText(13, _translate("Dialog", "COM14"))
        self.kumanda_port_secim_ComboBox.setItemText(14, _translate("Dialog", "COM15"))
        self.kumanda_baglan_buton.setText(_translate("Dialog", "Bağlan"))
        
        
    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_W:
            print("W")
        elif event.key() == Qt.Key_S:
            print("S")
            self.arac_arduino.write(b'2')
        elif event.key() == Qt.Key_A:
            print("A")
            self.arac_arduino.write(b'4')
        elif event.key() == Qt.Key_D:
            print("D")
            self.arac_arduino.write(b'3')
        elif event.key() == Qt.Key_4:
            print("Q")
            self.arac_arduino.write(b'5')
        elif event.key() == Qt.Key_5:
            print("E")
            self.arac_arduino.write(b'6')
        elif event.key() == Qt.Key_6:
            print("E")
            self.arac_arduino.write(b'7')
        elif event.key() == Qt.Key_F:
            self.a = 1
    def CancelFeed(self):
        exit()
    def arac_baglan(self, Dialog):
        try:
            #self.arduino = serial.Serial(port=str(self.port_secim_ComboBox.currentText()),baudrate = int(self.Baudrate_ComboBox.currentText()))
            self.arac_arduino = serial.Serial(port="COM3",baudrate = int(self.arac_Baudrate_ComboBox.currentText()))
            self.arac_baglan_label.setHidden(True)
            self.arac_baglan_label2.setHidden(False)
            self.arac_baglan_label3.setHidden(True)
        except:
            self.arac_baglan_label.setHidden(True)
            self.arac_baglan_label2.setHidden(True)
            self.arac_baglan_label3.setHidden(False)
    def kumanda_baglan(self, Dialog):
        try:
            self.kumanda_arduino = serial.Serial(port=str(self.kumanda_port_secim_ComboBox.currentText()),baudrate = int(self.kumanda_Baudrate_ComboBox.currentText()))
            self.kumanda_baglan_label.setHidden(True) 
            self.kumanda_baglan_label2.setHidden(False)
            self.kumanda_baglan_label3.setHidden(True)
            self.a = 1
        except:
            self.kumanda_baglan_label.setHidden(True)
            self.kumanda_baglan_label2.setHidden(True)
            self.kumanda_baglan_label3.setHidden(False)
    def write_read(self, Dialog):
        x = self.kumanda_arduino.readline()
        if x is not None:
            self.arac_arduino.write(bytes(str(x), 'utf-8'))
            return x
        time.sleep(0.3)
    def loop(self):
        if self.a == 1:
            print(self.write_read(self))
            
class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(0)
        while self.ThreadActive:
            ret, frame = Capture.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(600, 700, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
    def stop(self):
        self.ThreadActive = False
        self.quit()
    
if __name__ == "__main__":
    App = QApplication(sys.argv)
    Root = MainWindow()
    Root.show()
    sys.exit(App.exec())
