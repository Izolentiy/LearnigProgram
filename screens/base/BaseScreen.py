from PyQt5 import QtCore, QtWidgets


class BaseScreen(QtWidgets.QWidget):

    # There we setting up central widget in window and connecting assets
    # Здесь мы устанавливаем центральный виджет в главное окно и соединяем его с активами(ресурсами)
    def setupUi(self, main_window, assets):
        self.assets = assets
        self.main_widget = QtWidgets.QWidget()
        self.init_widget()
        main_window.setCentralWidget(self.main_widget)
        self.translate_text(main_window)

    # There we are create and configure central widget
    # Здесь мы создаем и настравиваем центральный виджет
    def init_widget(self):
        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)
        activeLayout = QtWidgets.QHBoxLayout()
        mainLayout.addSpacing(20)  # Top space
        activeLayout.addSpacing(20)  # Left space

        contentLayout = QtWidgets.QVBoxLayout()  # Create content layout
        self.init_base(contentLayout)  # Filling up content layout
        activeLayout.addLayout(contentLayout)
        activeLayout.addSpacing(20)  # Right space
        mainLayout.addLayout(activeLayout)
        mainLayout.addSpacing(20)  # Bottom space
        self.main_widget.setLayout(mainLayout)

    # There inited base components of each inherited screen(page bar, header, navigation buttons)
    # Здесь инициализируем базовые компоненты для каждого дочернего окна(виджета) [прогрес бар, загаловок, и кнопки снизу]
    def init_base(self, layout):
        """ Icons and other assets should be defined from the one python file """
        # Icons
        nextIcon = self.assets.NEXT_ICON
        backIcon = self.assets.BACK_ICON
        # Fonts
        headerFont = self.assets.HEADER_FONT

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
        layout.addWidget(self.header)\

        self.init_content(layout)

        # Creating functional layout with "back" and "next" buttons
        functionalLayout = QtWidgets.QHBoxLayout()
        btnBack = QtWidgets.QPushButton()
        btnBack.setObjectName("btnBack")
        btnBack.setMinimumSize(60, 60)
        btnBack.setMaximumSize(60, 60)
        btnBack.setIcon(backIcon)
        btnNext = QtWidgets.QPushButton()
        btnNext.setObjectName("btnNext")
        btnNext.setMinimumSize(60, 60)
        btnNext.setMaximumSize(60, 60)
        btnNext.setIcon(nextIcon)

        self.btnBack = btnBack
        self.btnNext = btnNext
        functionalLayout.addStretch(1)
        functionalLayout.addWidget(self.btnBack)  # Adding "continue" button in to layout
        functionalLayout.addSpacing(100)
        functionalLayout.addWidget(self.btnNext)  # Adding "create" button in to layout
        functionalLayout.addStretch(1)

        layout.addLayout(functionalLayout)  # Adding functional layout in to contentLayout

    # There will be inited individual components for each inherited screen
    # Здесь каждый наследующий виджет будет определять свое содержимое
    def init_content(self, layout):
        # There is should be individual widgets for each sub-screen
        pass

    # There will be inited all text content of inherited screen
    # В этом методе будут транслироваться надписи
    def translate_text(self, main_window):
        # This method should be deleted in the future, each string on each screen should be defined in special file
        pass
