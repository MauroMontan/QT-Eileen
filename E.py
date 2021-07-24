
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from source import icons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(821, 496)
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)
        MainWindow.setStyleSheet(u"QStackedWidget{\n"
"border-bottom-left-radius: 15px;\n"
" border-bottom-right-radius: 15px;\n"
"\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QFrame{\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border-radius:10px;\n"
"\n"
"}")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMaximumSize(QSize(16777215, 36))
        self.header.setStyleSheet(u"background:#03B898;\n"
"\n"

" border-bottom-left-radius: 0px;\n"
" border-bottom-right-radius: 0px;")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, -1, -1, -1)



        self.horizontalSpacer = QSpacerItem(150, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.frame_4 = QFrame(self.header)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Inconsolata")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:white;")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label)


        self.horizontalLayout_3.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.header)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMaximumSize(QSize(170, 30))
        self.frame_3.setStyleSheet(u"*{\n"
"\n"
"background:;\n"
"}\n"
"\n"
"QPushButton{\n"
"background:rgb(0, 255, 255);\n"
"}")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.frame_3.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(20, 20))
        self.pushButton_3.setStyleSheet(u"background:transparent;")
        icon = QIcon()
        icon.addFile(u":/imagenes/dentro.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setFlat(True)

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(20, 20))
        self.pushButton_2.setStyleSheet(u"background:transparent;")
        icon1 = QIcon()
        icon1.addFile(u":/imagenes/fuera.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setFlat(True)

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setMaximumSize(QSize(20, 20))
        self.pushButton.setFocusPolicy(Qt.NoFocus)
        self.pushButton.setContextMenuPolicy(Qt.NoContextMenu)
        self.pushButton.setStyleSheet(u"background:#03B898;")
        icon2 = QIcon()
        icon2.addFile(u":/imagenes/cerrar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QSize(14, 14))
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(True)

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.horizontalLayout_3.addWidget(self.frame_3)


        self.gridLayout.addWidget(self.header, 0, 0, 1, 3)

        self.body = QFrame(self.centralwidget)
        self.body.setObjectName(u"body")
        self.body.setStyleSheet(u"")
        self.body.setFrameShape(QFrame.NoFrame)
        self.body.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.body)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.body, 2, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMouseTracking(True)
        self.stackedWidget.setStyleSheet(u"*{\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:10px;\n"
"background:#4A4A4A;\n"
"\n"
"}\n"
"\n"
"QLineEdit{\n"
"background:white;\n"
"border-bottom-left-radius:10px;\n"
"\n"
"}\n"
"\n"
"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_7 = QHBoxLayout(self.page)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame{border-bottom-left-radius: 0px;\n"
" border-bottom-right-radius: 15px;}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.frame_5)
        if (self.tableWidget.columnCount() < 9):
            self.tableWidget.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"*{\n"
"	margin-left:0px;\n"
"	color:white;\n"
"	background:#4A4A4A;\n"
"	selection-background-color: rgb(170, 170, 255);\n"
"	border:2px;\n"
"}\n"
"\n"
"indicator:unchecked {\n"
"    background-color:#4A4A4A;\n"
"	color:white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	\n"
"	font: 97 15pt \"Inconsolata\";\n"
"    background-color: #4A4A4A;\n"
"	color:white;\n"
"    border:6px;\n"
"    height: 25px;\n"
"}\n"
"\n"
"QTableCornerButton:section{\n"
"background:rgb(170, 85, 255);\n"
"border:none;\n"
"}\n"
"\n"
"QScrollBar:vertical{\n"
"}\n"
"\n"
"QScrollBar:horizontal{\n"
"\n"
"}\n"
"\n"
"QTableView::item:alternate {\n"
"\n"
" background-color:#3DCC8E; \n"
"} \n"
"\n"
"")
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAutoScrollMargin(5)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget.setGridStyle(Qt.DashDotLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(110)
        self.tableWidget.verticalHeader().setVisible(False)

        self.gridLayout_3.addWidget(self.tableWidget, 0, 1, 1, 1)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 200))
        self.frame_6.setStyleSheet(u"\n"
"border-bottom-right-radius: 15px;\n"
"margin-bottom:3px;\n"
"margin-left:5px;\n"
"background:#4A4A4A;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.frame_6)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(800, 50))
        self.lineEdit.setStyleSheet(u"border:1px solid transparent;\n"
"\n"
"border-radius:10px;\n"
"\n"
"background:#3DCC8E;\n"
"color:white;")

        self.horizontalLayout_6.addWidget(self.lineEdit)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)









        self.gridLayout_3.addWidget(self.frame_6, 1, 1, 1, 1)


        self.horizontalLayout_7.addWidget(self.frame_5)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"QWidget{\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"\n"
