from PyQt5 import QtCore, QtGui, QtWidgets

from screens.base.BaseScreen import BaseScreen


class StartScreen(BaseScreen):

    def init_widget(self):
        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)
        activeLayout = QtWidgets.QHBoxLayout()
        mainLayout.addSpacing(20)  # Top space
        mainLayout.addStretch(1)
        activeLayout.addSpacing(20)  # Left space

        contentLayout = QtWidgets.QVBoxLayout()  # Create content layout
        self.init_content(contentLayout)  # Filling up content layout
        activeLayout.addLayout(contentLayout)
        activeLayout.addSpacing(20)  # Right space
        mainLayout.addLayout(activeLayout)
        mainLayout.addSpacing(20)  # Bottom space
        mainLayout.addStretch(1)
        self.widget.setLayout(mainLayout)

    def init_content(self, layout):
        # Icons
        settingsIcon = self.assets.SETTINGS_ICON
        createIcon = self.assets.CREATE_ICON
        # Fonts
        btnFont = self.assets.BTN_FONT
        nameFont = self.assets.NAME_FONT

        settingsLayout = QtWidgets.QHBoxLayout()
        btnSettings = QtWidgets.QPushButton()
        btnSettings.setMinimumSize(60, 60)
        btnSettings.setMaximumSize(60, 60)
        btnSettings.setObjectName("btnSettings")
        btnSettings.setIcon(settingsIcon)
        self.btnSettings = btnSettings
        settingsLayout.addWidget(self.btnSettings)  # Adding "settings" button in to layout
        layout.addLayout(settingsLayout)

        layout.addSpacing(80)
        programName = QtWidgets.QLabel()
        # programName.resize(0, 150)
        programName.setObjectName("name")
        programName.setFont(nameFont)
        programName.setAlignment(QtCore.Qt.AlignCenter)
        self.programName = programName
        layout.addWidget(self.programName)  # Adding "programName" label in to layout
        layout.addSpacing(80)

        # Creating functional layout with "create" and "continue" buttons
        functionalLayout = QtWidgets.QHBoxLayout()
        btnContinue = QtWidgets.QPushButton()
        btnContinue.setMinimumSize(60, 60)
        btnContinue.setMaximumSize(60, 60)
        btnContinue.setObjectName("btnContinue")
        btnContinue.setFont(btnFont)

        btnCreate = QtWidgets.QPushButton()
        btnCreate.setMinimumSize(60, 60)
        btnCreate.setMaximumSize(60, 60)
        btnCreate.setObjectName("btnCreate")
        btnCreate.setIcon(createIcon)

        self.btnContinue = btnContinue
        self.btnCreate = btnCreate
        functionalLayout.addWidget(self.btnContinue)  # Adding "continue" button in to layout
        functionalLayout.addWidget(self.btnCreate)  # Adding "create" button in to layout

        layout.addLayout(functionalLayout)  # Adding functional layout in to contentLayout

    def translate_text(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Learning program"))
        self.programName.setText(_translate("main_window", "LEARNING PROGRAM"))
        self.btnContinue.setText(_translate("main_window", "..."))
