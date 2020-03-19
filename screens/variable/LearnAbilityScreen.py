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

        # # Макет для ввода скорости чтения
        # read_layout = QtWidgets.QHBoxLayout()
        # read_tip = QtWidgets.QLabel()  # Read tip
        # read_tip.setObjectName("read_tip")
        # read_tip.setFont(tipFont)
        # read_tip.sizePolicy().setHorizontalStretch(1)
        # read_field = QtWidgets.QLineEdit()  # Read field
        # read_field.setObjectName("read_field")
        # read_tip.sizePolicy().setHorizontalStretch(1)
        # read_field.setMinimumHeight(20)
        # # Макет для ввода скорости просмотра видео
        # watch_layout = QtWidgets.QHBoxLayout()
        # watch_tip = QtWidgets.QLabel()  # Watch tip
        # watch_tip.setObjectName("watch_tip")
        # watch_tip.setFont(tipFont)
        # watch_tip.sizePolicy().setHorizontalStretch(1)
        # watch_field = QtWidgets.QLineEdit()  # Watch field
        # watch_field.setObjectName("watch_field")
        # watch_field.sizePolicy().setHorizontalStretch(1)
        # watch_field.setMinimumHeight(20)
        #
        # # Add widgets in to the layouts
        # self.read_tip = read_tip
        # self.read_field = read_field
        # self.watch_tip = watch_tip
        # self.watch_field = watch_field
        # read_layout.addWidget(self.read_tip)
        # read_layout.addSpacing(10)
        # read_layout.addWidget(self.read_field)
        # read_layout.addStretch(2)
        # watch_layout.addWidget(self.watch_tip)
        # watch_layout.addSpacing(10)
        # watch_layout.addWidget(self.watch_field)
        # watch_layout.addStretch(2)
        # layout.addSpacing(10)
        # layout.addLayout(read_layout)
        # layout.addSpacing(2)
        # layout.addLayout(watch_layout)

        # Создание макета для ввода скоростей чтения и просмотра видео
        speed_layout = QtWidgets.QGridLayout()  # Сеточный макет в котором мы расположим виджеты для ввода
        speed_layout.setSpacing(3)  # Установка внутренних отступов макета

        read_tip = QtWidgets.QLabel()  # Подсказка для поля ввода скорости чтения
        read_tip.setObjectName("read_tip")
        read_tip.setFont(tipFont)
        watch_tip = QtWidgets.QLabel()  # Подсказка для поля ввода скорости просмотра видео
        watch_tip.setObjectName("watch_tip")
        watch_tip.setFont(tipFont)

        read_field = QtWidgets.QLineEdit()  # Поле ввода скорости чтения
        read_field.setObjectName("read_field")
        read_field.setMinimumHeight(20)
        watch_field = QtWidgets.QLineEdit()  # Поле ввода скорости просмотра видео
        watch_field.setObjectName("watch_field")
        watch_field.setMinimumHeight(20)

        # Установка пременных в качестве аттрибутов-данных объекта
        # Это для того, чтобы к этим виджетам был доступ извне
        self.read_tip = read_tip
        self.read_field = read_field
        self.watch_tip = watch_tip
        self.watch_field = watch_field

        # Добавлнеие поле ввода для чтения
        speed_layout.addWidget(self.read_tip, 1, 0)
        speed_layout.addWidget(self.read_field, 1, 1)
        # Добавлнеие поле ввода для видео
        speed_layout.addWidget(self.watch_tip, 2, 0)
        speed_layout.addWidget(self.watch_field, 2, 1)

        # Установка макета с полями ввода в основной макет
        layout.addSpacing(10)
        layout.addLayout(speed_layout)

        layout.addStretch(1)

    def translate_text(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Learning program"))
        self.header.setText(_translate("main_window", "LEARN ABILITIES"))
        self.tip.setText(_translate("main_window", "Point your characteristics (in regular conditions):"))

        self.read_tip.setText(_translate("main_window", "Text reading speed:"))
        self.watch_tip.setText(_translate("main_window", "Video watching speed:"))
