from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets

from screens.base.BaseScreen import BaseScreen


class AbilitiesScreen(BaseScreen):

    def init_content(self, layout):
        # Fonts
        tipFont = self.assets.TIP_FONT
        # Policies
        fieldPolicy = self.assets.FIELD_POLICY

        # Init tip
        tip = QtWidgets.QLabel()
        tip.setObjectName("tip")
        tip.setFont(tipFont)
        tip.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.tip = tip
        layout.addWidget(self.tip)

        # Init reading speed layout
        read_layout = QtWidgets.QHBoxLayout()
        read_tip = QtWidgets.QLabel()  # Read tip
        read_tip.setObjectName("read_tip")
        read_tip.setFont(tipFont)
        read_field = QtWidgets.QLineEdit()  # Read field
        read_field.setObjectName("read_field")
        read_field.setSizePolicy(fieldPolicy)
        read_field.setMinimumHeight(20)
        # Init watching speed layout
        watch_layout = QtWidgets.QHBoxLayout()
        watch_tip = QtWidgets.QLabel()  # Watch tip
        watch_tip.setObjectName("watch_tip")
        watch_tip.setFont(tipFont)
        watch_field = QtWidgets.QLineEdit()  # Watch field
        watch_field.setObjectName("watch_field")
        watch_field.setSizePolicy(fieldPolicy)
        watch_field.setMinimumHeight(20)

        # Add widgets in to the layouts
        self.read_tip = read_tip
        self.read_field = read_field
        self.watch_tip = watch_tip
        self.watch_field = watch_field
        read_layout.addWidget(self.read_tip)
        read_layout.addWidget(self.read_field)
        watch_layout.addWidget(self.watch_tip)
        watch_layout.addWidget(self.watch_field)
        layout.addSpacing(10)
        layout.addLayout(read_layout)
        layout.addSpacing(2)
        layout.addLayout(watch_layout)

        layout.addStretch(2)

    def translate_text(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Learning program"))
        self.header.setText(_translate("main_window", "LEARN ABILITIES"))
        self.tip.setText(_translate("main_window", "Point your characteristics (in regular conditions):"))

        self.read_tip.setText(_translate("main_window", "Text reading speed:"))
        self.watch_tip.setText(_translate("main_window", "Video watching speed:"))