"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"\n"
"}")
        self.gridLayout_8 = QGridLayout(self.page_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.frame = QFrame(self.page_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 70))
        self.frame.setStyleSheet(u"*{\n"
"background:#4A4A4A;\n"
"color:white;\n"
" border-top-left-radius: 10px;\n"
" border-top-right-radius: 10px;\n"
" border-bottom-left-radius: 0px;\n"
" border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QLineEdit{\n"
" border-bottom-left-radius: 10px;\n"
" border-bottom-right-radius: 10px;\n"
"background:#3DCC8E;\n"
"color:white;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(20, 9, 20, 9)
        self.lineEdit_16 = QLineEdit(self.frame)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_7.addWidget(self.lineEdit_16, 1, 1, 1, 1)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_7.addWidget(self.label_11, 0, 0, 1, 1)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_7.addWidget(self.label_12, 1, 0, 1, 1)

        self.lineEdit_17 = QLineEdit(self.frame)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_7.addWidget(self.lineEdit_17, 0, 1, 1, 1)


        self.gridLayout_8.addWidget(self.frame, 0, 0, 1, 2)

        self.frame_7 = QFrame(self.page_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"\n"
"\n"
"QFrame{\n"
"background:white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"\n"
"background:rgb(170, 85, 255);\n"
"color:white;\n"
"}")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_7)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setLayoutDirection(Qt.LeftToRight)
        self.frame_8.setStyleSheet(u"QTimeEdit{\n"
"background:#3DCC8E;\n"
"color:black;\n"
"\n"
" border-top-right-radius: 15px;\n"
" border-bottom-right-radius: 15px;\n"
" border-bottom-left-radius:15px;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QLineEdit{\n"
"background:#3DCC8E;\n"
"color:white;\n"
"}\n"
"\n"
"QFrame{\n"
"color:white;\n"
"background:#4A4A4A;\n"
"border-radius:0;\n"
"}")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Plain)
        self.gridLayout_6 = QGridLayout(self.frame_8)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(70, 20))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_3, 2, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.frame_8)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMaximumSize(QSize(230, 20))
        self.lineEdit_7.setAlignment(Qt.AlignCenter)
        self.lineEdit_7.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.lineEdit_7, 7, 3, 1, 1)

        self.linLunes = QLineEdit(self.frame_8)
        self.linLunes.setObjectName(u"linLunes")
        self.linLunes.setMaximumSize(QSize(130, 30))
        self.linLunes.setMaxLength(11)
        self.linLunes.setEchoMode(QLineEdit.Normal)
        self.linLunes.setAlignment(Qt.AlignCenter)
        self.linLunes.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.linLunes, 2, 1, 1, 1)

        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(70, 20))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_2, 3, 0, 1, 1)

        self.label_5 = QLabel(self.frame_8)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(70, 20))
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_5, 5, 0, 1, 1)

        self.lineDomingo = QLineEdit(self.frame_8)
        self.lineDomingo.setObjectName(u"lineDomingo")
        self.lineDomingo.setMaximumSize(QSize(130, 30))
        self.lineDomingo.setMaxLength(11)
        self.lineDomingo.setAlignment(Qt.AlignCenter)
        self.lineDomingo.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.lineDomingo, 8, 1, 1, 1)

        self.lineEdit_6 = QLineEdit(self.frame_8)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMaximumSize(QSize(230, 20))
        self.lineEdit_6.setAlignment(Qt.AlignCenter)
        self.lineEdit_6.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.lineEdit_6, 6, 3, 1, 1)

        self.lineViernes = QLineEdit(self.frame_8)
        self.lineViernes.setObjectName(u"lineViernes")
        self.lineViernes.setMaximumSize(QSize(130, 30))
        self.lineViernes.setMaxLength(11)
        self.lineViernes.setAlignment(Qt.AlignCenter)
        self.lineViernes.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.lineViernes, 6, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame_8)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(230, 20))
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_2.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.lineEdit_2, 2, 3, 1, 1)

        self.lineEdit_5 = QLineEdit(self.frame_8)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMaximumSize(QSize(230, 20))
        self.lineEdit_5.setAlignment(Qt.AlignCenter)
        self.lineEdit_5.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.lineEdit_5, 5, 3, 1, 1)

        self.lineEdit_8 = QLineEdit(self.frame_8)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMaximumSize(QSize(230, 20))
        self.lineEdit_8.setAlignment(Qt.AlignCenter)
        self.lineEdit_8.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.lineEdit_8, 8, 3, 1, 1)

        self.lineJueves = QLineEdit(self.frame_8)
        self.lineJueves.setObjectName(u"lineJueves")
        self.lineJueves.setMaximumSize(QSize(130, 30))
        self.lineJueves.setMaxLength(11)
        self.lineJueves.setAlignment(Qt.AlignCenter)
        self.lineJueves.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.lineJueves, 5, 1, 1, 1)

        self.lineSabado = QLineEdit(self.frame_8)
        self.lineSabado.setObjectName(u"lineSabado")
        self.lineSabado.setMaximumSize(QSize(130, 30))
        self.lineSabado.setMaxLength(11)
        self.lineSabado.setAlignment(Qt.AlignCenter)
        self.lineSabado.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.lineSabado, 7, 1, 1, 1)

        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(70, 20))
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_7, 7, 0, 1, 1)

        self.label_18 = QLabel(self.frame_8)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(16777215, 20))
        self.label_18.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_18, 1, 3, 1, 1)

        self.linMiercoles = QLineEdit(self.frame_8)
        self.linMiercoles.setObjectName(u"linMiercoles")
        self.linMiercoles.setMaximumSize(QSize(130, 30))
        self.linMiercoles.setMaxLength(11)
        self.linMiercoles.setAlignment(Qt.AlignCenter)
        self.linMiercoles.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.linMiercoles, 4, 1, 1, 1)

        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(70, 20))
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_6, 6, 0, 1, 1)

        self.lineMartes = QLineEdit(self.frame_8)
        self.lineMartes.setObjectName(u"lineMartes")
        self.lineMartes.setMaximumSize(QSize(130, 30))
        self.lineMartes.setMaxLength(11)
        self.lineMartes.setAlignment(Qt.AlignCenter)
        self.lineMartes.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.lineMartes, 3, 1, 1, 1)

        self.label_8 = QLabel(self.frame_8)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(70, 20))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_8, 8, 0, 1, 1)

        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(79, 20))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_4, 4, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.frame_8)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMaximumSize(QSize(230, 20))
        self.lineEdit_4.setAlignment(Qt.AlignCenter)
        self.lineEdit_4.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.lineEdit_4, 4, 3, 1, 1)

        self.lineEdit_3 = QLineEdit(self.frame_8)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaximumSize(QSize(230, 20))
        self.lineEdit_3.setAlignment(Qt.AlignCenter)
        self.lineEdit_3.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.lineEdit_3, 3, 3, 1, 1)

        self.label_19 = QLabel(self.frame_8)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_19, 1, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame_8, 0, 1, 1, 1)


        self.gridLayout_8.addWidget(self.frame_7, 1, 0, 1, 4)

        self.pushButton_5 = QPushButton(self.page_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy1)
        self.pushButton_5.setMaximumSize(QSize(110, 30))
        self.pushButton_5.setStyleSheet(u"*{\n"
"background:#3DCC8E;\n"
"color:white;\n"
"border-radius:10px;\n"
"\n"
"}")
        self.pushButton_5.setFlat(False)

        self.gridLayout_8.addWidget(self.pushButton_5, 4, 3, 1, 1)

        self.label_20 = QLabel(self.page_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(16777215, 15))
        self.label_20.setStyleSheet(u"color:white;")

        self.gridLayout_8.addWidget(self.label_20, 3, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.page_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMaximumSize(QSize(16777215, 30))
        self.pushButton_6.setStyleSheet(u"*{\n"
"background:#3DCC8E;\n"
"color:white;\n"
"border-radius:10px;\n"
"\n"
"}")

        self.gridLayout_8.addWidget(self.pushButton_6, 4, 1, 1, 1)

        self.pushButton_7 = QPushButton(self.page_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMaximumSize(QSize(16777215, 30))
        self.pushButton_7.setStyleSheet(u"*{\n"
"background:#3DCC8E;\n"
"color:white;\n"
"border-radius:10px;\n"
"\n"
"}")

        self.gridLayout_8.addWidget(self.pushButton_7, 4, 2, 1, 1)

        self.comboBox = QComboBox(self.page_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox.setStyleSheet(u"QComboBox::drop-down \n"
"{\n"
"    border: 0px;\n"
"}\n"
"QComboBox{\n"
"border:2px solid transparent;\n"
"background:#3DCC8E;\n"
"color:white;\n"
"border-radius:10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow{\n"
"	background:white;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"border-radius:6;\n"
"}\n"
"")
        self.comboBox.setEditable(False)
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setFrame(True)

        self.gridLayout_8.addWidget(self.comboBox, 4, 0, 1, 1)

        self.frame_9 = QFrame(self.page_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"*{\n"
"color:white;\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_9)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.radioButton = QRadioButton(self.frame_9)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.radioButton, 2, 0, 1, 1)

        self.radioButton_2 = QRadioButton(self.frame_9)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.radioButton_2, 2, 1, 1, 1)

        self.label_23 = QLabel(self.frame_9)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(130, 16777215))

        self.gridLayout_2.addWidget(self.label_23, 1, 0, 1, 1)

        self.label_21 = QLabel(self.frame_9)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(40, 40))
        self.label_21.setPixmap(QPixmap(u":/imagenes/quimica.png"))
        self.label_21.setScaledContents(True)

        self.gridLayout_2.addWidget(self.label_21, 1, 1, 1, 1)


        self.gridLayout_8.addWidget(self.frame_9, 0, 2, 1, 2)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_5 = QGridLayout(self.page_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_10 = QFrame(self.page_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_10)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit = QPlainTextEdit(self.frame_10)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setStyleSheet(u"*{\n"
"color:white;\n"
"	font: 20pt \"Ubuntu\";\n"
"\n"
"}")

        self.gridLayout_9.addWidget(self.plainTextEdit, 0, 0, 1, 2)

        self.pushButton_10 = QPushButton(self.frame_10)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(50, 50))
        self.pushButton_10.setMaximumSize(QSize(50, 50))
        self.pushButton_10.setStyleSheet(u"\n"
"*{\n"
"background:white;\n"
"border:2px solid;\n"
"border-radius:20px;\n"
"color:black;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/imagenes/recargar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon5)
        self.pushButton_10.setIconSize(QSize(30, 30))

        self.gridLayout_9.addWidget(self.pushButton_10, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.frame_10)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"\n"
"QFrame{\n"
"background:#4A4A4A;\n"
"\n"
" border-top-left-radius: 0px;\n"
" border-top-right-radius: 0px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.frame_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(160, 16777215))
        self.label_22.setStyleSheet(u"*{\n"
"color:white;\n"
"}")

        self.horizontalLayout_5.addWidget(self.label_22)

        self.comboBox_3 = QComboBox(self.frame_2)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMaximumSize(QSize(250, 30))
        self.comboBox_3.setStyleSheet(u"QComboBox::drop-down \n"
"{\n"
"    border: 0px;\n"
"}\n"
"QComboBox{\n"
"border:2px solid transparent;\n"
"background:#3DCC8E;\n"
"color:white;\n"
"border-radius:10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow{\n"
"	background:white;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"border-radius:6;\n"
"}")
        self.comboBox_3.setIconSize(QSize(300, 30))

        self.horizontalLayout_5.addWidget(self.comboBox_3)

        self.horizontalSpacer_5 = QSpacerItem(250, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.gridLayout_9.addWidget(self.frame_2, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_10, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_3)

        self.gridLayout.addWidget(self.stackedWidget, 2, 2, 1, 1)

        self.frame_11 = QFrame(self.centralwidget)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(60, 16777215))
        self.frame_11.setStyleSheet(u"QFrame{\n"
" border-bottom-left-radius: 15px;\n"
" border-bottom-right-radius: 0px;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;\n"
"background:#4A4A4A;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"	border-radius:10px;\n"
"	background:#3DCC8E;\n"
"	color:white;\n"
"}")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 13, 3, 5)
        self.pushButton_13 = QPushButton(self.frame_11)
        self.pushButton_13.setObjectName(u"pushButton_13")
        icon6 = QIcon()
        icon6.addFile(u":/imagenes/tabla.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_13.setIcon(icon6)
        self.pushButton_13.setIconSize(QSize(30, 40))
        self.pushButton_13.setFlat(True)

        self.verticalLayout.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.frame_11)
        self.pushButton_14.setObjectName(u"pushButton_14")
        icon7 = QIcon()
        icon7.addFile(u":/imagenes/user-interface.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon7)
        self.pushButton_14.setIconSize(QSize(34, 40))
        self.pushButton_14.setFlat(True)

        self.verticalLayout.addWidget(self.pushButton_14)

        self.pushButton_9 = QPushButton(self.frame_6)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/imagenes/confD.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon4)
        self.pushButton_9.setIconSize(QSize(30, 30))
        self.pushButton_9.setFlat(True)

        self.verticalLayout.addWidget(self.pushButton_9)



        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)



        self.pushButton_15 = QPushButton(self.frame_11)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setIcon(icon5)
        self.pushButton_15.setIconSize(QSize(34, 40))
        self.pushButton_15.setFlat(True)

        self.pushButton_8 = QPushButton(self.frame_6)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/imagenes/copiar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon3)
        self.pushButton_8.setIconSize(QSize(30, 30))
        self.pushButton_8.setFlat(True)

        self.verticalLayout.addWidget(self.pushButton_8)


        self.pushButton_12 = QPushButton(self.frame_11)
        self.pushButton_12.setObjectName(u"pushButton_12")
        icon8 = QIcon()
        icon8.addFile(u":/imagenes/lapiz (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon8)
        self.pushButton_12.setIconSize(QSize(34, 40))
        self.pushButton_12.setFlat(True)

        self.verticalLayout.addWidget(self.pushButton_12)






        self.verticalLayout.addWidget(self.pushButton_15)

        self.lineEdit_16.setMaxLength(22)

        self.verticalLayout.addItem(self.verticalSpacer)




        self.gridLayout.addWidget(self.frame_11, 2, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButton.setDefault(False)
        self.stackedWidget.setCurrentIndex(0)

        self.comboBox.addItem("busca una materia para editar/eliminar")
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))


        self.label.setText(QCoreApplication.translate("MainWindow", u"Eileen 2.O", None))
        self.pushButton_3.setText("")
        self.pushButton_2.setText("")
        self.pushButton.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Grupo", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Materia ", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Lunes", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Martes", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Miercoles", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Jueves", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Viernes", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Sabado", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Domingo", None));
