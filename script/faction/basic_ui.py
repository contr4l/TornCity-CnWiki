# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basic.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TornSpy(object):
    def setupUi(self, TornSpy):
        TornSpy.setObjectName("TornSpy")
        TornSpy.resize(499, 392)
        TornSpy.setStyleSheet("background-color: rgb(218, 218, 163);")
        self.gridLayout = QtWidgets.QGridLayout(TornSpy)
        self.gridLayout.setObjectName("gridLayout")
        self.key = QtWidgets.QLineEdit(TornSpy)
        self.key.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.key.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.key.setObjectName("key")
        self.gridLayout.addWidget(self.key, 0, 1, 1, 1)
        self.faction_name = QtWidgets.QComboBox(TornSpy)
        self.faction_name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.faction_name.setStyleSheet("font: 14pt \"黑体\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.faction_name.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.faction_name.setIconSize(QtCore.QSize(16, 16))
        self.faction_name.setObjectName("faction_name")
        self.faction_name.addItem("")
        self.faction_name.addItem("")
        self.faction_name.addItem("")
        self.faction_name.addItem("")
        self.faction_name.addItem("")
        self.faction_name.addItem("")
        self.faction_name.addItem("")
        self.gridLayout.addWidget(self.faction_name, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(TornSpy)
        self.label_2.setStyleSheet("font: 14pt \"黑体\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(TornSpy)
        self.label_3.setStyleSheet("font: 14pt \"黑体\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(TornSpy)
        self.label.setStyleSheet("font: 14pt \"黑体\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(TornSpy)
        self.pushButton.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 0);")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(TornSpy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 600 10pt \"黑体\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.faction_id_opt = QtWidgets.QLineEdit(TornSpy)
        self.faction_id_opt.setObjectName("faction_id_opt")
        self.gridLayout.addWidget(self.faction_id_opt, 2, 1, 1, 1)
        self.ClearAll = QtWidgets.QPushButton(TornSpy)
        self.ClearAll.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.ClearAll.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"background-color: rgb(255, 0, 0);")
        self.ClearAll.setObjectName("ClearAll")
        self.gridLayout.addWidget(self.ClearAll, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(TornSpy)
        self.label_5.setStyleSheet("font: 600 10pt \"黑体\";")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 1)

        self.retranslateUi(TornSpy)
        QtCore.QMetaObject.connectSlotsByName(TornSpy)

    def retranslateUi(self, TornSpy):
        _translate = QtCore.QCoreApplication.translate
        TornSpy.setWindowTitle(_translate("TornSpy", "TornSpy"))
        self.faction_name.setItemText(0, _translate("TornSpy", "CCRC"))
        self.faction_name.setItemText(1, _translate("TornSpy", "PTA"))
        self.faction_name.setItemText(2, _translate("TornSpy", "PN"))
        self.faction_name.setItemText(3, _translate("TornSpy", "SH"))
        self.faction_name.setItemText(4, _translate("TornSpy", "NOV"))
        self.faction_name.setItemText(5, _translate("TornSpy", "BSU"))
        self.faction_name.setItemText(6, _translate("TornSpy", "Others"))
        self.label_2.setText(_translate("TornSpy", "Faction"))
        self.label_3.setText(_translate("TornSpy", "Faction_ID (Optional)"))
        self.label.setText(_translate("TornSpy", "Key"))
        self.pushButton.setText(_translate("TornSpy", "Spy!"))
        self.label_4.setText(_translate("TornSpy", "Faction_ID仅当目标帮派\n"
"不在Faction列表中才需要填写"))
        self.faction_id_opt.setStyleSheet(_translate("TornSpy", "font: 14pt \"黑体\";\n"
"background-color: rgb(255, 255, 255);"))
        self.ClearAll.setText(_translate("TornSpy", "Clear Cloud Data"))
        self.label_5.setText(_translate("TornSpy", "谨慎点击!会导致所有云端文档失效->"))
