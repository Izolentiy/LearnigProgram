from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets

from screens.base.BaseScreen import BaseScreen
from screens.util.CalendarWidget import CalendarWidget


class EnvironmentScreen(BaseScreen):

    def init_content(self, layout):
        # Fonts
        tipFont = self.assets.TIP_FONT

        # Init tip
        tip = QtWidgets.QLabel()
        tip.setObjectName("tip")
        tip.setFont(tipFont)
        tip.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)

        # Init calendar widget
        calendar = CalendarWidget()
        calendar.setObjectName("calendar")
        calendar.set_style()

        # Add widgets in layout
        self.tip = tip
        self.calendar = calendar
        layout.addWidget(self.tip)
        layout.addSpacing(20)
        layout.addWidget(self.calendar)
        layout.addSpacing(20)

    def translate_text(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Learning program"))
        self.header.setText(_translate("main_window", "LIFE ENVIRONMENTS"))
        self.tip.setText(_translate("main_window", "Point life environments you live in:"))