#if QT_CONFIG(tooltip)
        self.tableWidget.setToolTip(QCoreApplication.translate("MainWindow", u"Buena suerte!", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"AQUI VA EL LINK", None))
#if QT_CONFIG(tooltip)
        self.pushButton_8.setToolTip(QCoreApplication.translate("MainWindow", u"Copiar Enlace", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_8.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_9.setToolTip(QCoreApplication.translate("MainWindow", u"Ir a la reunion", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_9.setText("")
        self.lineEdit_16.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tu Grupo ", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"MATERIA", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"GRUPO", None))
        self.lineEdit_17.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre de la Materia", None))
        self.lineEdit_17.setClearButtonEnabled(True)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"LUNES", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Primero agrega un horario", None))
        self.linLunes.setPlaceholderText(QCoreApplication.translate("MainWindow", u"00:00-00:00", None))
        self.lineEdit_16.setClearButtonEnabled(True)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"MARTES", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"JUEVES", None))
        self.lineDomingo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"00:00-00:00", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Primero agrega un horario", None))
        self.lineViernes.setPlaceholderText(QCoreApplication.translate("MainWindow", u"00:00-00:00", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Primero agrega un horario", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Primero agrega un horario", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Primero agrega un horario", None))
        self.lineJueves.setPlaceholderText(QCoreApplication.translate("MainWindow", u"00:00-00:00", None))
        self.lineSabado.setPlaceholderText(QCoreApplication.translate("MainWindow", u"00:00-00:00", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"SABADO", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Enlaces(Urls)", None))
        self.linMiercoles.setPlaceholderText(QCoreApplication.translate("MainWindow", u"00:00-00:00", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"VIERNES", None))
        self.lineMartes.setPlaceholderText(QCoreApplication.translate("MainWindow", u"00:00-00:00", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"DOMINGO", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"MIERCOLES", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Primero agrega un horario", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Primero agrega un horario", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Horarios (24hrs)", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"guardar", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Para editar materia en especifico selecciona una materia que hayas agregado", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
#if QT_CONFIG(tooltip)
        self.pushButton_7.setToolTip(QCoreApplication.translate("MainWindow", u"Busca una materia antes", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"eliminar", None))
        self.comboBox.setCurrentText("")
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Si", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Es Laboratorio?", None))
        self.label_21.setText("")
        self.pushButton_10.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Crear una nota para ", None))
#if QT_CONFIG(tooltip)
        self.pushButton_13.setToolTip(QCoreApplication.translate("MainWindow", u"Aqu\u00ed puedes ver tu horario!", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_13.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_14.setToolTip(QCoreApplication.translate("MainWindow", u"A\u00f1ade/edita o elimina una materia", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_14.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_15.setToolTip(QCoreApplication.translate("MainWindow", u"Recarga el Url!", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_12.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_12.setToolTip(QCoreApplication.translate("MainWindow", u"Información", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_15.setText("")
        self.lineEdit_2.setToolTip(QCoreApplication.translate("MainWindow", u"dejar vacio si no hay horario asignado", None))
        self.lineEdit_3.setToolTip(QCoreApplication.translate("MainWindow", u"dejar vacio si no hay horario asignado", None))
        self.lineEdit_4.setToolTip(QCoreApplication.translate("MainWindow", u"dejar vacio si no hay horario asignado", None))
        self.lineEdit_5.setToolTip(QCoreApplication.translate("MainWindow", u"dejar vacio si no hay horario asignado", None))
        self.lineEdit_6.setToolTip(QCoreApplication.translate("MainWindow", u"dejar vacio si no hay horario asignado", None))
        self.lineEdit_7.setToolTip(QCoreApplication.translate("MainWindow", u"dejar vacio si no hay horario asignado", None))
        self.lineEdit_8.setToolTip(QCoreApplication.translate("MainWindow", u"dejar vacio si no hay horario asignado", None))

    # retranslateUi
