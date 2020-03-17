from PyQt5 import QtCore, QtGui, QtWidgets

from screens.base.BaseScreen import BaseScreen


class MaterialExplorer(BaseScreen):

    def init_base(self, layout):
        # Icons
        nextIcon = self.assets.NEXT_ICON
        backIcon = self.assets.BACK_ICON
        # Fonts
        headerFont = self.assets.HEADER_FONT
        btnFont = self.assets.BTN_FONT

        # Init page bar
        page_bar = QtWidgets.QProgressBar(self)
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
        header = QtWidgets.QLabel(self)
        header.setObjectName("header")
        header.setMinimumSize(QtCore.QSize(0, 60))
        header.setFont(headerFont)
        self.header = header
        layout.addWidget(self.header)

        # Init content
        self.init_content(layout)

        # Creating functional layout with "back" and "next" buttons
        functionalLayout = QtWidgets.QHBoxLayout()
        btnBack = QtWidgets.QPushButton()
        btnBack.setObjectName("btnBack")
        btnBack.setMinimumSize(60, 60)
        btnBack.setMaximumSize(60, 60)
        btnBack.setIcon(backIcon)
        btnUnknown = QtWidgets.QPushButton()
        btnUnknown.setObjectName("btnUnknown")
        btnUnknown.setMinimumSize(60, 60)
        btnUnknown.setMaximumSize(60, 60)
        btnUnknown.setFont(btnFont)
        btnUnknown.setText("...")

        self.btnBack = btnBack
        self.btnUnknown = btnUnknown
        functionalLayout.addStretch(1)
        functionalLayout.addWidget(self.btnBack)  # Adding "continue" button in to layout
        functionalLayout.addSpacing(100)
        functionalLayout.addWidget(self.btnUnknown)  # Adding "create" button in to layout
        functionalLayout.addStretch(1)
        layout.addLayout(functionalLayout)  # Adding functional layout in to contentLayout

    def init_content(self, layout):
        # Fonts
        contentFont = self.assets.TIP_FONT
        # Size Policies
        descriptionPolicy = self.assets.DESCRIPTION_POLICY
        titlesPolicy = self.assets.TITLES_POLICY
        sortPolicy = self.assets.SORT_POLICY

        # Init internal layouts
        wrapLayout = QtWidgets.QHBoxLayout()
        titlesLayout = QtWidgets.QVBoxLayout()
        sortLayout = QtWidgets.QHBoxLayout()
        # Init tip
        tip = QtWidgets.QLabel()
        tip.setObjectName("tip")
        tip.setFont(contentFont)
        tip.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        # Init sort list
        sort_list = QtWidgets.QComboBox()
        sort_list.setObjectName("sort_list")
        sort_list.setSizePolicy(sortPolicy)
        sort_list.setFont(contentFont)
        sort_list.setFocusPolicy(QtCore.Qt.WheelFocus)
        sort_list.addItem("")
        sort_list.addItem("")
        self.tip = tip
        self.sort_list = sort_list
        sortLayout.addWidget(self.tip)
        sortLayout.addSpacing(10)
        sortLayout.addWidget(self.sort_list)
        # Init list of titles
        titles_list = QtWidgets.QListWidget()
        titles_list.setObjectName("titles_list")
        titles_list.setAlternatingRowColors(True)
        titles_list.setWordWrap(True)
        # Init description
        description = QtWidgets.QTextEdit()
        description.setObjectName("description")
        description.setSizePolicy(descriptionPolicy)
        description.setFocusPolicy(QtCore.Qt.StrongFocus)
        description.setReadOnly(True)
        description.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.titles_list = titles_list
        self.description = description
        titlesLayout.addLayout(sortLayout)
        titlesLayout.addWidget(self.titles_list)

        # Add all widgets in content layout
        wrapWidget = QtWidgets.QWidget()
        wrapWidget.setMinimumWidth(200)
        wrapWidget.setSizePolicy(titlesPolicy)
        titlesLayout.setContentsMargins(0, 0, 0, 0)
        titlesLayout.setSpacing(2)
        wrapWidget.setLayout(titlesLayout)
        wrapLayout.addWidget(wrapWidget)
        wrapLayout.addSpacing(4)
        wrapLayout.addWidget(self.description)
        layout.addLayout(wrapLayout)
        layout.addSpacing(30)

    def translate_text(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Learning program"))
        self.header.setText(_translate("main_window", "TITLE"))
        self.btnUnknown.setText(_translate("main_window", "..."))
        self.tip.setText(_translate("main_window", "Sort by:"))
        self.sort_list.setItemText(0, _translate("main_window", "Name"))
        self.sort_list.setItemText(1, _translate("main_window", "Level"))
