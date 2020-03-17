from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt

from screens.base.BaseScreen import BaseScreen


class LevelsScreens(BaseScreen):

    def init_content(self, layout):
        # Fonts
        tipFont = self.assets.TIP_FONT
        listFont = self.assets.LIST_FONT

        # Init first tip
        tip = QtWidgets.QLabel()
        tip.setObjectName("tip")
        tip.setFont(tipFont)
        tip.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.tip = tip
        layout.addWidget(self.tip)

        # Init start levels list
        start_list = QtWidgets.QComboBox()
        start_list.setObjectName("start_list")
        start_list.setFont(listFont)
        # Flags for list
        flags = start_list.view().window().windowFlags() | Qt.Popup | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint
        start_list.view().window().setWindowFlags(flags)
        self.start_list = start_list
        layout.addWidget(self.start_list)
        layout.addSpacing(10)

        # Init second tip
        tip_2 = QtWidgets.QLabel()
        tip_2.setObjectName("tip")
        tip_2.setFont(tipFont)
        tip_2.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.tip_2 = tip_2
        layout.addWidget(self.tip_2)

        # Init finish levels list
        finish_list = QtWidgets.QComboBox()
        finish_list.setObjectName("finish_list")
        finish_list.setFont(listFont)
        # Flags for list
        flags = finish_list.view().window().windowFlags() | Qt.Popup | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint
        finish_list.view().window().setWindowFlags(flags)
        self.finish_list = finish_list
        layout.addWidget(self.finish_list)
        layout.addStretch(1)

    def translate_text(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Learning program"))
        self.tip.setText(_translate("main_window", "Enter your start point:"))
        self.tip_2.setText(_translate("main_window", "Enter your finish point:"))
        self.header.setText(_translate("main_window", "INDICATE YOUR LEVEL"))
