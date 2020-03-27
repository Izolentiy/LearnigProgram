from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets

from screens.base.BaseScreen import BaseScreen
from screens.util.CalendarWidget import CalendarWidget


class AbilitiesScreen(BaseScreen):

    def init_content(self, layout):

        self.init_fields()  # Инициализация полей ввода
        self.init_calendar_field()  # Инициализация календаря

        # Обёрточный макет
        wrap_layout = QtWidgets.QHBoxLayout()
        base_layout = QtWidgets.QVBoxLayout()
        base_layout.addWidget(self.speed_tip)
        base_layout.addSpacing(10)
        base_layout.addWidget(self.speed_widget)
        base_layout.addSpacing(20)
        base_layout.addWidget(self.cal_tip)
        base_layout.addWidget(self.cal_widget)

        wrap_layout.addLayout(base_layout)
        wrap_layout.addStretch(1)

        # Установка макета с полями ввода в основной макет
        layout.addLayout(wrap_layout)
        # layout.addWidget(self.speed_tip)
        # layout.addSpacing(10)
        # layout.addWidget(speed_widget)
        # layout.addSpacing(20)
        # layout.addWidget(self.cal_tip)
        # layout.addWidget(cal_widget)
        # layout.addLayout(wrap_layout)

        layout.addStretch(1)

    def init_fields(self):
        # Fonts
        tipFont = self.assets.TIP_FONT

        # Init speed_tip
        speed_tip = QtWidgets.QLabel()
        speed_tip.setObjectName("speed_tip")
        speed_tip.setFont(tipFont)
        speed_tip.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.speed_tip = speed_tip

        # Создание макета для ввода скоростей чтения и просмотра видео
        speed_widget = QtWidgets.QWidget()  # Обёрточный виджет для полей ввода
        speed_layout = QtWidgets.QGridLayout()  # Сеточный макет в котором мы расположим виджеты для ввода
        speed_layout.setSpacing(3)  # Установка внутренних отступов макета

        read_tip = QtWidgets.QLabel()  # Подсказка для поля ввода скорости чтения
        read_tip.setObjectName("read_tip")
        read_tip.setFont(tipFont)
        watch_tip = QtWidgets.QLabel()  # Подсказка для поля ввода скорости просмотра видео
        watch_tip.setObjectName("watch_tip")
        watch_tip.setFont(tipFont)
        con_tip = QtWidgets.QLabel()  # Подсказка для поля ввода времени предельной концентрации
        con_tip.setObjectName("con_tip")
        con_tip.setFont(tipFont)
        sleep_tip = QtWidgets.QLabel()  # Подсказка для поля ввода времени сна
        sleep_tip.setObjectName("sleep_tip")
        sleep_tip.setFont(tipFont)

        read_field = QtWidgets.QLineEdit()  # Поле ввода скорости чтения
        read_field.setMaximumWidth(50)
        read_field.setObjectName("read_field")
        read_field.setMinimumHeight(20)
        read_field.setValidator(QtGui.QIntValidator(1, 1500))
        read_field.setPlaceholderText(QtCore.QCoreApplication.translate('', '42'))
        watch_field = QtWidgets.QComboBox()  # Поле ввода скорости просмотра видео
        watch_field.setMaximumWidth(50)
        watch_field.setObjectName("watch_field")
        watch_field.setMinimumHeight(20)
        for i in range(75, 201, 25):  # Заполнение комбо-бокса со скоростями просмотра видео
            watch_field.addItem(str(i * 0.01))
        watch_field.setCurrentText('1.0')  # Установка начального значения для комбо-бокса
        sleep_field = QtWidgets.QComboBox()  # Поле ввода времени сна
        sleep_field.setMaximumWidth(50)
        sleep_field.setObjectName("sleep_field")
        sleep_field.setMinimumHeight(20)
        for i in range(4, 13):  # Заполнение комбо-бокса с часами сна
            sleep_field.addItem(str(i))
        sleep_field.setCurrentText('8')  # Установка начального значения комбо-бокса
        con_field = QtWidgets.QLineEdit()  # Поле ввода времени предельной концентрации
        con_field.setMaximumWidth(50)
        con_field.setObjectName("con_field")
        con_field.setMinimumHeight(20)
        con_field.setValidator(QtGui.QIntValidator(30, 360))
        con_field.setPlaceholderText(QtCore.QCoreApplication.translate('', '42'))

        read_ps = QtWidgets.QLabel()  # Единиц измерения
        read_ps.setObjectName("read_ps")
        read_ps.setFont(tipFont)
        watch_ps = QtWidgets.QLabel()  # Единиц измерения
        watch_ps.setObjectName("watch_ps")
        watch_ps.setFont(tipFont)
        sleep_ps = QtWidgets.QLabel()  # Единиц измерения
        sleep_ps.setObjectName("sleep_ps")
        sleep_ps.setFont(tipFont)
        con_ps = QtWidgets.QLabel()  # Единиц измерения
        con_ps.setObjectName("con_ps")
        con_ps.setFont(tipFont)

        # Установка доступа к виджетам извне
        self.read_tip = read_tip
        self.read_field = read_field
        self.read_ps = read_ps
        self.watch_tip = watch_tip
        self.watch_field = watch_field
        self.watch_ps = watch_ps
        self.sleep_tip = sleep_tip
        self.sleep_field = sleep_field
        self.sleep_ps = sleep_ps
        self.con_tip = con_tip
        self.con_field = con_field
        self.con_ps = con_ps

        # Добавлнеие поле ввода для чтения
        speed_layout.addWidget(self.read_tip, 0, 0)
        speed_layout.addWidget(self.read_field, 0, 1)
        speed_layout.addWidget(self.read_ps, 0, 2)
        # Добавлнеие поле ввода для видео
        speed_layout.addWidget(self.watch_tip, 1, 0)
        speed_layout.addWidget(self.watch_field, 1, 1)
        speed_layout.addWidget(self.watch_ps, 1, 2)
        # Добавлнеие поле ввода для сна
        speed_layout.addWidget(self.sleep_tip, 2, 0)
        speed_layout.addWidget(self.sleep_field, 2, 1)
        speed_layout.addWidget(self.sleep_ps, 2, 2)
        # Добавлнеие поле ввода для времени предельной концентрации
        speed_layout.addWidget(self.con_tip, 3, 0)
        speed_layout.addWidget(self.con_field, 3, 1)
        speed_layout.addWidget(self.con_ps, 3, 2)
        # Установка макета в обёрточный виджет
        speed_layout.setContentsMargins(0, 0, 0, 0)
        speed_widget.setLayout(speed_layout)

        self.speed_widget = speed_widget

        pass

    def init_calendar_field(self):
        # Fonts
        tipFont = self.assets.TIP_FONT

        # Инициализация виджета календаря и элементов для его настройки
        cal_btns_layout = QtWidgets.QVBoxLayout()  # Макет кнопок управления календарём
        cal_widget = QtWidgets.QWidget()  # Обёрточный виджет для каленадря
        cal_layout = QtWidgets.QHBoxLayout()  # Макет для каленадря

        cal_tip = QtWidgets.QLabel()
        cal_tip.setObjectName("cal_tip")
        cal_tip.setFont(tipFont)
        # cal_tip.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)

        btnStudy = QtWidgets.QPushButton()  # Кнопка для отмето учебных дней
        btnStudy.setObjectName('btnStudy')
        btnStudy.setCheckable(True)
        btnStudy.setChecked(False)
        btnStudy.setMinimumSize(90, 20)
        btnJob = QtWidgets.QPushButton()  # Кнопка для отметок рабочих дней
        btnJob.setObjectName('btnJob')
        btnJob.setCheckable(True)
        btnJob.setChecked(False)
        btnJob.setMinimumSize(90, 20)
        btnFree = QtWidgets.QPushButton()  # Кнопка для отметок выходных дней
        btnFree.setObjectName('btnFree')
        btnFree.setCheckable(True)
        btnFree.setChecked(False)
        btnFree.setMinimumSize(90, 20)

        calendar = CalendarWidget()
        calendar.setObjectName("calendar")

        # Приблуды для каленадрного макета
        self.cal_tip = cal_tip
        self.calendar = calendar
        self.btnStudy = btnStudy
        self.btnJob = btnJob
        self.btnFree = btnFree

        # Добавления календаря и его кнопок в макет и обёрточный виджет
        cal_btns_layout.addWidget(self.btnJob)
        cal_btns_layout.addSpacing(5)
        cal_btns_layout.addWidget(self.btnStudy)
        cal_btns_layout.addSpacing(5)
        cal_btns_layout.addWidget(self.btnFree)
        cal_btns_layout.addStretch(1)
        cal_layout.addWidget(self.calendar)
        cal_layout.addSpacing(5)
        cal_layout.addLayout(cal_btns_layout)
        cal_layout.setSpacing(0)
        cal_layout.setContentsMargins(0, 0, 0, 0)
        cal_widget.setLayout(cal_layout)
        self.cal_widget = cal_widget

    def translate_text(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Learning program"))
        self.header.setText(_translate("main_window", "LEARN ABILITIES"))
        self.speed_tip.setText(_translate("main_window", "Point your characteristics (in regular conditions):"))

        self.read_tip.setText(_translate("main_window", "Text reading speed:"))
        self.read_ps.setText(_translate("main_window", "words/minute"))
        self.watch_tip.setText(_translate("main_window", "Video watching speed:"))
        self.watch_ps.setText(_translate("main_window", "speed coefficient"))
        self.sleep_tip.setText(_translate("main_window", "Sleep time:"))
        self.sleep_ps.setText(_translate("main_window", "hours/day"))
        self.con_tip.setText(_translate("main_window", "Peak concentration time:"))
        self.con_ps.setText(_translate("main_window", "minutes"))

        self.cal_tip.setText(_translate("main_window", "Point life environments you live in:"))
        self.btnStudy.setText(_translate("main_window", "Study days"))
        self.btnJob.setText(_translate("main_window", "Job days"))
        self.btnFree.setText(_translate("main_window", "Free days"))
