# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'header.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(841, 553)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setMargin(3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.addFilesButton = QtGui.QToolButton(Form)
        self.addFilesButton.setObjectName(_fromUtf8("addFilesButton"))
        self.horizontalLayout_2.addWidget(self.addFilesButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.filesListWidget = QtGui.QListWidget(Form)
        self.filesListWidget.setMinimumSize(QtCore.QSize(300, 0))
        self.filesListWidget.setObjectName(_fromUtf8("filesListWidget"))
        self.verticalLayout_3.addWidget(self.filesListWidget)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(3, 3, -1, -1)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.deleteButton = QtGui.QPushButton(Form)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.horizontalLayout_10.addWidget(self.deleteButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setMargin(3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.previewEdit = QtGui.QPlainTextEdit(Form)
        self.previewEdit.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.previewEdit.setObjectName(_fromUtf8("previewEdit"))
        self.verticalLayout.addWidget(self.previewEdit)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(6, 6, -1, 6)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.unitEdit = QtGui.QLineEdit(self.groupBox)
        self.unitEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.unitEdit.setObjectName(_fromUtf8("unitEdit"))
        self.horizontalLayout_3.addWidget(self.unitEdit)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_3.addWidget(self.label_11)
        self.timeUnitBox = QtGui.QComboBox(self.groupBox)
        self.timeUnitBox.setObjectName(_fromUtf8("timeUnitBox"))
        self.timeUnitBox.addItem(_fromUtf8(""))
        self.timeUnitBox.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.timeUnitBox)
        spacerItem3 = QtGui.QSpacerItem(13, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_3.addWidget(self.label_7)
        self.scaleEdit = QtGui.QLineEdit(self.groupBox)
        self.scaleEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.scaleEdit.setInputMask(_fromUtf8(""))
        self.scaleEdit.setObjectName(_fromUtf8("scaleEdit"))
        self.horizontalLayout_3.addWidget(self.scaleEdit)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_2.addWidget(self.label_6)
        self.colIndexEdit = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colIndexEdit.sizePolicy().hasHeightForWidth())
        self.colIndexEdit.setSizePolicy(sizePolicy)
        self.colIndexEdit.setMinimumSize(QtCore.QSize(250, 0))
        self.colIndexEdit.setObjectName(_fromUtf8("colIndexEdit"))
        self.verticalLayout_2.addWidget(self.colIndexEdit)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_4.addWidget(self.label_9)
        self.colNameEdit = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colNameEdit.sizePolicy().hasHeightForWidth())
        self.colNameEdit.setSizePolicy(sizePolicy)
        self.colNameEdit.setMinimumSize(QtCore.QSize(250, 0))
        self.colNameEdit.setObjectName(_fromUtf8("colNameEdit"))
        self.verticalLayout_4.addWidget(self.colNameEdit)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 2, 0, 1, 1)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_5.addWidget(self.label_8)
        self.indexColEdit = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.indexColEdit.sizePolicy().hasHeightForWidth())
        self.indexColEdit.setSizePolicy(sizePolicy)
        self.indexColEdit.setMinimumSize(QtCore.QSize(250, 0))
        self.indexColEdit.setObjectName(_fromUtf8("indexColEdit"))
        self.verticalLayout_5.addWidget(self.indexColEdit)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 3, 0, 1, 1)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_6.addWidget(self.label_10)
        self.indexFormatsEdit = QtGui.QLineEdit(self.groupBox)
        self.indexFormatsEdit.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.indexFormatsEdit.sizePolicy().hasHeightForWidth())
        self.indexFormatsEdit.setSizePolicy(sizePolicy)
        self.indexFormatsEdit.setMinimumSize(QtCore.QSize(250, 0))
        self.indexFormatsEdit.setReadOnly(True)
        self.indexFormatsEdit.setObjectName(_fromUtf8("indexFormatsEdit"))
        self.verticalLayout_6.addWidget(self.indexFormatsEdit)
        self.gridLayout_2.addLayout(self.verticalLayout_6, 4, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_5.addWidget(self.label_3)
        self.dirEdit = QtGui.QLineEdit(Form)
        self.dirEdit.setMinimumSize(QtCore.QSize(250, 0))
        self.dirEdit.setReadOnly(True)
        self.dirEdit.setObjectName(_fromUtf8("dirEdit"))
        self.horizontalLayout_5.addWidget(self.dirEdit)
        self.dirButton = QtGui.QToolButton(Form)
        self.dirButton.setText(_fromUtf8(""))
        self.dirButton.setObjectName(_fromUtf8("dirButton"))
        self.horizontalLayout_5.addWidget(self.dirButton)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.consoleLabel = QtGui.QLabel(Form)
        self.consoleLabel.setObjectName(_fromUtf8("consoleLabel"))
        self.verticalLayout.addWidget(self.consoleLabel)
        self.progressBar = QtGui.QProgressBar(Form)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.writeButton = QtGui.QPushButton(Form)
        self.writeButton.setObjectName(_fromUtf8("writeButton"))
        self.horizontalLayout.addWidget(self.writeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Header Tool", None))
        self.label.setText(_translate("Form", "Add Files", None))
        self.addFilesButton.setText(_translate("Form", "...", None))
        self.addFilesButton.setShortcut(_translate("Form", "Ctrl+O", None))
        self.deleteButton.setText(_translate("Form", "Delete", None))
        self.deleteButton.setShortcut(_translate("Form", "Ctrl+D", None))
        self.label_5.setText(_translate("Form", "File Preview", None))
        self.groupBox.setTitle(_translate("Form", "Header Comment", None))
        self.label_4.setText(_translate("Form", "Unit", None))
        self.unitEdit.setText(_translate("Form", "mm", None))
        self.label_11.setText(_translate("Form", "Time Unit", None))
        self.timeUnitBox.setItemText(0, _translate("Form", "years", None))
        self.timeUnitBox.setItemText(1, _translate("Form", "days", None))
        self.label_7.setText(_translate("Form", "Scale", None))
        self.scaleEdit.setText(_translate("Form", "1", None))
        self.label_6.setText(_translate("Form", "Column indexes", None))
        self.label_9.setText(_translate("Form", "Column names", None))
        self.label_8.setText(_translate("Form", "Index columns", None))
        self.label_10.setText(_translate("Form", "Index formats", None))
        self.label_3.setText(_translate("Form", "Directory", None))
        self.consoleLabel.setText(_translate("Form", "TextLabel", None))
        self.writeButton.setText(_translate("Form", "Write", None))

