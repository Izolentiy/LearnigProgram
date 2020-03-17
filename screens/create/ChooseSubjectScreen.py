from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtWidgets

from screens.base.BaseScreen import BaseScreen


class SubjectScreen(BaseScreen):

    def init_content(self, layout):
        # Fonts
        tipFont = self.assets.TIP_FONT
        listFont = self.assets.LIST_FONT

        # Init tip
        tip = QtWidgets.QLabel()
        tip.setObjectName("tip")
        tip.setFont(tipFont)
        tip.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)

        # Init subject list
        subject_list = QtWidgets.QComboBox()
        subject_list.setObjectName("subject_list")
        subject_list.setFont(listFont)
        # Flags for list
        flags = subject_list.view().window().windowFlags() | Qt.Popup | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint
        subject_list.view().window().setWindowFlags(flags)

        # Add everything in layout
        self.tip = tip
        self.subject_list = subject_list
        layout.addWidget(self.tip)
        layout.addWidget(self.subject_list)
        layout.addStretch(1)

    def translate_text(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Learning program"))
        self.header.setText(_translate("main_window", "CHOOSE YOUR SUBJECT"))
        self.tip.setText(_translate("main_window", "Indicate subject you want to learn:"))
