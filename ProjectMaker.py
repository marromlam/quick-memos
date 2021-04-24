# -*- coding: UTF-8 -*-


##########################################################################################
# Importing packages. ####################################################################

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import (QByteArray, QDate, QDateTime, QEvent, QPoint, QRect,
                          QRegExp, QSettings, QSize, Qt, QTime, QTimer)
from PyQt5.QtGui import QColor, QIcon, QRegExpValidator, QValidator
from PyQt5.QtWidgets import (QAbstractItemView, QFormLayout ,QAbstractItemDelegate,
                             QAction, QApplication, QComboBox, QDialog, QDialogButtonBox,
                             QFileDialog, QWidget, QPushButton, QLineEdit, QInputDialog,
                             QGridLayout, QGroupBox, QHeaderView, QInputDialog,
                             QItemDelegate, QLabel, QLineEdit, QMainWindow, QMessageBox,
                             QStyle, QStyleOptionViewItem, QTableWidget,QTableWidgetItem,
                             QTreeWidget, QTreeWidgetItem, QVBoxLayout)

from ProLib import *

##########################################################################################



##########################################################################################
# Global Constants and parameters. #######################################################

DefaultNumberOfRows = 120 #(#+1)
database = 'Data'
mode1=1; mode2=1; mode3=1
global factor
factor = 2
separ = '---------------------------------------------'
sectspa = '                             '

##########################################################################################



