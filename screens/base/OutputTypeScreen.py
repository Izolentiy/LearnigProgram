from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets

from screens.base.BaseScreen import BaseScreen


class CreateType(BaseScreen):

    def init_base(self, layout):
        """ Icons and other assets should be defined from the one python file """
        # Icons
        backIcon = self.assets.ANGLE_DONW_ICON
        # Fonts
        headerFont = self.assets.HEADER_FONT

        # Init page bar
        page_bar = QtWidgets.QProgressBar()
        page_bar.setObjectName("page_bar")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(page_bar.sizePolicy().hasHeightForWidth())
        page_bar.setSizePolicy(sizePolicy)
        page_bar.setMinimumSize(QtCore.QSize(0, 4))
        page_bar.setProperty("value", 0)
        page_bar.setTextVisible(False)
        self.page_bar = page_bar
        layout.addWidget(self.page_bar)  # Adding "page bar" in to layout

        # Init header
        header = QtWidgets.QLabel()
        header.setObjectName("header")
        header.setMinimumSize(QtCore.QSize(0, 60))
        header.setAlignment(QtCore.Qt.AlignCenter)
        header.setFont(headerFont)
        self.header = header
        layout.addWidget(self.header)

        self.init_content(layout)
        layout.addStretch(1)

        # Creating functional layout with "back" and "next" buttons
        functionalLayout = QtWidgets.QHBoxLayout()
        btnBack = QtWidgets.QPushButton()
        btnBack.setObjectName("btnBack")
        btnBack.setMinimumSize(60, 60)
        btnBack.setMaximumSize(60, 60)
        btnBack.setIcon(backIcon)

        self.btnBack = btnBack
        functionalLayout.addWidget(self.btnBack)  # Adding "continue" button in to layout

        layout.addLayout(functionalLayout)  # Adding functional layout in to contentLayout

    def init_content(self, layout):
        # Fonts
        tipFont = self.assets.TIP_FONT
        btnFont = self.assets.BTN_FONT

        # Init buttons layout
        wrap_layout = QtWidgets.QHBoxLayout()
        buttons_layout = QtWidgets.QVBoxLayout()

        # Init tip
        tip = QtWidgets.QLabel()
        tip.setObjectName("tip")
        tip.setFont(tipFont)
        tip.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignCenter)

        # Create schedule button
        btnSchedule = QtWidgets.QPushButton()
        btnSchedule.setObjectName('btnSchedule')
        btnSchedule.setMinimumHeight(25)
        btnSchedule.setMinimumWidth(400)

        # Create learn variables button
        btnVars = QtWidgets.QPushButton()
        btnVars.setObjectName('btnVars')
        btnVars.setMinimumHeight(25)
        btnVars.setMinimumWidth(400)

        # Layout filling
        self.tip = tip
        self.btnSchedule = btnSchedule
        self.btnVars = btnVars
        layout.addLayout(wrap_layout)
        wrap_layout.addStretch(1)
        wrap_layout.addLayout(buttons_layout)
        wrap_layout.addStretch(1)
        buttons_layout.addWidget(self.tip)
        buttons_layout.addSpacing(50)
        buttons_layout.addWidget(self.btnSchedule)
        buttons_layout.addSpacing(20)
        buttons_layout.addWidget(self.btnVars)

    def translate_text(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Learning program"))
        self.header.setText(_translate("main_window", "CREATE"))
        self.tip.setText(_translate("main_window", "Output file you want to create:"))
        self.btnSchedule.setText(_translate("main_window", "NEW SCHEDULE"))
        self.btnVars.setText(_translate("main_window", "NEW LEARN VARIABLES"))
