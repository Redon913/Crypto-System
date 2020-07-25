from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date
from functools import partial
import DecryptionAlgo as Decryption, EncryptionAlgo as Encryption, logging, os, stat

class Front_Window(object):

    def __init__(self):
        self.logger=logging.getLogger() 
        self.logger.setLevel(logging.DEBUG)
        self.logger.info("The System has started")
        try:
            os.mkdir('./logs', stat.S_IREAD)
        except OSError as ose:
            self.logger.error(ose)
        logging.basicConfig(filename="./logs/"+ str(date.today()) + ".log", 
                    format='%(asctime)s %(message)s', 
                    filemode='w')
  
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(800, 600)
        MainWindow.setFixedSize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/logo/Main_Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStatusTip("")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(19, 19, 751, 501))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.about_heading_1 = QtWidgets.QLabel(self.frame)
        self.about_heading_1.setGeometry(QtCore.QRect(290, 280, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Unica One")
        font.setPointSize(18)
        self.about_heading_1.setFont(font)
        self.about_heading_1.setAlignment(QtCore.Qt.AlignCenter)
        self.about_heading_1.setObjectName("about_heading_1")

        self.heading_top_1 = QtWidgets.QLabel(self.frame)
        self.heading_top_1.setGeometry(QtCore.QRect(280, 30, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Reality Hyper")
        font.setPointSize(24)
        self.heading_top_1.setFont(font)
        self.heading_top_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.heading_top_1.setAutoFillBackground(False)
        self.heading_top_1.setAlignment(QtCore.Qt.AlignCenter)
        self.heading_top_1.setObjectName("heading_top_1")

        self.hr_line_Above_logo = QtWidgets.QFrame(self.frame)
        self.hr_line_Above_logo.setGeometry(QtCore.QRect(290, 160, 190, 3))
        self.hr_line_Above_logo.setFrameShape(QtWidgets.QFrame.HLine)
        self.hr_line_Above_logo.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hr_line_Above_logo.setObjectName("hr_line_Above_logo")

        self.redon_logo_img = QtWidgets.QLabel(self.frame)
        self.redon_logo_img.setGeometry(QtCore.QRect(240, 170, 281, 81))
        self.redon_logo_img.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.redon_logo_img.setAutoFillBackground(False)
        self.redon_logo_img.setText("")
        self.redon_logo_img.setPixmap(QtGui.QPixmap("./images/logo/Redon_Logo.png"))
        self.redon_logo_img.setAlignment(QtCore.Qt.AlignCenter)
        self.redon_logo_img.setObjectName("redon_logo_img")

        self.hr_line_below_logo = QtWidgets.QFrame(self.frame)
        self.hr_line_below_logo.setGeometry(QtCore.QRect(290, 270, 190, 3))
        self.hr_line_below_logo.setFrameShape(QtWidgets.QFrame.HLine)
        self.hr_line_below_logo.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hr_line_below_logo.setObjectName("hr_line_below_logo")

        self.about_heading_2 = QtWidgets.QLabel(self.frame)
        self.about_heading_2.setGeometry(QtCore.QRect(230, 330, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Unica One")
        font.setPointSize(24)
        self.about_heading_2.setFont(font)
        self.about_heading_2.setAlignment(QtCore.Qt.AlignCenter)
        self.about_heading_2.setObjectName("about_heading_2")

        self.option_groupBox = QtWidgets.QGroupBox(self.frame)
        self.option_groupBox.setGeometry(QtCore.QRect(60, 380, 631, 101))
        font = QtGui.QFont()
        font.setFamily("Unica One")
        font.setPointSize(11)
        self.option_groupBox.setFont(font)
        self.option_groupBox.setObjectName("option_groupBox")

        self.To_Encryption = QtWidgets.QPushButton(self.option_groupBox)
        self.To_Encryption.setGeometry(QtCore.QRect(70, 40, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Unica One")
        font.setPointSize(20)
        self.To_Encryption.setFont(font)
        self.To_Encryption.setWhatsThis("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./images/icons/Encryption.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.To_Encryption.setIcon(icon1)
        self.To_Encryption.setIconSize(QtCore.QSize(40, 40))
        self.To_Encryption.setObjectName("To_Encryption")

        self.To_Decryption = QtWidgets.QPushButton(self.option_groupBox)
        self.To_Decryption.setGeometry(QtCore.QRect(350, 40, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Unica One")
        font.setPointSize(20)
        self.To_Decryption.setFont(font)
        self.To_Decryption.setWhatsThis("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./images/icons/Decryption.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.To_Decryption.setIcon(icon2)
        self.To_Decryption.setIconSize(QtCore.QSize(40, 40))
        self.To_Decryption.setObjectName("To_Decryption")

        self.heading_top_3 = QtWidgets.QLabel(self.frame)
        self.heading_top_3.setGeometry(QtCore.QRect(240, 110, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Reality Hyper")
        font.setPointSize(24)
        self.heading_top_3.setFont(font)
        self.heading_top_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.heading_top_3.setAutoFillBackground(False)
        self.heading_top_3.setAlignment(QtCore.Qt.AlignCenter)
        self.heading_top_3.setObjectName("heading_top_3")

        self.heading_top_2 = QtWidgets.QLabel(self.frame)
        self.heading_top_2.setGeometry(QtCore.QRect(350, 70, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Reality Hyper")
        font.setPointSize(24)
        self.heading_top_2.setFont(font)
        self.heading_top_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.heading_top_2.setAutoFillBackground(False)
        self.heading_top_2.setAlignment(QtCore.Qt.AlignCenter)
        self.heading_top_2.setObjectName("heading_top_2")

        self.made_by_text = QtWidgets.QLabel(self.centralwidget)
        self.made_by_text.setGeometry(QtCore.QRect(300, 540, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Unica One")
        font.setPointSize(16)
        self.made_by_text.setFont(font)
        self.made_by_text.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.made_by_text.setAutoFillBackground(False)
        self.made_by_text.setAlignment(QtCore.Qt.AlignCenter)
        self.made_by_text.setObjectName("made_by_text")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Unica One")
        font.setPointSize(12)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslate_Front_Ui(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate_Front_Ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Redon\'s Crypto-System"))
        self.about_heading_1.setText(_translate("MainWindow", "Summer Training"))
        self.heading_top_1.setText(_translate("MainWindow", "Welcome"))
        self.about_heading_2.setText(_translate("MainWindow", "Applied Cryptography"))
        self.option_groupBox.setTitle(_translate("MainWindow", "Choose An Option"))
        self.To_Encryption.setStatusTip(_translate("MainWindow", "You will be taken to the Encryption Engine"))
        self.To_Encryption.setText(_translate("MainWindow", "Encryption"))
        self.To_Encryption.clicked.connect(partial(self.Encryption_Ui, MainWindow))
        self.To_Decryption.setStatusTip(_translate("MainWindow", "You will be taken to the Decryption Engine"))
        self.To_Decryption.clicked.connect(partial(self.Decryption_Ui, MainWindow))
        self.To_Decryption.setText(_translate("MainWindow", "Decryption"))
        self.heading_top_3.setText(_translate("MainWindow", "CryptoEngine"))
        self.heading_top_2.setText(_translate("MainWindow", "to"))
        self.made_by_text.setText(_translate("MainWindow", "Project By Redon"))
        self.made_by_text.setStatusTip(_translate("MainWindow", "Can Contact me: https://redon913.github.io/profile/"))

    def Encryption_Ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(800, 600)
        MainWindow.setFixedSize(800,600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\images\\icons\\Encryption.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.encryption_widget = QtWidgets.QWidget(MainWindow)
        self.encryption_widget.setObjectName("encryption_widget")

        self.back = QtWidgets.QCommandLinkButton(self.encryption_widget)
        self.back.setGeometry(QtCore.QRect(40, 10, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Unica One")
        font.setPointSize(12)
        self.back.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\images\\icons\\back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back.setIcon(icon1)
        self.back.setIconSize(QtCore.QSize(30, 30))
        self.back.setObjectName("back")

        self.Title_label = QtWidgets.QLabel(self.encryption_widget)
        self.Title_label.setGeometry(QtCore.QRect(230, 10, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Reality Hyper")
        font.setPointSize(22)
        self.Title_label.setFont(font)
        self.Title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Title_label.setObjectName("Title_label")

        self.Encryption_input = QtWidgets.QFrame(self.encryption_widget)
        self.Encryption_input.setGeometry(QtCore.QRect(30, 90, 741, 241))
        font = QtGui.QFont()
        font.setFamily("Unica One")
        font.setPointSize(12)
        self.Encryption_input.setFont(font)
        self.Encryption_input.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Encryption_input.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Encryption_input.setObjectName("Encryption_input")

        self.Cipher_selection_comboBox = QtWidgets.QComboBox(self.Encryption_input)
        self.Cipher_selection_comboBox.setGeometry(QtCore.QRect(170, 10, 500, 20))
        self.Cipher_selection_comboBox.setObjectName("Cipher_selection_comboBox")
        self.Cipher_selection_comboBox.addItem("")
        self.Cipher_selection_comboBox.addItem("")
        self.Cipher_selection_comboBox.addItem("")

        self.Cipher_algo_label = QtWidgets.QLabel(self.Encryption_input)
        self.Cipher_algo_label.setGeometry(QtCore.QRect(30, 10, 120, 20))
        self.Cipher_algo_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Cipher_algo_label.setObjectName("Cipher_algo_label")

        self.Plaintext_label = QtWidgets.QLabel(self.Encryption_input)
        self.Plaintext_label.setGeometry(QtCore.QRect(30, 50, 120, 20))
        self.Plaintext_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Plaintext_label.setObjectName("Plaintext_label")

        self.Plaintext_TextEdit = QtWidgets.QPlainTextEdit(self.Encryption_input)
        self.Plaintext_TextEdit.setGeometry(QtCore.QRect(170, 50, 410, 81))
        self.Plaintext_TextEdit.setObjectName("Plaintext_TextEdit")

        self.Key_label = QtWidgets.QLabel(self.Encryption_input)
        self.Key_label.setGeometry(QtCore.QRect(40, 150, 120, 20))
        self.Key_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Key_label.setObjectName("Key_label")

        self.Key_lineEdit = QtWidgets.QLineEdit(self.Encryption_input)
        self.Key_lineEdit.setGeometry(QtCore.QRect(170, 140, 410, 31))
        self.Key_lineEdit.setObjectName("Key_lineEdit")

        self.Encrypt_submit_button = QtWidgets.QPushButton(self.Encryption_input)
        self.Encrypt_submit_button.setGeometry(QtCore.QRect(270, 190, 241, 30))
        self.Encrypt_submit_button.setObjectName("Encrypt_submit_button")

        self.Browse_Key_Files = QtWidgets.QToolButton(self.Encryption_input)
        self.Browse_Key_Files.setGeometry(QtCore.QRect(580, 140, 91, 31))
        self.Browse_Key_Files.setObjectName("Browse_Key_Files")

        self.Browse_Plaintext_Files = QtWidgets.QToolButton(self.Encryption_input)
        self.Browse_Plaintext_Files.setGeometry(QtCore.QRect(580, 50, 91, 31))
        self.Browse_Plaintext_Files.setObjectName("Browse_Plaintext_Files")

        self.line_below_title = QtWidgets.QFrame(self.encryption_widget)
        self.line_below_title.setGeometry(QtCore.QRect(30, 60, 741, 20))
        self.line_below_title.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_below_title.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_below_title.setObjectName("line_below_title")

        self.Cipher_text_output_field = QtWidgets.QTextBrowser(self.encryption_widget)
        self.Cipher_text_output_field.setGeometry(QtCore.QRect(200, 370, 501, 101))
        font = QtGui.QFont()
        font.setFamily("Unica One")
        font.setPointSize(12)
        self.Cipher_text_output_field.setFont(font)
        self.Cipher_text_output_field.setObjectName("Cipher_text_output_field")

        self.Cipher_Text_label = QtWidgets.QLabel(self.encryption_widget)
        self.Cipher_Text_label.setGeometry(QtCore.QRect(60, 370, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Unica One")
        font.setPointSize(12)   
        self.Cipher_Text_label.setFont(font)
        self.Cipher_Text_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Cipher_Text_label.setObjectName("Cipher_Text_label")

        self.line_below_Enc_input = QtWidgets.QFrame(self.encryption_widget)
        self.line_below_Enc_input.setGeometry(QtCore.QRect(30, 340, 741, 20))
        self.line_below_Enc_input.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_below_Enc_input.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_below_Enc_input.setObjectName("line_below_Enc_input")

        self.line_below_Cipher_output = QtWidgets.QFrame(self.encryption_widget)
        self.line_below_Cipher_output.setGeometry(QtCore.QRect(30, 480, 741, 20))
        self.line_below_Cipher_output.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_below_Cipher_output.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_below_Cipher_output.setObjectName("line_below_Cipher_output")

        self.Message_Display = QtWidgets.QLabel(self.encryption_widget)
        self.Message_Display.setGeometry(QtCore.QRect(90, 500, 611, 51))
        font = QtGui.QFont()
        font.setFamily("Unica One")
        font.setPointSize(12)
        self.Message_Display.setFont(font)
        self.Message_Display.setText("")
        self.Message_Display.setAlignment(QtCore.Qt.AlignCenter)
        self.Message_Display.setObjectName("Message_Display")

        MainWindow.setCentralWidget(self.encryption_widget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Unica One")
        font.setPointSize(12)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslate_Encrypt_Ui(MainWindow)
        MainWindow.show()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate_Encrypt_Ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Redon\'s Encryption Engine"))
        self.Title_label.setText(_translate("MainWindow", "ENCRYPTION ENGINE"))
        self.Cipher_selection_comboBox.setItemText(0, _translate("MainWindow", "Caesar Cipher"))
        self.Cipher_selection_comboBox.setItemText(1, _translate("MainWindow", "Vigenere Cipher"))
        self.Cipher_selection_comboBox.setItemText(2, _translate("MainWindow", "Rail Fence Cipher"))
        self.Cipher_algo_label.setText(_translate("MainWindow", "Cipher Algorithm:"))
        self.Plaintext_label.setText(_translate("MainWindow", "Plain Text:"))
        self.Key_label.setText(_translate("MainWindow", "Key"))
        self.Encrypt_submit_button.setText(_translate("MainWindow", "Encrypt"))
        self.Encrypt_submit_button.setStatusTip(_translate("MainWindow", "Your plaintext will be encrypted"))
        self.Encrypt_submit_button.clicked.connect(self.encryption_Logic)
        self.Browse_Plaintext_Files.setText(_translate("MainWindow", "Browse File"))
        self.Browse_Plaintext_Files.clicked.connect(self.openPlaintextFile)
        self.Browse_Key_Files.setText(_translate("MainWindow", "Browse File"))
        self.Browse_Key_Files.clicked.connect(self.openKeyFile)
        self.Cipher_Text_label.setText(_translate("MainWindow", "Cipher Text:"))
        self.back.setText(_translate("MainWindow", "Back"))
        self.back.setStatusTip(_translate("MainWindow", "You will be taken to the Main Window"))
        self.back.clicked.connect(partial(self.setupUi, MainWindow))

    def encryption_Logic(self):
        try:
            self.Message_Display.setText("")
            if(self.Cipher_selection_comboBox.currentIndex() == 0):
                self.key = self.Key_lineEdit.text()
                self.plainText = self.Plaintext_TextEdit.toPlainText()
                self.CaesarCipher = Encryption.CaesarCipher(str(self.plainText), int(self.key))
                self.Cipher_text_output_field.setText(self.CaesarCipher.CipherText())
            elif(self.Cipher_selection_comboBox.currentIndex() == 1):
                self.key = self.Key_lineEdit.text()
                self.plainText = self.Plaintext_TextEdit.toPlainText()
                self.VigenereCipher = Encryption.VigenereCipher(str(self.plainText), str(self.key))
                self.Cipher_text_output_field.setText(self.VigenereCipher.CipherText())
            elif(self.Cipher_selection_comboBox.currentIndex() == 2):
                self.key = self.Key_lineEdit.text()
                self.plainText = self.Plaintext_TextEdit.toPlainText()
                self.RailCipher = Encryption.RailFence(str(self.plainText), int(self.key))
                self.Cipher_text_output_field.setText(self.RailCipher.CipherText())
        except ValueError as Ve:
            self.logger.error(Ve)
            if('string not found' in str(Ve)):
                self.Message_Display.setText("Please make input Key an String\nInteger here will be real bad")
            elif('int() with base 10' in str(Ve)):
                self.Message_Display.setText("Please make input Key an interger\nString there causes heartattack in my lungs")
            else:
             self.Message_Display.setText("Please check your inputs\nThey are causing headache in my stomach")
        except Exception as e:
            self.logger.error(e)
            self.Message_Display.setText("Please check your inputs\nThey are causing headache in my stomach")

    def Decryption_Ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(800, 600)
        MainWindow.setFixedSize(800,600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\images\\icons\\Decryption.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.decryption_widget = QtWidgets.QWidget(MainWindow)
        self.decryption_widget.setObjectName("decryption_widget")

        self.back = QtWidgets.QCommandLinkButton(self.decryption_widget)
        self.back.setGeometry(QtCore.QRect(40, 10, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Unica One")
        font.setPointSize(12)
        self.back.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\images\\icons\\back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back.setIcon(icon1)
        self.back.setIconSize(QtCore.QSize(30, 30))
        self.back.setObjectName("back")

        self.Title_label = QtWidgets.QLabel(self.decryption_widget)
        self.Title_label.setGeometry(QtCore.QRect(230, 10, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Reality Hyper")
        font.setPointSize(22)
        self.Title_label.setFont(font)
        self.Title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Title_label.setObjectName("Title_label")

        self.Decryption_input = QtWidgets.QFrame(self.decryption_widget)
        self.Decryption_input.setGeometry(QtCore.QRect(30, 90, 741, 241))
        font = QtGui.QFont()
        font.setFamily("Unica One")
        font.setPointSize(12)
        self.Decryption_input.setFont(font)
        self.Decryption_input.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Decryption_input.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Decryption_input.setObjectName("Decryption_input")

        self.Cipher_selection_comboBox = QtWidgets.QComboBox(self.Decryption_input)
        self.Cipher_selection_comboBox.setGeometry(QtCore.QRect(170, 10, 500, 20))
        self.Cipher_selection_comboBox.setObjectName("Cipher_selection_comboBox")
        self.Cipher_selection_comboBox.addItem("")
        self.Cipher_selection_comboBox.addItem("")
        self.Cipher_selection_comboBox.addItem("")

        self.Cipher_algo_label = QtWidgets.QLabel(self.Decryption_input)
        self.Cipher_algo_label.setGeometry(QtCore.QRect(30, 10, 120, 20))
        self.Cipher_algo_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Cipher_algo_label.setObjectName("Cipher_algo_label")

        self.Plaintext_label = QtWidgets.QLabel(self.Decryption_input)
        self.Plaintext_label.setGeometry(QtCore.QRect(30, 50, 120, 20))
        self.Plaintext_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Plaintext_label.setObjectName("Plaintext_label")

        self.Plaintext_TextEdit = QtWidgets.QPlainTextEdit(self.Decryption_input)
        self.Plaintext_TextEdit.setGeometry(QtCore.QRect(170, 50, 410, 81))
        self.Plaintext_TextEdit.setObjectName("Plaintext_TextEdit")

        self.Key_label = QtWidgets.QLabel(self.Decryption_input)
        self.Key_label.setGeometry(QtCore.QRect(40, 150, 120, 20))
        self.Key_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Key_label.setObjectName("Key_label")

        self.Key_lineEdit = QtWidgets.QLineEdit(self.Decryption_input)
        self.Key_lineEdit.setGeometry(QtCore.QRect(170, 140, 410, 31))
        self.Key_lineEdit.setObjectName("Key_lineEdit")

        self.Decrypt_submit_button = QtWidgets.QPushButton(self.Decryption_input)
        self.Decrypt_submit_button.setGeometry(QtCore.QRect(270, 190, 241, 30))
        self.Decrypt_submit_button.setObjectName("Encrypt_submit_button")

        self.Browse_Key_Files = QtWidgets.QToolButton(self.Decryption_input)
        self.Browse_Key_Files.setGeometry(QtCore.QRect(580, 140, 91, 31))
        self.Browse_Key_Files.setObjectName("Browse_Key_Files")

        self.Browse_Plaintext_Files = QtWidgets.QToolButton(self.Decryption_input)
        self.Browse_Plaintext_Files.setGeometry(QtCore.QRect(580, 50, 91, 31))
        self.Browse_Plaintext_Files.setObjectName("Browse_Plaintext_Files")

        self.line_below_title = QtWidgets.QFrame(self.decryption_widget)
        self.line_below_title.setGeometry(QtCore.QRect(30, 60, 741, 20))
        self.line_below_title.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_below_title.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_below_title.setObjectName("line_below_title")

        self.Cipher_text_output_field = QtWidgets.QTextBrowser(self.decryption_widget)
        self.Cipher_text_output_field.setGeometry(QtCore.QRect(200, 370, 501, 101))
        font = QtGui.QFont()
        font.setFamily("Unica One")
        font.setPointSize(12)
        self.Cipher_text_output_field.setFont(font)
        self.Cipher_text_output_field.setObjectName("Cipher_text_output_field")

        self.Cipher_Text_label = QtWidgets.QLabel(self.decryption_widget)
        self.Cipher_Text_label.setGeometry(QtCore.QRect(60, 370, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Unica One")
        font.setPointSize(12)   
        self.Cipher_Text_label.setFont(font)
        self.Cipher_Text_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Cipher_Text_label.setObjectName("Cipher_Text_label")

        self.line_below_Enc_input = QtWidgets.QFrame(self.decryption_widget)
        self.line_below_Enc_input.setGeometry(QtCore.QRect(30, 340, 741, 20))
        self.line_below_Enc_input.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_below_Enc_input.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_below_Enc_input.setObjectName("line_below_Enc_input")

        self.line_below_Cipher_output = QtWidgets.QFrame(self.decryption_widget)
        self.line_below_Cipher_output.setGeometry(QtCore.QRect(30, 480, 741, 20))
        self.line_below_Cipher_output.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_below_Cipher_output.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_below_Cipher_output.setObjectName("line_below_Cipher_output")

        self.Message_Display = QtWidgets.QLabel(self.decryption_widget)
        self.Message_Display.setGeometry(QtCore.QRect(90, 500, 611, 51))
        font = QtGui.QFont()
        font.setFamily("Unica One")
        font.setPointSize(12)
        self.Message_Display.setFont(font)
        self.Message_Display.setText("")
        self.Message_Display.setAlignment(QtCore.Qt.AlignCenter)
        self.Message_Display.setObjectName("Message_Display")

        MainWindow.setCentralWidget(self.decryption_widget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Unica One")
        font.setPointSize(12)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslate_Decrypt_Ui(MainWindow)
        MainWindow.show()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate_Decrypt_Ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Redon\'s Decryption Engine"))
        self.Title_label.setText(_translate("MainWindow", "DECRYPTION ENGINE"))
        self.Cipher_selection_comboBox.setItemText(0, _translate("MainWindow", "Caesar Cipher"))
        self.Cipher_selection_comboBox.setItemText(1, _translate("MainWindow", "Vigenere Cipher"))
        self.Cipher_selection_comboBox.setItemText(2, _translate("MainWindow", "Rail Fence Cipher"))
        self.Cipher_algo_label.setText(_translate("MainWindow", "Cipher Algorithm:"))
        self.Plaintext_label.setText(_translate("MainWindow", "Cipher Text:"))
        self.Key_label.setText(_translate("MainWindow", "Key"))
        self.Decrypt_submit_button.setText(_translate("MainWindow", "Decrypt"))
        self.Decrypt_submit_button.setStatusTip(_translate("MainWindow", "Your ciphertext will be decrypted"))
        self.Decrypt_submit_button.clicked.connect(self.decryption_Logic)
        self.Browse_Plaintext_Files.setText(_translate("MainWindow", "Browse File"))
        self.Browse_Plaintext_Files.clicked.connect(self.openPlaintextFile)
        self.Browse_Key_Files.setText(_translate("MainWindow", "Browse File"))
        self.Browse_Key_Files.clicked.connect(self.openKeyFile)
        self.Cipher_Text_label.setText(_translate("MainWindow", "Plain Text:"))
        self.back.setText(_translate("MainWindow", "Back"))
        self.back.setStatusTip(_translate("MainWindow", "You will be taken to the Main Window"))
        self.back.clicked.connect(partial(self.setupUi, MainWindow))

    def decryption_Logic(self):
        try:
            self.Message_Display.setText("")
            if(self.Cipher_selection_comboBox.currentIndex() == 0):
                self.key = self.Key_lineEdit.text()
                self.plainText = self.Plaintext_TextEdit.toPlainText()
                self.CaesarCipher = Decryption.CaesarCipher(str(self.plainText), int(self.key))
                self.Cipher_text_output_field.setText(self.CaesarCipher.PlainText())
            elif(self.Cipher_selection_comboBox.currentIndex() == 1):
                self.key = self.Key_lineEdit.text()
                self.plainText = self.Plaintext_TextEdit.toPlainText()
                self.VigenereCipher = Decryption.VigenereCipher(str(self.plainText), str(self.key))
                self.Cipher_text_output_field.setText(self.VigenereCipher.PlainText())       
            elif(self.Cipher_selection_comboBox.currentIndex() == 2):
                self.key = self.Key_lineEdit.text()
                self.plainText = self.Plaintext_TextEdit.toPlainText()
                self.RailCipher = Decryption.RailFence(str(self.plainText), int(self.key))
                self.Cipher_text_output_field.setText(self.RailCipher.PlainText())       
        except ValueError as Ve:
            self.logger.error(Ve)
            if('string not found' in str(Ve)):
                self.Message_Display.setText("Please make input Key an String\nInteger here will be real bad")
            elif('int() with base 10' in str(Ve)):
                self.Message_Display.setText("Please make input Key an interger\nString there causes heartattack in my lungs")
            else:
             self.Message_Display.setText("Please check your inputs\nThey are causing headache in my stomach")
        except Exception as e:
            self.logger.error(e)
            self.Message_Display.setText("Please check your inputs\nThey are causing headache in my stomach")

    def openKeyFile(self):
        try:
            self.logger.info("User is importing key file")
            filepath = QtWidgets.QFileDialog.getOpenFileName()
            text = ""
            self.logger.info("User is imported key file")
            with open(filepath[0], 'r') as file:
                text = text.join(file.readlines())
            self.finalKeyText =  text
            self.Key_lineEdit.setText(self.finalKeyText)
        except UnicodeDecodeError as UdE:
            self.logger.error(UdE)
            self.Key_lineEdit.setText("")
            self.Cipher_text_output_field.setText("")
            self.Message_Display.setText("Sorry!! I can't open this file\nplease try again or another file")
        except Exception as e:
            self.logger.error(e)
            self.Message_Display.setText("Please check your inputs\nThey are causing headache in my stomach")

    def openPlaintextFile(self):
        try:
            self.logger.info("User is importing plaintext file")
            filepath = QtWidgets.QFileDialog.getOpenFileName()
            text = ""
            self.logger.info("User is imported plaintext file")
            with open(filepath[0], 'r') as file:
                text = text.join(file.readlines())
            self.finalPlaintextText =  text
            self.Plaintext_TextEdit.setPlainText(self.finalPlaintextText)
        except UnicodeDecodeError as UdE:
            self.logger.error(str(UdE))
            self.Plaintext_TextEdit.setPlainText("")
            self.Cipher_text_output_field.setText("")
            self.Message_Display.setText("Sorry!! I can't open this file\nplease try again or another file")
        except Exception as e:
            self.logger.error(e)
            self.Message_Display.setText("Please check your inputs\nThey are causing headache in my stomach")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    MainWindow = QtWidgets.QMainWindow()
    Front = Front_Window()
    Front.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())