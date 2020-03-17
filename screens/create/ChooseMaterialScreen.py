from PyQt5 import QtCore, QtWidgets

from screens.base.BaseScreen import BaseScreen


class MaterialsScreen(BaseScreen):

    def init_content(self, layout):
        # Fonts
        tipFont = self.assets.TIP_FONT
        listFont = self.assets.LIST_FONT

        # Init tip
        tip = QtWidgets.QLabel()
        tip.setObjectName("tip")
        tip.setFont(tipFont)
        # tip.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignCenter)

        # Init wrap layouts
        wrap_layout = QtWidgets.QHBoxLayout()
        buttons_layout = QtWidgets.QVBoxLayout()

        # Init books button
        btnBooks = QtWidgets.QPushButton()
        btnBooks.setObjectName("btnBooks")
        btnBooks.setMinimumHeight(25)
        btnBooks.setMinimumWidth(400)
        # Init lectures button
        btnLectures = QtWidgets.QPushButton()
        btnLectures.setObjectName("btnLectures")
        btnLectures.setMinimumHeight(25)
        btnLectures.setMinimumWidth(400)
        # Init web resources button
        btnWebRes = QtWidgets.QPushButton()
        btnWebRes.setObjectName("btnWebRes")
        btnWebRes.setMinimumHeight(25)
        btnWebRes.setMinimumWidth(400)

        # Add everything in layout
        self.tip = tip
        self.btnBooks = btnBooks
        self.btnLectures = btnLectures
        self.btnWebRes = btnWebRes
        layout.addWidget(self.tip)
        layout.addSpacing(50)
        buttons_layout.addWidget(self.btnBooks)
        buttons_layout.addSpacing(25)
        buttons_layout.addWidget(self.btnLectures)
        buttons_layout.addSpacing(25)
        buttons_layout.addWidget(self.btnWebRes)
        wrap_layout.addStretch(1)
        wrap_layout.addLayout(buttons_layout)
        wrap_layout.addStretch(1)
        layout.addLayout(wrap_layout)
        layout.addStretch(1)

    def translate_text(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Learning program"))
        self.tip.setText(_translate("main_window", "Choose materials you are gonna learn with"))
        self.header.setText(_translate("main_window", "CHOOSE YOUR MATERIALS"))