class Ui_ProjectMaker(object):

    def setupUi(self, ProjectMaker):
        ProjectMaker.setObjectName("ProjectMaker")
        ProjectMaker.setEnabled(True)
        ProjectMaker.resize(361, 452)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ProjectMaker.sizePolicy().hasHeightForWidth())
        ProjectMaker.setSizePolicy(sizePolicy)
        ProjectMaker.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Tabs = QtWidgets.QTabWidget(ProjectMaker)
        self.Tabs.setEnabled(True)
        self.Tabs.setGeometry(QtCore.QRect(12, 46, 336, 392))
        self.Tabs.setTabPosition(QtWidgets.QTabWidget.North)
        self.Tabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.Tabs.setElideMode(QtCore.Qt.ElideMiddle)
        self.Tabs.setUsesScrollButtons(False)
        self.Tabs.setDocumentMode(False)
        self.Tabs.setTabsClosable(False)
        self.Tabs.setTabBarAutoHide(False)
        self.Tabs.setObjectName("Tabs")
        self.AddTab = QtWidgets.QWidget()
        self.AddTab.setObjectName("AddTab")
        self.layoutWidget = QtWidgets.QWidget(self.AddTab)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 291, 331))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.AddDataTable = QtWidgets.QTableWidget(self.layoutWidget)
        self.AddDataTable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.AddDataTable.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.AddDataTable.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AddDataTable.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.AddDataTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.AddDataTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.AddDataTable.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.AddDataTable.setDragEnabled(True)
        self.AddDataTable.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.AddDataTable.setAlternatingRowColors(True)
        self.AddDataTable.setGridStyle(QtCore.Qt.SolidLine)
        self.AddDataTable.setCornerButtonEnabled(False)
        self.AddDataTable.setObjectName("AddDataTable")
        self.AddDataTable.setColumnCount(2)
        self.AddDataTable.setRowCount(2)
        # Setting up default rows. ############################################
        self.AddDataTable.setRowCount(DefaultNumberOfRows+1)
        for l in range(0,DefaultNumberOfRows):
            item = QtWidgets.QTableWidgetItem()
            self.AddDataTable.setVerticalHeaderItem(l, item)
        #######################################################################
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.AddDataTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.AddDataTable.setHorizontalHeaderItem(1, item)
        self.AddDataTable.horizontalHeader().setCascadingSectionResizes(False)
        self.AddDataTable.horizontalHeader().setDefaultSectionSize(119)
        self.AddDataTable.horizontalHeader().setMinimumSectionSize(19)
        self.verticalLayout.addWidget(self.AddDataTable)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.AddVariableNameLabel = QtWidgets.QLabel(self.layoutWidget)
        self.AddVariableNameLabel.setObjectName("AddVariableNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.AddVariableNameLabel)
        self.AddVariableNameBox = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.AddVariableNameBox.setFont(font)
        self.AddVariableNameBox.setObjectName("AddVariableNameBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.AddVariableNameBox)
        self.AddSymbolicNameLabel = QtWidgets.QLabel(self.layoutWidget)
        self.AddSymbolicNameLabel.setObjectName("AddSymbolicNameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.AddSymbolicNameLabel)
        self.AddSymbolicNameBox = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.AddSymbolicNameBox.setFont(font)
        self.AddSymbolicNameBox.setObjectName("AddSymbolicNameBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.AddSymbolicNameBox)
        self.AddVariableUnitsLabel = QtWidgets.QLabel(self.layoutWidget)
        self.AddVariableUnitsLabel.setObjectName("AddVariableUnitsLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.AddVariableUnitsLabel)
        self.AddVariableUnitsBox = QtWidgets.QLineEdit(self.layoutWidget)
        self.AddVariableUnitsBox.setObjectName("AddVariableUnitsBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.AddVariableUnitsBox)
        self.verticalLayout.addLayout(self.formLayout)
        self.splitter = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.AddSave = QtWidgets.QPushButton(self.splitter)
        self.AddSave.setDefault(False)
        self.AddSave.setFlat(False)
        self.AddSave.setObjectName("AddSave")
        self.AddImport = QtWidgets.QPushButton(self.splitter)
        self.AddImport.setObjectName("AddImport")
        self.AddClear = QtWidgets.QPushButton(self.splitter)
        self.AddClear.setObjectName("AddClear")
        self.verticalLayout.addWidget(self.splitter)
        self.Tabs.addTab(self.AddTab, "")
        self.ExpTab = QtWidgets.QWidget()
        self.ExpTab.setObjectName("ExpTab")
        self.layoutWidget1 = QtWidgets.QWidget(self.ExpTab)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 20, 291, 331))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.ExpMethodSelect = QtWidgets.QComboBox(self.layoutWidget1)
        self.ExpMethodSelect.setObjectName("ExpMethodSelect")
        self.ExpMethodSelect.addItem("",1)
        self.ExpMethodSelect.addItem("",2)
        self.ExpMethodSelect.addItem("",3)
        self.verticalLayout_4.addWidget(self.ExpMethodSelect)
        self.ExpVariableSelect = QtWidgets.QListWidget(self.layoutWidget1)
        self.ExpVariableSelect.setAlternatingRowColors(True)
        self.ExpVariableSelect.setObjectName("ExpVariableSelect")
        self.verticalLayout_4.addWidget(self.ExpVariableSelect)
        self.ExpCaptionBox = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setItalic(True)
        self.ExpCaptionBox.setFont(font)
        self.ExpCaptionBox.setObjectName("ExpCaptionBox")
        self.verticalLayout_4.addWidget(self.ExpCaptionBox)
        self.splitter_2 = QtWidgets.QSplitter(self.layoutWidget1)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.ExpPreview = QtWidgets.QPushButton(self.splitter_2)
        self.ExpPreview.setObjectName("ExpPreview")
        self.ExpExport = QtWidgets.QPushButton(self.splitter_2)
        self.ExpExport.setObjectName("ExpExport")
        self.verticalLayout_4.addWidget(self.splitter_2)
        self.Tabs.addTab(self.ExpTab, "")
        self.StaTab = QtWidgets.QWidget()
        self.StaTab.setObjectName("StaTab")
        self.StaDataTable = QtWidgets.QTableWidget(self.StaTab)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.StaDataTable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.StaDataTable.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.StaDataTable.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.StaDataTable.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.StaDataTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.StaDataTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.StaDataTable.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.StaDataTable.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.StaDataTable.setAlternatingRowColors(True)
        self.StaDataTable.setGridStyle(QtCore.Qt.SolidLine)
        self.StaDataTable.setColumnCount(1)
        self.StaDataTable.setGeometry(QtCore.QRect(20, 20, 111, 281))
        self.StaDataTable.setAlternatingRowColors(True)
        self.StaDataTable.setObjectName("StaDataTable")
        self.StaDataTable.horizontalHeader().setDefaultSectionSize(80)
        item = QtWidgets.QTableWidgetItem('Data')
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.StaDataTable.setHorizontalHeaderItem(0, item)
        self.layoutWidget2 = QtWidgets.QWidget(self.StaTab)
        self.layoutWidget2.setGeometry(QtCore.QRect(140, 20, 171, 281))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.StaNumberVariablesSelect = QtWidgets.QComboBox(self.layoutWidget2)
        self.StaNumberVariablesSelect.setObjectName("StaNumberVariablesSelect")
        self.StaNumberVariablesSelect.addItem("",1)
        self.StaNumberVariablesSelect.addItem("",2)
        self.verticalLayout_5.addWidget(self.StaNumberVariablesSelect)
        self.StaVariableSelect = QtWidgets.QListWidget(self.layoutWidget2)
        self.StaVariableSelect.setAlternatingRowColors(True)
        self.StaVariableSelect.setObjectName("StaVariableSelect")
        self.verticalLayout_5.addWidget(self.StaVariableSelect)
        self.StatCobertureLabel = QtWidgets.QLabel(self.layoutWidget2)
        self.StatCobertureLabel.setObjectName("StatCobertureLabel")
        self.verticalLayout_5.addWidget(self.StatCobertureLabel)
        self.StaCobertureSelect = QtWidgets.QComboBox(self.layoutWidget2)
        self.StaCobertureSelect.setObjectName("StaCobertureSelect")
        self.StaCobertureSelect.addItem("",1)
        self.StaCobertureSelect.addItem("",2)
        self.StaCobertureSelect.addItem("",3)
        self.StaCobertureSelect.addItem("",4)
        self.StaCobertureSelect.addItem("",5)
        self.StaCobertureSelect.addItem("",6)
        self.StaCobertureSelect.addItem("",7)
        self.verticalLayout_5.addWidget(self.StaCobertureSelect)
        self.StaStatistics = QtWidgets.QPushButton(self.layoutWidget2)
        self.StaStatistics.setObjectName("StaStatistics")
        self.verticalLayout_5.addWidget(self.StaStatistics)
        self.splitter_3 = QtWidgets.QSplitter(self.StaTab)
        self.splitter_3.setGeometry(QtCore.QRect(15, 320, 301, 32))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.StaCsvCopy = QtWidgets.QPushButton(self.splitter_3)
        self.StaCsvCopy.setObjectName("StaCsvCopy")
        self.StaTexCopy = QtWidgets.QPushButton(self.splitter_3)
        self.StaTexCopy.setObjectName("StaTexCopy")
        self.Tabs.addTab(self.StaTab, "")
        self.KaiTab = QtWidgets.QWidget()
        self.KaiTab.setObjectName("KaiTab")
        self.KaiParameterTable = QtWidgets.QTableWidget(self.KaiTab)
        self.KaiParameterTable.setGeometry(QtCore.QRect(21, 20, 171, 243))
        self.KaiParameterTable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.KaiParameterTable.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.KaiParameterTable.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.KaiParameterTable.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.KaiParameterTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.KaiParameterTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.KaiParameterTable.setAutoScroll(False)
        self.KaiParameterTable.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.KaiParameterTable.setDragEnabled(False)
        self.KaiParameterTable.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.KaiParameterTable.setAlternatingRowColors(True)
        self.KaiParameterTable.setIconSize(QtCore.QSize(0, 0))
        self.KaiParameterTable.setShowGrid(True)
        self.KaiParameterTable.setCornerButtonEnabled(False)
        self.KaiParameterTable.setObjectName("KaiParameterTable")
        self.KaiParameterTable.setColumnCount(2)
        self.KaiParameterTable.setRowCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.KaiParameterTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.KaiParameterTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.KaiParameterTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.KaiParameterTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.KaiParameterTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.KaiParameterTable.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.KaiParameterTable.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.KaiParameterTable.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.KaiParameterTable.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.KaiParameterTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.KaiParameterTable.setHorizontalHeaderItem(1, item)
        self.KaiParameterTable.horizontalHeader().setVisible(True)
        self.KaiParameterTable.horizontalHeader().setCascadingSectionResizes(False)
        self.KaiParameterTable.horizontalHeader().setDefaultSectionSize(67)
        self.KaiParameterTable.horizontalHeader().setHighlightSections(False)
        self.KaiParameterTable.horizontalHeader().setMinimumSectionSize(40)
        self.KaiParameterTable.horizontalHeader().setSortIndicatorShown(False)
        self.KaiParameterTable.horizontalHeader().setStretchLastSection(True)
        self.KaiParameterTable.verticalHeader().setCascadingSectionResizes(False)
        self.KaiParameterTable.verticalHeader().setDefaultSectionSize(24)
        self.KaiParameterTable.verticalHeader().setHighlightSections(False)
        self.KaiDependentBox = QtWidgets.QLineEdit(self.KaiTab)
        self.KaiDependentBox.setGeometry(QtCore.QRect(120, 290, 191, 21))
        self.KaiDependentBox.setAlignment(QtCore.Qt.AlignCenter)
        self.KaiDependentBox.setObjectName("KaiDependentBox")
        self.KaiFunctionLabel = QtWidgets.QLabel(self.KaiTab)
        self.KaiFunctionLabel.setGeometry(QtCore.QRect(20, 270, 287, 18))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.KaiFunctionLabel.setFont(font)
        self.KaiFunctionLabel.setTextFormat(QtCore.Qt.AutoText)
        self.KaiFunctionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.KaiFunctionLabel.setObjectName("KaiFunctionLabel")
        self.KaiTest = QtWidgets.QPushButton(self.KaiTab)
        self.KaiTest.setGeometry(QtCore.QRect(110, 320, 113, 32))
        self.KaiTest.setObjectName("KaiTest")
        self.KaiSqrLabel = QtWidgets.QTextEdit(self.KaiTab)
        self.KaiSqrLabel.setGeometry(QtCore.QRect(200, 20, 111, 141))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(237, 237, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.NoRole, brush)
        self.KaiSqrLabel.setPalette(palette)
        self.KaiSqrLabel.setAutoFillBackground(True)
        self.KaiSqrLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.KaiSqrLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.KaiSqrLabel.setLineWidth(1)
        self.KaiSqrLabel.setReadOnly(True)
        self.KaiSqrLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.KaiSqrLabel.setObjectName("KaiSqrLabel")
        self.KaiConfidenceBox = QtWidgets.QLineEdit(self.KaiTab)
        self.KaiConfidenceBox.setGeometry(QtCore.QRect(200, 130, 111, 21))
        self.KaiConfidenceBox.setAlignment(QtCore.Qt.AlignCenter)
        self.KaiConfidenceBox.setObjectName("KaiConfidenceBox")
        self.KaiConfidenceLabel = QtWidgets.QLabel(self.KaiTab)
        self.KaiConfidenceLabel.setGeometry(QtCore.QRect(200, 90, 111, 41))
        self.KaiConfidenceLabel.setText("<html><head/><body><p>Confidence level</p></body></html>")
        self.KaiConfidenceLabel.setTextFormat(QtCore.Qt.RichText)
        self.KaiConfidenceLabel.setScaledContents(False)
        self.KaiConfidenceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.KaiConfidenceLabel.setObjectName("KaiConfidenceLabel")
        self.KaiIndependentBox = QtWidgets.QLineEdit(self.KaiTab)
        self.KaiIndependentBox.setGeometry(QtCore.QRect(20, 290, 61, 21))
        self.KaiIndependentBox.setObjectName("KaiIndependentBox")
        self.KaiEqualLabel = QtWidgets.QLabel(self.KaiTab)
        self.KaiEqualLabel.setGeometry(QtCore.QRect(90, 290, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.KaiEqualLabel.setFont(font)
        self.KaiEqualLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.KaiEqualLabel.setObjectName("KaiEqualLabel")
        self.Tabs.addTab(self.KaiTab, "")
        self.ProTab = QtWidgets.QWidget()
        self.ProTab.setObjectName("ProTab")
        self.ProPropagate = QtWidgets.QPushButton(self.ProTab)
        self.ProPropagate.setGeometry(QtCore.QRect(110, 320, 113, 32))
        self.ProPropagate.setObjectName("ProPropagate")
        self.layoutWidget3 = QtWidgets.QWidget(self.ProTab)
        self.layoutWidget3.setGeometry(QtCore.QRect(20, 20, 291, 291))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ProText = QtWidgets.QTextEdit(self.layoutWidget3)
        font = QtGui.QFont()
        font.setItalic(False)
        self.ProText.setFont(font)
        self.ProText.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.ProText.setObjectName("ProText")
        self.verticalLayout_3.addWidget(self.ProText)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ProFunctionLabel = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ProFunctionLabel.setFont(font)
        self.ProFunctionLabel.setTextFormat(QtCore.Qt.AutoText)
        self.ProFunctionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ProFunctionLabel.setObjectName("ProFunctionLabel")
        self.verticalLayout_2.addWidget(self.ProFunctionLabel)
        self.ProFunctionBox = QtWidgets.QLineEdit(self.layoutWidget3)
        self.ProFunctionBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ProFunctionBox.setObjectName("ProFunctionBox")
        self.verticalLayout_2.addWidget(self.ProFunctionBox)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.ProVariableNameLabel = QtWidgets.QLabel(self.layoutWidget3)
        self.ProVariableNameLabel.setObjectName("ProVariableNameLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ProVariableNameLabel)
        self.ProVariableNameBox = QtWidgets.QLineEdit(self.layoutWidget3)
        self.ProVariableNameBox.setObjectName("ProVariableNameBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ProVariableNameBox)
        self.ProSymbolicNameLabel = QtWidgets.QLabel(self.layoutWidget3)
        self.ProSymbolicNameLabel.setObjectName("ProSymbolicNameLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.ProSymbolicNameLabel)
        self.ProSymbolicNameBox = QtWidgets.QLineEdit(self.layoutWidget3)
        self.ProSymbolicNameBox.setObjectName("ProSymbolicNameBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ProSymbolicNameBox)
        self.ProVariableUnitsLabel = QtWidgets.QLabel(self.layoutWidget3)
        self.ProVariableUnitsLabel.setObjectName("ProVariableUnitsLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.ProVariableUnitsLabel)
        self.ProVariableUnitsBox = QtWidgets.QLineEdit(self.layoutWidget3)
        self.ProVariableUnitsBox.setObjectName("ProVariableUnitsBox")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ProVariableUnitsBox)
        self.verticalLayout_3.addLayout(self.formLayout_2)
        self.Tabs.addTab(self.ProTab, "")
        self.layoutWidget4 = QtWidgets.QWidget(ProjectMaker)
        self.layoutWidget4.setGeometry(QtCore.QRect(20, 10, 331, 23))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ProjectNameLabel = QtWidgets.QLabel(self.layoutWidget4)
        self.ProjectNameLabel.setObjectName("ProjectNameLabel")
        self.horizontalLayout.addWidget(self.ProjectNameLabel)
        self.ProjectNameBox = QtWidgets.QLineEdit(self.layoutWidget4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ProjectNameBox.setFont(font)
        self.ProjectNameBox.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.ProjectNameBox.setAutoFillBackground(False)
        self.ProjectNameBox.setClearButtonEnabled(False)
        self.ProjectNameBox.setObjectName("ProjectNameBox")
        self.ProjectNameBox.setText('/Users/suser/Desktop/New')
        self.horizontalLayout.addWidget(self.ProjectNameBox)
        self.actionSave = QtWidgets.QAction(ProjectMaker)
        self.actionSave.setObjectName("actionSave")


        #self.retranslateUi(ProjectMaker)
        #self.Tabs.setCurrentIndex(4)
        self.retranslateUi(ProjectMaker)
        #self.DirectoryCkeck(ProjectMaker)
        self.Tabs.setCurrentIndex(0)
        # Setting up actions of GUI. ##########################################
        self.AddSave.clicked.connect(self.AddSaveButton)
        self.AddImport.clicked.connect(self.AddImportButton)
        self.AddClear.clicked.connect(self.AddClearButton)
        self.ExpPreview.clicked.connect(self.ExpPreviewButton)
        self.ExpExport.clicked.connect(self.ExpExportButton)
        self.StaStatistics.clicked.connect(self.StaDoButton)
        self.Tabs.tabBarClicked.connect(self.TabsRefresh)
        self.ExpMethodSelect.activated.connect(self.handleActivated1)
        self.StaNumberVariablesSelect.activated.connect(self.handleActivated2)
        self.StaCobertureSelect.activated.connect(self.handleActivated3)
        self.ProPropagate.clicked.connect(self.ProPropagateButton)
        self.KaiTest.clicked.connect(self.KaySqrButton)
        #######################################################################
        QtCore.QMetaObject.connectSlotsByName(ProjectMaker)
        ProjectMaker.setTabOrder(self.ProjectNameBox, self.AddVariableNameBox)
        ProjectMaker.setTabOrder(self.AddVariableNameBox, self.AddSymbolicNameBox)
        ProjectMaker.setTabOrder(self.AddSymbolicNameBox, self.AddVariableUnitsBox)
        ProjectMaker.setTabOrder(self.AddVariableUnitsBox, self.AddDataTable)
        ProjectMaker.setTabOrder(self.AddDataTable, self.AddSave)
        ProjectMaker.setTabOrder(self.AddSave, self.AddClear)
        ProjectMaker.setTabOrder(self.AddClear, self.AddImport)
        ProjectMaker.setTabOrder(self.AddImport, self.ExpMethodSelect)
        ProjectMaker.setTabOrder(self.ExpMethodSelect, self.ExpVariableSelect)
        ProjectMaker.setTabOrder(self.ExpVariableSelect, self.ExpCaptionBox)
        ProjectMaker.setTabOrder(self.ExpCaptionBox, self.ExpPreview)
        ProjectMaker.setTabOrder(self.ExpPreview, self.ExpExport)
        ProjectMaker.setTabOrder(self.ExpExport, self.StaDataTable)
        ProjectMaker.setTabOrder(self.StaDataTable, self.StaNumberVariablesSelect)
        ProjectMaker.setTabOrder(self.StaNumberVariablesSelect, self.StaVariableSelect)
        ProjectMaker.setTabOrder(self.StaVariableSelect, self.StaCobertureSelect)
        ProjectMaker.setTabOrder(self.StaCobertureSelect, self.StaStatistics)
        ProjectMaker.setTabOrder(self.StaStatistics, self.StaCsvCopy)
        ProjectMaker.setTabOrder(self.StaCsvCopy, self.StaTexCopy)
        ProjectMaker.setTabOrder(self.StaTexCopy, self.ProPropagate)
        ProjectMaker.setTabOrder(self.ProPropagate, self.ProText)
        ProjectMaker.setTabOrder(self.ProText, self.ProFunctionBox)
        ProjectMaker.setTabOrder(self.ProFunctionBox, self.ProVariableNameBox)
        ProjectMaker.setTabOrder(self.ProVariableNameBox, self.ProSymbolicNameBox)
        ProjectMaker.setTabOrder(self.ProSymbolicNameBox, self.ProVariableUnitsBox)
        ProjectMaker.setTabOrder(self.ProVariableUnitsBox, self.Tabs)
        ProjectMaker.setTabOrder(self.Tabs, self.KaiParameterTable)

    def retranslateUi(self, ProjectMaker):
        _translate = QtCore.QCoreApplication.translate
        ProjectMaker.setWindowTitle(_translate("ProjectMaker", "Project Maker"))
        # Setting up rows label. ##############################################
        for l in range(0, DefaultNumberOfRows):
            item = self.AddDataTable.verticalHeaderItem(l)
            item.setText(_translate("Form", str(l + 1)))
        #######################################################################
        item = self.AddDataTable.horizontalHeaderItem(0)
        item.setText(_translate("ProjectMaker", "Data"))
        item = self.AddDataTable.horizontalHeaderItem(1)
        item.setText(_translate("ProjectMaker", "Uncertainty"))
        self.AddVariableNameLabel.setText(_translate("ProjectMaker", "Variable Name"))
        self.AddSymbolicNameLabel.setText(_translate("ProjectMaker", "Symbolic Name"))
        self.AddVariableUnitsLabel.setText(_translate("ProjectMaker", "Variable Units"))
        self.AddSave.setText(_translate("ProjectMaker", "Save"))
        self.AddImport.setText(_translate("ProjectMaker", "Import"))
        self.AddClear.setText(_translate("ProjectMaker", "Clear"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.AddTab), _translate("ProjectMaker", "Add"))
        self.ExpMethodSelect.setItemText(0, _translate("ProjectMaker", "LaTeX - default uncertainties"))
        self.ExpMethodSelect.setItemText(1, _translate("ProjectMaker", "LaTeX - simple brackets"))
        self.ExpMethodSelect.setItemText(2, _translate("ProjectMaker", "Wolfram"))
        self.ExpVariableSelect.setSortingEnabled(True)
        self.ExpCaptionBox.setText(_translate("ProjectMaker", "Caption to TeX export"))
        self.ExpPreview.setText(_translate("ProjectMaker", "Preview"))
        self.ExpExport.setText(_translate("ProjectMaker", "Export"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.ExpTab), _translate("ProjectMaker", "Exporter"))
        self.StaNumberVariablesSelect.setItemText(0, _translate("ProjectMaker", "Direct measures"))
        self.StaNumberVariablesSelect.setItemText(1, _translate("ProjectMaker", "Indirect measures"))
        self.StaVariableSelect.setSortingEnabled(True)
        self.StatCobertureLabel.setText(_translate("ProjectMaker", "Coberture factor"))
        self.StaCobertureSelect.setItemText(0, _translate("ProjectMaker", "Gaussian 68%"))
        self.StaCobertureSelect.setItemText(1, _translate("ProjectMaker", "Gaussian 95%"))
        self.StaCobertureSelect.setItemText(2, _translate("ProjectMaker", "Gaussian 99%"))
        self.StaCobertureSelect.setItemText(3, _translate("ProjectMaker", "Student 70%"))
        self.StaCobertureSelect.setItemText(4, _translate("ProjectMaker", "Student 95%"))
        self.StaCobertureSelect.setItemText(5, _translate("ProjectMaker", "Student 99%"))
        self.StaCobertureSelect.setItemText(6, _translate("ProjectMaker", "Other Percentile"))
        self.StaStatistics.setText(_translate("ProjectMaker", "Do statistics"))
        self.StaCsvCopy.setText(_translate("ProjectMaker", "Copy csv format"))
        self.StaTexCopy.setText(_translate("ProjectMaker", "Copy TeX format"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.StaTab), _translate("ProjectMaker", "Stat"))
        item = self.KaiParameterTable.verticalHeaderItem(0)
        item.setText(_translate("ProjectMaker", "1"))
        item = self.KaiParameterTable.verticalHeaderItem(1)
        item.setText(_translate("ProjectMaker", "2"))
        item = self.KaiParameterTable.verticalHeaderItem(2)
        item.setText(_translate("ProjectMaker", "3"))
        item = self.KaiParameterTable.verticalHeaderItem(3)
        item.setText(_translate("ProjectMaker", "4"))
        item = self.KaiParameterTable.verticalHeaderItem(4)
        item.setText(_translate("ProjectMaker", "5"))
        item = self.KaiParameterTable.verticalHeaderItem(5)
        item.setText(_translate("ProjectMaker", "6"))
        item = self.KaiParameterTable.verticalHeaderItem(6)
        item.setText(_translate("ProjectMaker", "7"))
        item = self.KaiParameterTable.verticalHeaderItem(7)
        item.setText(_translate("ProjectMaker", "8"))
        item = self.KaiParameterTable.verticalHeaderItem(8)
        item.setText(_translate("ProjectMaker", "9"))
        item = self.KaiParameterTable.horizontalHeaderItem(0)
        item.setText(_translate("ProjectMaker", "Parameter"))
        item = self.KaiParameterTable.horizontalHeaderItem(1)
        item.setText(_translate("ProjectMaker", "Value"))
        self.KaiFunctionLabel.setText(_translate("ProjectMaker", "Function"))
        self.KaiTest.setText(_translate("ProjectMaker", "χ2 Test"))
        self.KaiSqrLabel.setHtml(_translate("ProjectMaker", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times\'; font-size:48pt; font-style:italic; color:#252525;\">χ</span><span style=\" font-family:\'Times\'; font-size:48pt; font-style:italic; color:#252525; vertical-align:super;\">2</span></p></body></html>"))
        self.KaiConfidenceBox.setText(_translate("ProjectMaker", "0.95"))
        self.KaiEqualLabel.setText(_translate("ProjectMaker", "="))
        self.Tabs.setTabText(self.Tabs.indexOf(self.KaiTab), _translate("ProjectMaker", "KaiSqr"))
        self.ProPropagate.setText(_translate("ProjectMaker", "Propagate"))
        self.ProText.setHtml(_translate("ProjectMaker", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The use of universal <span style=\" font-weight:600;\">pysical constants</span> is permmited. But it is important to know thei names blabala</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">h </span>= 6.6 x 10<span style=\" vertical-align:super;\">-34</span></p></body></html>"))
        self.ProFunctionLabel.setText(_translate("ProjectMaker", "Function"))
        self.ProVariableNameLabel.setText(_translate("ProjectMaker", "Variable Name"))
        self.ProSymbolicNameLabel.setText(_translate("ProjectMaker", "Symbolic Name"))
        self.ProVariableUnitsLabel.setText(_translate("ProjectMaker", "Variable Units"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.ProTab), _translate("ProjectMaker", "Propagator"))
        self.ProjectNameLabel.setText(_translate("ProjectMaker", "Project Name:"))
        self.actionSave.setText(_translate("ProjectMaker", "Save"))

##########################################################################################



##########################################################################################
# Coberture factor input dialog. #########################################################

    def CobertureDialog(self,ProjectMaker):
        text, ok = QInputDialog.getText(ProjectMaker, 'Coberture factor',
                                        'Enter the desired coberture factor:')

        if ok:
            factor = float(text)
        return factor

##########################################################################################



##########################################################################################
# Directory checking and name functions. #################################################

    def DirectoryCkeck(self):
        print('# Checking directories...')
        print('  ' + str(self.ProjectNameBox.text()))
        if os.path.exists(str(self.ProjectNameBox.text())):
            print('  Your project exists! Start working.')
        else:
            print('  Setting up a new project.')
            os.makedirs(str(self.ProjectNameBox.text()))
            os.makedirs(str(self.ProjectNameBox.text()) + '/otr')
            os.makedirs(str(self.ProjectNameBox.text()) + '/gpx')
            os.makedirs(str(self.ProjectNameBox.text()) + '/bib')
            #os.makedirs(str(self.ProjectNameBox.text()) + '/cpr')
            os.makedirs(str(self.ProjectNameBox.text()) + '/dat')
            os.makedirs(str(self.ProjectNameBox.text()) + '/dat/DataBackUp')

    def DirectoryName(self):
        projectpath = str(self.ProjectNameBox.text()) + '/dat/'
        return projectpath

##########################################################################################



##########################################################################################
# Add Data Assistant functions in buttons. ###############################################

    ###############################################################################

    def AddSaveButton(self):
        print(' ')
        cprint("  Adding new variables                             " + sectspa,\
               'white', 'on_blue', attrs=['bold'], file=sys.stderr)
        self.DirectoryCkeck()
        ppath = self.DirectoryName()

        # Load Table
        rows = self.AddDataTable.rowCount();
        null = 0;
        DAT = np.zeros(rows, );
        UNC = np.zeros(rows, )
        for l in range(0, rows):
            if self.AddDataTable.item(l, 0) is None:
                null = null + 1
            else:
                try:
                    try:
                        DAT[l - null] = float(self.AddDataTable.item(l, 0).text())
                        UNC[l - null] = float(self.AddDataTable.item(l, 1).text())
                    except ValueError:
                        null = null + 1
                except AttributeError:
                    null = null + 1

        print('# Reading new data.')
        print('  Data correctly imported.')
        DAT = np.delete(DAT, np.s_[l - null + 1::], 0)
        print('  Uncertainty correctly imported.')
        UNC = np.delete(UNC, np.s_[l - null + 1::], 0)
        print('  Name, symbol and units correctly imported.')
        NAM = str(self.AddVariableNameBox.text())
        SYM = str(self.AddSymbolicNameBox.text())
        UNI = str(self.AddVariableUnitsBox.text())

        # Save
        print('# Checking previous database and storing new variable.')
        DIC = {'sym': SYM, 'uni': UNI, 'dat': DAT, 'unc': UNC}
        StoreVar(DIC, str(NAM), ppath, 'Data')

    ###############################################################################

    ###############################################################################

    def AddImportButton(self):
        print('Not working yet. Sorry :(.')

    ###############################################################################

    ###############################################################################

    def AddClearButton(self):
        for l in range(0, DefaultNumberOfRows):
            self.AddDataTable.setItem(l, 0, QTableWidgetItem())
            self.AddDataTable.setItem(l, 1, QTableWidgetItem())

    ###############################################################################

##########################################################################################



##########################################################################################
# Export #################################################################################

    ###############################################################################

    def handleActivated1(self, index):
        global mode1
        #print(self.ExporterMethodSelect.itemText(index))
        #print(self.ExporterMethodSelect.itemData(index))
        mode1 = self.ExpMethodSelect.itemData(index)

    ###############################################################################

    ###############################################################################

    def ExpExportButton(self):
        cprint("  Export                                           " + sectspa, \
               'white', 'on_blue', attrs=['bold'], file=sys.stderr)
        ppath = self.DirectoryName()
        CAP = self.ExpCaptionBox.text()

        # Starting up loading variables and creating correct MAT dimensional matrix.
        items = self.ExpReadSelect()
        print('# Importing database variables.')
        Data = LoadVar(ppath, database)

        # Checking dimensions.
        aux1 = 0
        for l in range(0,len(items)):
            aux1 = max(len(Data[items[l]]['dat']),aux1)

        MAT = np.zeros([aux1,2*len(items)],); SYM = []; UNI = []

        # Writing data and uncertainty into MAT.
        for n in range(0, 2*len(items),2):
            DAT = Data[items[int(n/2)]]['dat']; UNC = Data[items[int(n/2)]]['unc']
            MAT[0:(len(DAT)), [n-0]] = DAT[:, np.newaxis]
            MAT[0:(len(UNC)), [n+1]] = UNC[:, np.newaxis]
            SYM.append(Data[items[int(n/2)]]['sym'])
            UNI.append(Data[items[int(n/2)]]['uni'])

        # Finishing.
        if mode1 == 1:
            print('# Exporting table to export_TeX in +/- notation.')
            TableToTeX(MAT,CAP,SYM,UNI,ppath)
        elif mode1 == 2:
            print('# Exporting table to export_TeX in (··) notation.')
            TableToTeX(MAT, CAP, SYM, UNI, ppath)
        else:
            print('# Exporting table to export_WMA.')
            WolframEx(MAT, CAP, SYM, UNI, ppath)

    ###############################################################################

    ###############################################################################

    def ExpPreviewButton(self):
        cprint("  Preview table                                    " + sectspa, \
               'white', 'on_blue', attrs=['bold'], file=sys.stderr)
        ppath = self.DirectoryName()
        CAP = self.ExpCaptionBox.text()

        # Starting up loading variables and creating correct MAT dimensional matrix.
        items = self.ExpReadSelect()
        Data = LoadVar(ppath, database)

        # Checking dimensions.
        aux1 = 0
        for l in range(0, len(items)):
            aux1 = max(len(Data[items[l]]['dat']), aux1)

        MAT = np.zeros([aux1, 2 * len(items)], ); SYM = []; UNI = []

        # Writing data and uncertainty into MAT.
        for n in range(0, 2 * len(items), 2):
            DAT = Data[items[int(n / 2)]]['dat'];
            UNC = Data[items[int(n / 2)]]['unc'];
            MAT[0:(len(DAT)), [n - 0]] = DAT[:, np.newaxis]
            MAT[0:(len(UNC)), [n + 1]] = UNC[:, np.newaxis]
            SYM.append(Data[items[int(n / 2)]]['sym'])
            UNI.append(Data[items[int(n / 2)]]['uni'])

        PreviewTableTeX(MAT, CAP, SYM, UNI, ppath)

    ###############################################################################

    def ExpReadSelect(self):
        itemsList = self.ExpVariableSelect.selectedItems()
        selection = []
        # Reading all selected items.
        for item in itemsList:
            selection.append(item.text())
        return selection

    ###############################################################################

##########################################################################################



##########################################################################################
# Load variables in Exporter List ########################################################

    def TabsRefresh(self):

        self.DirectoryCkeck()
        ppath = self.DirectoryName()
        Data = LoadVar(ppath, database)

        # Showing aceptable variables.
        self.ExpVariableSelect.clear()
        self.StaVariableSelect.clear()
        for l in range(0,len(Data.keys())):
            self.ExpVariableSelect.addItem(list(Data.keys())[l])
            self.StaVariableSelect.addItem(list(Data.keys())[l])

        # Reseting selection and sorting.
        self.ExpVariableSelect.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.StaVariableSelect.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.ExpVariableSelect.setSortingEnabled(True)
        self.StaVariableSelect.setSortingEnabled(True)

##########################################################################################

    ###############################################################################

    def handleActivated2(self, index):
        global mode2
        #print(self.ExporterMethodSelect.itemText(index))
        #print(self.ExporterMethodSelect.itemData(index))
        mode2 = self.StaNumberVariablesSelect.itemData(index)

    def handleActivated3(self, index):
        global mode3
        #print(self.ExporterMethodSelect.itemText(index))
        #print(self.ExporterMethodSelect.itemData(index))
        mode3 = self.StaCobertureSelect.itemData(index)

    ###############################################################################

    def StaDoButton(self):
        print('')
        cprint("  Statistical mean                                 " + sectspa, \
               'white', 'on_blue', attrs=['bold'], file=sys.stderr)
        ppath = self.DirectoryName()

        try:
            # Loading variables and creating correct MAT dimensional matrix.
            items = self.StaReadSelect()
            Data = LoadVar(ppath, database)

            # Checking dimensions.
            aux1 = 0
            for k in range(0, len(items)):
                aux1 = aux1 + len(Data[items[k]]['dat'])

            MAT = np.zeros([aux1, 2], )
            SYM = Data[items[0]]['sym']; UNI = Data[items[0]]['uni']

            # Writing data and uncertainty into MAT.
            aux2 = 0
            for l in range(0, len(items)):
                DAT = Data[items[int(l)]]['dat']
                UNC = Data[items[int(l)]]['unc']
                MAT[aux2:(len(DAT)+aux2), [0]] = DAT[:, np.newaxis]
                MAT[aux2:(len(DAT)+aux2), [1]] = UNC[:, np.newaxis]
                aux2 = aux2 + len(DAT)
            aux3 = aux2

            # Printing data in table.
            self.StaDataTable.setRowCount(aux2)
            for n in range(0,aux2):
                self.StaDataTable.setItem(n,0,QTableWidgetItem(str(MAT[n,[0]][0])))


            # Variable mean - Direct measurements.
            if mode2 == 1:

                # Setting up coberture factor.
                if mode3==1:
                    factor = stats.norm.ppf(1-(1-.68)/2)
                elif mode3==2:
                    factor = stats.norm.ppf(1-(1-.95)/2)
                elif mode3==3:
                    factor = stats.norm.ppf(1-(1-0.99)/2)
                elif mode3==4:
                    factor = stats.t.ppf(1-(1-0.70)/2, aux3)
                elif mode3==5:
                    factor = stats.t.ppf(1-(1-0.95)/2, aux3)
                elif mode3==6:
                    factor = stats.t.ppf(1-(1-0.99)/2, aux3)
                elif mode3==7:
                    try:
                        factor = self.CobertureDialog(ProjectMaker)
                    except:
                        factor = 2
                        print('  Coberture factor was not provided.'
                              ' Continuing with default one.')
                else:
                    print('  Invalid Mode!')

                if aux3 > 20:
                    print('  DOF is ' + str(aux3) + ', so gaussian approximation is'
                                                    ' valid.')
                else:
                    print('  DOF is ' + str(aux3) + ', you should use t-Student'
                                                    ' percentiles.')
                print('  Current coberture factor is ' + str(factor) + '.')
                dat = abs(MAT[:, [0]]); uBd = abs(MAT[:, [1]])

                # Check if it is necesary to ponderate.
                weights = 0
                for n in range(0,len(uBd)-1):
                    if uBd[n] != uBd[n+1]:
                        weights = 1

                # Mean and elimination.
                if weights==0:
                    print('  All data have the same uncentainty, mean is no weighted.')
                    daM = np.mean(dat); lda = len(dat)
                    dMv = np.mean(daM)*np.ones([lda, 1],)
                    uAs = np.sqrt((sum((dat - dMv)**(2))/(lda - 1)))
                else:
                    print('  Statitiscal mean is weighted due to different precisions.')
                    daM = sum(dat/(uBd**2))/sum(1/(uBd**2)); lda = len(dat)
                    dMv = np.mean(daM) * np.ones([lda, 1], )
                    uAs = np.sqrt((uBd*sum((dat - dMv) ** (2)) / (lda - 1)))

                dol = dMv + factor * uAs; upl = dMv - factor * uAs
                dNA = dat[(dat  > dol) | (dat  < upl)]
                dOK = dat[(dat <= dol) & (dat >= upl)]
                dNA = np.sort(dNA); lNA = len(dNA); lOK = len(dOK)
                print('  ' + str(lNA) + ' values out of the confidence interval.')

                # Mean with all good measurements.
                if lOK !=0:
                    if weights == 0:
                        daOKm = float(np.mean(dOK))
                        daOKv = np.mean(daOKm)*np.ones([lOK, 1],)
                        uAOKs = np.sqrt((np.sum((dOK - daOKv)**(2))/(lOK - 1)))
                        uAOKm = uAOKs/np.sqrt(lOK)
                        uCOKd = float(factor*np.sqrt(uAOKm**2+sum(uBd[0])**2))
                        UncPrint(daOKm,uCOKd)
                    else:
                        daOKm = float(sum(dat/(uBd**2))/sum(1/(uBd**2)))
                        uAOKm = 1/np.sqrt(sum(1/(uBd**2)))
                        uCOKd = float(factor*np.sqrt(uAOKm[0]**2))
                        UncPrint(daOKm,uCOKd)
                else:
                    print('  All your data is out of the confidence interval.')
                    print('  Very poor quality measurements. Try incrementing coberture.')

                """
                out1 = sprintf(...
                '$%s = ( %.1f \\pm %.1f ) \\times 10^{%i} \\ \\mathrm{%s}$\n', ...
                var, VAR, uni);

                if LRene~=0
                out2 = [sprintf(['Empregando un factor de cobertura \n'...
                                 'k=%.3f existen %i medidas fÛra do \n'...
                                 'intervalo que nos oferta a desviaciÛn\n'...
                                 'tÌpica da mostra. Os valores dos que\n'...
                                 'nos desfacemos son:'], factor, LRene)...
                            sprintf('\n%s', num2str(dataVALID0'))...
                        sprintf('.\n(vÈxase saÌda Statistic.txt)')]
                else
                out2 = [sprintf(['Empregando un factor de cobertura \n'...
                                 'k=%.3f, non houbo medidas fÛra do inter-\n'...
                                 'valo de confianza da mostra'], factor)...
                            sprintf('.\n(vÈxase saÌda Statistic.txt)')]
                end

                fid = fopen(['Statistic.txt'], 'a');
                fprintf(fid, '\n')
                fprintf(fid, '\nA desviaciÛn tÌpica da mostra\n')
                fprintf(fid, '\\[u_A(%s)=\\sqrt{\\frac{\\sum_{i=1}^n (%s ^i - \\langle %s \\rangle)^2}{n-1}}= %.2f \\] \n',
                        var, var, var, uASAMPLE)
                fprintf(fid, '\nA desviaciÛn tÌpica da media\n')
                fprintf(fid, '\\[u_A(\\langle %s \\rangle) = \\frac{u_A(%s)}{\\sqrt{n}}= %.2f \\] \n', var, var, uAMEAN)
                fprintf(fid, '\nA incerteza combinada\n')
                fprintf(fid,
                        '\\[u_C(\\langle %s \\rangle) = \\kappa \\sqrt{u^2_B(%s) + u^2_A(\\langle %s \\rangle)}= %.1f \\]\n',
                        var, var, var, uMEAN)
            """
            # Mean of several variables - Indirect measurements.
            elif mode2 == 2:

                # Creating the function of sum.
                FUN = '('; NAM = ''
                for o in range(0,len(items)):
                    if o == int(len(items)-1):
                        FUN = FUN + Data[items[int(o)]]['sym'] + ')/' + str(aux3)
                        NAM = NAM + Data[items[int(o)]]['sym']
                    else:
                        FUN = FUN + Data[items[int(o)]]['sym'] + '+'
                        NAM = NAM + Data[items[int(o)]]['sym'] + '_'
                print('  Function ' + FUN + ' is going to be propagated within PPDDM.')

                # Parsing and selecting variable dependencies.
                fun = parse_expr(FUN, transformations=transformations)
                listvar = list(VariableExtractor(FUN))
                v = {}; f = {}; f['fun'] = FUN; d = {}
                for p in range(0, len(listvar)):
                    v[listvar[p]] = sp.symbols(listvar[p])

                # Reading required data values.
                for q in range(0, len(listvar)):
                    for r in range(0, len(Data)):
                        if Data[list(Data.keys())[r]]['sym'] == list(v.keys())[q]:
                            d[list(v.keys())[q]] = Data[list(Data.keys())[r]]

                # Expression of U, total uncertainty of the function.
                c = len(listvar); U = sp.symbols('U'); U = 0; u = sp.symbols('u')
                for s in range(0, c):
                    if d[list(v.keys())[s]]['unc'][0] != 0:
                        U = U + (sp.diff(f['fun'], v[list(v.keys())[s]])) ** 2 * \
                                (u(v[list(v.keys())[s]])) ** 2
                f['ufn'] = sp.simplify(U); del U; f['fun'] = sp.simplify(fun)

                # Eval function all over the data.
                dat = MAT[:, [0]]; uBd = MAT[:, [1]]
                f['dat'] = float(sum(sum(dat))/aux3)
                f['unc'] = float(np.sqrt((1/(aux3**2))*sum(sum(uBd**2))))
                UncPrint(f['dat'],f['unc'])

                # Creating the new variable.
                NAM = 'mean_' + NAM
                print('  New variable was created: ' + NAM)
                SYM = '\\langle ' + SYM + ' \\rangle'
                NEW = {'dat': np.array([f['dat']]), 'unc': np.array([f['unc']])}
                NEW['sym'] = SYM; NEW['uni'] = UNI
                StoreVar(NEW, NAM, ppath, 'Data')

                with open(ppath + 'Statistics' + '.txt', 'a') as aux:
                    aux.write(separ + 'x' + separ + '\n\n')
                    aux.write('No que segue propagamos os datos de $' + SYM + '$')
                    aux.write(',\n\\[ ' + SYM + ' = ' + sp.latex(f['fun']) + ' \\],\n')
                    aux.write('mediante o método de derivadas parciais coa expresión\n')
                    aux.write('\\[u^2(' + SYM + ')=' + sp.latex(f['ufn']) + '\\]')
                    aux.write('\nObtemos, xa que logo, os seguintes resultados:\n')
            # Error case
            else:
                print('  Invalid Mode!')
        except:
            print('  Cannot finish the job! Maybe you missselected the variables.')

    ###############################################################################

    def StaReadSelect(self):
        itemsList = self.StaVariableSelect.selectedItems()
        selection = []
        # Reading all selected items.
        for item in itemsList:
            selection.append(item.text())
        return selection

    ###############################################################################

##########################################################################################



##########################################################################################
# Uncertainty propagator. ################################################################

    def ProPropagateButton(self):
        print('')
        cprint("  Uncertainty propagator                           " + sectspa, \
               'white', 'on_blue', attrs=['bold'], file=sys.stderr)
        ppath = self.DirectoryName()
        FUN = str(self.ProFunctionBox.text())
        fun = parse_expr(FUN, transformations=transformations)
        NAM = str(self.ProVariableNameBox.text())
        SYM = str(self.ProSymbolicNameBox.text())
        UNI = str(self.ProVariableUnitsBox.text())

        listvar = list(VariableExtractor(FUN))
        v = {}; f = {}; f['fun'] = FUN; d = {}
        for k in range(0, len(listvar)):
            v[listvar[k]] = sp.symbols(listvar[k])

        # Leo Data
        Data = LoadVar(ppath, 'Data')
        for l in range(0, len(listvar)):
            for m in range(0, len(Data)):
                if Data[list(Data.keys())[m]]['sym'] == list(v.keys())[l]:
                    d[list(v.keys())[l]] = Data[list(Data.keys())[m]]

        # Expression of U, total uncertainty of the function
        c = len(listvar); U = sp.symbols('U'); U = 0; u = sp.symbols('u')
        for n in range(0, c):
            if d[list(v.keys())[n]]['unc'][0] != 0:
                U = U + (sp.diff(f['fun'], v[list(v.keys())[n]])) ** 2 * \
                        (u(v[list(v.keys())[n]])) ** 2
        f['ufn'] = sp.simplify(U); del U; f['fun'] = fun

        # Eval function all over the data.
        f['dat'] = np.zeros(len(d[list(v.keys())[0]]['dat']), )
        f['unc'] = np.zeros(len(d[list(v.keys())[0]]['dat']), )

        for p in range(0, len(f['dat'])):
            aux1 = {}; aux2 = {}
            for o in range(0, c):
                aux1[v[list(v.keys())[o]]] = d[list(v.keys())[o]]['dat'][p]
                aux2[u(v[list(v.keys())[o]])] = d[list(v.keys())[o]]['unc'][p]
            f['dat'][p] = float(f['fun'].subs(aux1))
            aux3 = f['ufn'].subs(aux2)
            f['unc'][p] = np.sqrt(float(aux3.subs(aux1)))

        # Creating the new variable.
        NEW = {'dat': f['dat'], 'unc': f['unc'], 'sym': SYM, 'uni': UNI}
        StoreVar(NEW, NAM, ppath, 'Data')

        with open(ppath + 'Propagator' + '.txt', 'a') as aux:
            aux.write('\n' + separ + 'x' + separ + '\n\n')
            aux.write('No que segue propagamos os datos de $' + SYM + '$')
            aux.write(',\n\\[ ' + SYM + ' = ' + sp.latex(f['fun']) + ' \\],\n')
            aux.write('mediante o método de derivadas parciais coa expresión\n')
            aux.write('\\[u^2(' + SYM + ')=' + sp.latex(f['ufn']) + '\\]')
            aux.write('\nObtemos, xa que logo, os seguintes resultados:')

##########################################################################################




##########################################################################################
# Test de KaiSqr. ########################################################################

    def KaySqrButton(self):
        print('')
        cprint("  KaiSqr hypothesis test                           " + sectspa, \
               'white', 'on_blue', attrs=['bold'], file=sys.stderr)
        ppath = self.DirectoryName()

        # PHASE 1 - Subs parameter values in FUN
        FUN = str(self.KaiDependentBox.text())
        fun = parse_expr(FUN, transformations=transformations); f={}; f['fun'] = fun
        print(f)
        # Reading parameters (b).
        rows = self.KaiParameterTable.rowCount(); null = 0; b = {}
        for l in range(0, rows):
            if self.KaiParameterTable.item(l, 0) is None:
                null = null + 1
            else:
                try:
                    try:
                        b[str(self.KaiParameterTable.item(l, 0).text())] = float(
                            self.KaiParameterTable.item(l, 1).text())
                    except ValueError:
                        null = null + 1
                except AttributeError:
                    null = null + 1
        print(b) #OK
        FUN = str(f['fun'].subs(b))
        print(f['fun'].subs(b))
        print(FUN)
        print('aqui')
        AUX = list(VariableExtractor(FUN))
        YFN = str(self.KaiIndependentBox.text())
        FUN = '(' + YFN + '-(' + FUN + '))'
        fun = parse_expr(FUN, transformations=transformations); print(fun)

        listvar = list(VariableExtractor(FUN))
        v = {}; f = {}; f['fun'] = FUN; d = {}
        for k in range(0, len(listvar)):
            v[listvar[k]] = sp.symbols(listvar[k])

        # Reading Data.
        try:
            Data = LoadVar(ppath, 'Data')
            for l in range(0, len(listvar)):
                for m in range(0, len(Data)):
                    if Data[list(Data.keys())[m]]['sym'] == list(v.keys())[l]:
                        d[list(v.keys())[l]] = Data[list(Data.keys())[m]]

            # Expression of U, total uncertainty of the function
            c = len(listvar); f['fun'] = fun; print(f['fun'])

            # Eval function all over the data.
            f['dat'] = np.zeros(len(d[list(v.keys())[0]]['dat']), )
        except:
            print('Error loading database. Check its existence.')

        try:
            for p in range(0, len(f['dat'])):
                aux1 = {}; aux2 = {}
                for o in range(0, c):
                    aux1[v[list(v.keys())[o]]] = d[list(v.keys())[o]]['dat'][p]
                f['dat'][p] = float(f['fun'].subs(aux1))
        except:
            print('# Something went wrong, maybe array sizes? Check that, and try again.')
            print('  Following results may not be correct because of data error.')
        print(f)
        try:
            rKai = sum((f['dat']/d[YFN]['unc'])**2); cl = float(self.KaiConfidenceBox.text()); print(rKai)
            pKai = stats.chi2.ppf(cl,len(f['dat'])-len(b.keys()))
            print('  Testing at ' + str(cl) + 'confidence level.')
            with open(ppath + 'KaiSqr' + '.txt', 'a') as aux:
                aux.write('\n' + separ + 'x' + separ + '\n\n')
                aux.write('Non obstante, cómpre ver mediante, por exemplo, un test--')
                aux.write('$\\chi ^2$, que o axuste é satisfactorio. Para iso imos ')
                aux.write('supoñer que os nosos puntos se axustan a $' + str(YFN) + ' = f(')
                aux.write(str(AUX[0]) + ')$ para o conxunto $\\lbrace ' + str(AUX[0]) + '_i,')
                aux.write(str(YFN) + '_i \\rbrace _{i=1}^n$ dos nosos ' + str(len(f['dat'])))
                aux.write(' valores, e que a distribución nai das medidas $' + str(YFN) + '$')
                aux.write(' é gaussiana, posto que en xeral esta é a distribución que ')
                aux.write('goberna os procesos de medida. Daquela é esperable que \n')
                aux.write('\\[z_i = \\frac{' + str(YFN) + ' _i -\\bar{' + str(YFN) + ' _i }}')
                aux.write('{\\sigma_i}\\] \n sexa $z_i \in N(0,1)$ de tal modo que podemos ')
                aux.write('agardar que, \n \\[\\chi ^2 = \\sum_{i=1}^n \\frac{(' + str(YFN))
                aux.write('_i -\\bar{' + str(YFN) + '}_i)^2}{\\sigma_i^2} \\] \n')
                aux.write('responda a unha distribución $\chi^2$ de Pearson. Asumimos agora ')
                aux.write('que, a primeira orde, os valores que medimos DE ALGO ')
                aux.write('coinciden coas predicións da lei teórica e polo tanto é licita a ')
                aux.write('aproximación $\\bar{'+str(YFN)+'_i} \\approx f('+str(AUX[0])+')$.')
                aux.write(' Ademais, dado que temos incertezas variables nas medidas DE ')
                aux.write('ALGO, tomamos por válido que $\\sigma_i^2 \\approx u^2('+str(YFN))
                aux.write('_i )$ polo que, conseguintemente,\n\\begin{equation}\n')
                aux.write('\\chi ^2 = \\sum_{i=1}^n \\frac{(' +str(YFN)+' -f('+ str(AUX[0]))
                aux.write('))^2}{u^2(' + str(YFN) + ')}.\n \\end{equation}')

                if   rKai>=pKai:
                    print('# WARNING! Your fitting model is not a valid one.')
                    aux.write('Partimos dos ' + str(len(f['dat'])) + ' valores medidos no ')
                    aux.write('laboratorio e como temos '+str(len(b.keys()))+ ' parámetros ')
                    aux.write('que determinamos mediante o axuste, temos ao final ')
                    aux.write(str(len(f['dat'])-len(b.keys())) + ' graos de liberdade que ')
                    aux.write('gobernan a distribución de Pearson. Practicamos un test—')
                    aux.write('$\chi^2$ cun nivel de confianza de')
                    aux.write(str(float(cl)) + 'polo que empregamos o')
                    aux.write(' percentil $\chi_{' + str(1 - float(cl)))
                    aux.write(';' + str(len(f['dat']) - len(b.keys())) + '}^2$.')
                    aux.write('Se comparamos este valor co obtido coa suma de cadrados, ')
                    aux.write('concluímos que, como \n\\[ \chi_{')
                    aux.write(str(1 - float(self.KaiConfidenceBox.text())) + ';')
                    aux.write(str(len(f['dat']) - len(b.keys())) + '}^2 = ' + str(pKai) + '<')
                    aux.write(str(rKai) + '\\]\n e rexeitamos por tanto a hipótese proposta ')
                    aux.write('a este nivel de confianza \n\n COMENTAR CONCLUSIÓNS')
                elif rKai<pKai:
                    print('# Your model is OK: ' + str(rKai) + ' < ' + str(pKai))
                    aux.write('Partimos dos ' + str(len(f['dat'])) + ' valores medidos no ')
                    aux.write('laboratorio e como temos '+str(len(b.keys()))+ ' parámetros ')
                    aux.write('que determinamos mediante o axuste, temos ao final ')
                    aux.write(str(len(f['dat'])-len(b.keys())) + ' graos de liberdade que ')
                    aux.write('gobernan a distribución de Pearson. Practicamos un test—')
                    aux.write('$\chi^2$ cun nivel de confianza de ')
                    aux.write(str(cl)+' polo que empregamos ')
                    aux.write('o percentil $\chi_{'+str(1-float(cl)))
                    aux.write(';' + str(len(f['dat'])-len(b.keys())) + '}^2$.')
                    aux.write('Se comparamos este valor co obtido coa suma de cadrados, ')
                    aux.write('concluímos que, como \n\\[ \chi_{')
                    aux.write(str(1-float(self.KaiConfidenceBox.text())) +';')
                    aux.write(str(len(f['dat'])-len(b.keys()))+ '}^2 = ' + str(pKai) + '>')
                    aux.write(str(rKai) + '\\] \n a hipótese é aceptable neste nivel de ')
                    aux.write('confianza \n\n COMENTAR CONCLUSIÓNS')
        except:
            print('Error persistant. Check previous errors.')
##########################################################################################






##########################################################################################

##########################################################################################

##########################################################################################

##########################################################################################

##########################################################################################

##########################################################################################



##########################################################################################
# Start GUI window. ######################################################################

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProjectMaker = QtWidgets.QWidget()
    ui = Ui_ProjectMaker()
    ui.setupUi(ProjectMaker)
    os.system('clear')
    ProjectMaker.show()
    sys.exit(app.exec_())

##########################################################################################
