import os
import traceback

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QPushButton

import Constants
from DataProcessor import DataProcessor
from screens.create import ChooseSubjectScreen, LifeFactorsScreen, YourFullJourneyScreen, ChooseMaterialScreen, \
    IndicateLevelScreen, YourScheduleScreen, CongratulationsScreen
from screens.base import StartScreen, OutputTypeScreen
from screens.util import MaterialExplorerScreen
from screens.variable import LearnAbilityScreen, EnvironmentScreen

style = os.path.join(os.path.dirname(__file__), 'screens/base/style.css')


class ScreenController(QMainWindow):

    """ Класс контроллер экранов наследует класс QMainWindow [по-русски "главное окно"]
    в нём происходят основные операции связанные с центральными виджетами "экранами",
    а также вспомогательными объектами (Обратчик данных, Активы)
    """

    # Конструктор
    def __init__(self):

        # Init screen operator (main window)
        super().__init__()

        # Настраиваем главное окно
        # self.setMinimumSize(500, 600)
        self.resize(1100, 650)
        self.setWindowTitle("Learning program")
        # Определяем вспомогательные пайтон скрипты
        self.dataProcessor = DataProcessor()
        self.assets = Constants.Assets()

        # Опеределям начальный режим окна, и инициализируем виджеты начального окна
        self.operate_mode = Constants.START_MODE
        self.startScreen = StartScreen.StartScreen()
        self.fileTypeScreen = OutputTypeScreen.CreateType()

        # Инициализиурем виджеты для режима "создание учебного плана"
        self.chooseSubjectScreen = ChooseSubjectScreen.SubjectScreen()
        self.indicateLevelScreen = IndicateLevelScreen.LevelsScreens()
        self.chooseMaterialScreen = ChooseMaterialScreen.MaterialsScreen()
        self.lifeFactorScreen = LifeFactorsScreen.Ui_main_window()
        self.yourScheduleScreen = YourScheduleScreen.ScheduleScreen()
        self.yourFullJourneyScreen = YourFullJourneyScreen.Ui_main_window()
        self.congratulationsScreen = CongratulationsScreen.Ui_main_window()
        # Инициализируем виджеты для режима "определние переменных обучения"
        self.abilitiesScreen = LearnAbilityScreen.AbilitiesScreen()
        self.environmentScreen = EnvironmentScreen.EnvironmentScreen()
        # Инициализируем виджеты для режима "вспомогательные экраны" (настройки, окно просмотра материалов)
        self.materialExplorerScreen = MaterialExplorerScreen.MaterialExplorer()
        self.settingsScreen = None
        self.informationScreen = None

        # Создаем список экранов для каждого режима окна и индексы к ним
        self.start_screen = [self.startScreen, self.fileTypeScreen]
        self.start_scr_index = 0
        # Экраны для режима "Создание плана"
        self.create_screen = [self.chooseSubjectScreen,
                              self.indicateLevelScreen,
                              self.chooseMaterialScreen,
                              self.lifeFactorScreen,
                              self.yourScheduleScreen,
                              self.yourFullJourneyScreen,
                              self.congratulationsScreen]
        self.create_scr_index = 0
        # Экраны для режима "Переменные обучения"
        self.vars_screen = [self.abilitiesScreen, self.environmentScreen]
        self.vars_scr_index = 0
        # Вспомогатльные экраны (настройки, обозреватель экранов, "Морган Фриман")
        self.util_screen = [self.materialExplorerScreen, self.informationScreen, self.settingsScreen]
        self.util_scr_index = 0
        self.util_showed = False

        # Словарь содержащий все списки с экранами и определяющий для них ключи
        self.screens = {
            Constants.START_MODE: self.start_screen,
            Constants.LEARN_VARIABLES_MODE: self.vars_screen,
            Constants.CREATE_SCHEDULE_MODE: self.create_screen,
            Constants.SHOW_UTIL_MODE: self.util_screen
                        }

        # Вспомогательные флаги, для настройки отображения окна
        # flags = self.windowFlags() | Qt.WindowStaysOnTopHint
        # self.setWindowFlags(flags)
        # Инициализация стилей
        self.calendarStyleOn = False
        self.update_style()

        # Отображение окна
        self.set_screen()
        self.show()

    # Вспомогательные методы
    def update_style(self):
        self.calendarStyleOn = True
        try:
            self.setStyleSheet(open(style).read())
        except FileNotFoundError:
            print('style not found')

    @classmethod
    def update_page_bar(cls, screens, curr_scr_index):
        screens[curr_scr_index].page_bar.setRange(0, len(screens))
        screens[curr_scr_index].page_bar.setValue(curr_scr_index + 1)

    """
    --------||-------- Методы для работы с виджетами --------||--------
    """
    # Метод для манипулирования центральным видзжетом
    def set_screen(self):
        try:
            # Укорачиваниме имен переменных
            index = None
            mode = self.operate_mode
            assets = self.assets

            # Определение индекса
            if mode == Constants.START_MODE:
                index = self.start_scr_index
            elif mode == Constants.LEARN_VARIABLES_MODE:
                index = self.vars_scr_index
            elif mode == Constants.CREATE_SCHEDULE_MODE:
                index = self.create_scr_index
            elif mode == Constants.SHOW_UTIL_MODE:
                index = self.util_scr_index

            # Установка центрального виджета
            screen = self.screens[mode][index]
            screen.setupUi(self, assets)

            # Если режим окна начальный, то будет выполняться этот блок
            if mode == Constants.START_MODE:
                if isinstance(screen, StartScreen.StartScreen):
                    screen.btnCreate.clicked.connect(self.button_processor)
                elif isinstance(screen, OutputTypeScreen.CreateType):
                    screen.btnBack.clicked.connect(self.button_processor)
                    screen.btnSchedule.clicked.connect(self.button_processor)
                    screen.btnVars.clicked.connect(self.button_processor)

            # Если режим окна "создание учебного плана", то будет выполняться этот блок
            elif mode == Constants.CREATE_SCHEDULE_MODE:
                self.update_page_bar(self.screens[mode], index)
                # Соединение кнопок
                screen.btnNext.clicked.connect(self.button_processor)
                screen.btnBack.clicked.connect(self.button_processor)
                # Загрузка данных для центрального виджета
                self.dataProcessor.get_data(screen)
                if self.operate_mode == 42:
                    pass
                # Настройка виджета для выбора материалов
                elif isinstance(screen, ChooseMaterialScreen.MaterialsScreen):
                    # Connect buttons
                    screen.btnBooks.clicked.connect(self.button_processor)
                    screen.btnLectures.clicked.connect(self.button_processor)
                    screen.btnWebRes.clicked.connect(self.button_processor)
                # Life factors screen
                elif isinstance(screen, LifeFactorsScreen.Ui_main_window):
                    # Setting up calendar style
                    if self.calendarStyleOn:
                        screen.calendar.set_style()
                    # Connect buttons
                    screen.btnFree.toggled.connect(self.button_processor)
                    screen.btnJob.toggled.connect(self.button_processor)
                    screen.btnStudy.toggled.connect(self.button_processor)
                    # Connect to calendar
                    screen.calendar.connect_external(screen)

            # Если режим окна "определение переменных обучения", то будет выполняться этот блок
            elif mode == Constants.LEARN_VARIABLES_MODE:
                self.update_page_bar(self.screens[mode], index)
                # Поключение кнопок к обработчку кнопок
                screen.btnNext.clicked.connect(self.button_processor)
                screen.btnBack.clicked.connect(self.button_processor)
                # Настройка виджета для выбора материалов
                if mode == 42:
                    pass
                elif isinstance(screen, LearnAbilityScreen.AbilitiesScreen):
                    if self.calendarStyleOn:
                        screen.calendar.set_style()
                    # Connect buttons
                    screen.btnFree.toggled.connect(self.button_processor)
                    screen.btnJob.toggled.connect(self.button_processor)
                    screen.btnStudy.toggled.connect(self.button_processor)
                    # Соединение с календарём
                    screen.calendar.connect_external(screen)
                # Настройка виджета для выбора материалов
                elif isinstance(screen, ChooseMaterialScreen.MaterialsScreen):
                    # Connect buttons
                    screen.btnBooks.clicked.connect(self.button_processor)
                    screen.btnLectures.clicked.connect(self.button_processor)
                    screen.btnWebRes.clicked.connect(self.button_processor)

            # Если режим окна "отображение вспомогательных окон", то будет выполняться этот блок
            elif mode == Constants.SHOW_UTIL_MODE:
                button = self.sender()
                screen.header.setText(button.text())  # Setting up window content
                self.dataProcessor.get_data(screen)  # Loading screen data
                # Connect buttons
                screen.btnBack.clicked.connect(self.button_processor)
                screen.titles_list.clicked.connect(self.button_processor)

        except (RuntimeError, NameError, AttributeError, IndexError):
            stack = traceback.extract_stack()
            print('Что-то пошло не так в методе: {}'.format(stack[-1][2]))  # [-1][2] Это просто магические числа

    # Обработчик нажатий
    def button_processor(self):
        try:
            # Укорачиваниме имен переменных
            cur_index = None  # Старое значение индекса
            index = None  # Будет принимать изменения индекса
            cur_mode = self.operate_mode  # Старое значение режима
            mode = self.operate_mode  # Режим экрана
            screen = self.centralWidget().screen  # Текущий экран
            element = self.sender()  # Элемент на который нажали
            element_id = element.objectName()  # Имя этого элемента
            # Определение индекса
            if mode == Constants.START_MODE:
                index = self.start_scr_index
                cur_index = self.start_scr_index
            elif mode == Constants.LEARN_VARIABLES_MODE:
                index = self.vars_scr_index
                cur_index = self.vars_scr_index
            elif mode == Constants.CREATE_SCHEDULE_MODE:
                index = self.create_scr_index
                cur_index = self.create_scr_index
            elif mode == Constants.SHOW_UTIL_MODE:
                index = self.util_scr_index
                cur_index = self.util_scr_index

            # Обработка нажатий
            if element_id == "btnCreate":
                index += 1
            elif element_id == "btnNext":
                if mode == Constants.CREATE_SCHEDULE_MODE:
                    self.dataProcessor.set_data(screen)
                    index += 1
                elif mode == Constants.LEARN_VARIABLES_MODE:
                    index += 1
                    self.dataProcessor.save_data('data/variables/test.txt')

            elif element_id == "btnBack":
                self.dataProcessor.set_data(screen)
                if mode == Constants.START_MODE:
                    index -= 1
                elif mode == Constants.CREATE_SCHEDULE_MODE:
                    if index == 0:
                        mode = Constants.START_MODE
                    else:
                        index -= 1
                elif mode == Constants.SHOW_UTIL_MODE:
                    mode = Constants.CREATE_SCHEDULE_MODE
                    if self.util_showed:
                        self.util_showed = False
                elif mode == Constants.LEARN_VARIABLES_MODE:
                    if index == 0:
                        mode = Constants.START_MODE
                    else:
                        index -= 1
                else:
                    pass

            elif element_id == "btnSchedule":
                mode = Constants.CREATE_SCHEDULE_MODE
            elif element_id == "btnVars":
                mode = Constants.LEARN_VARIABLES_MODE
            elif (element_id == "btnBooks" or
                  element_id == "btnLectures" or
                  element_id == "btnWebRes"):
                self.util_showed = True
                mode = Constants.SHOW_UTIL_MODE
            if mode != cur_mode or index != cur_index:
                # Обратное определение индекса
                if cur_mode == Constants.START_MODE:
                    self.start_scr_index = index
                elif cur_mode == Constants.LEARN_VARIABLES_MODE:
                    self.vars_scr_index = index
                elif cur_mode == Constants.CREATE_SCHEDULE_MODE:
                    self.create_scr_index = index
                elif cur_mode == Constants.SHOW_UTIL_MODE:
                    self.util_scr_index = index
                self.operate_mode = mode  # Обратное определение режима
                self.set_screen()

            if element_id == "btnFree":
                if element.isChecked():
                    screen.btnJob.setChecked(False)
                    screen.btnStudy.setChecked(False)
                    screen.calendar.month_panel.setSelectionMode(QTableWidget.MultiSelection)
                else:
                    if (not screen.btnJob.isChecked() and
                            not screen.btnFree.isChecked() and
                            not screen.btnStudy.isChecked()):
                        screen.calendar.month_panel.setSelectionMode(QTableWidget.NoSelection)
            elif element_id == "btnJob":
                if element.isChecked():
                    screen.btnFree.setChecked(False)
                    screen.btnStudy.setChecked(False)
                    screen.calendar.month_panel.setSelectionMode(QTableWidget.MultiSelection)
                else:
                    if (not screen.btnJob.isChecked() and
                            not screen.btnFree.isChecked() and
                            not screen.btnStudy.isChecked()):
                        screen.calendar.month_panel.setSelectionMode(QTableWidget.NoSelection)
            elif element_id == "btnStudy":
                if element.isChecked():
                    screen.btnJob.setChecked(False)
                    screen.btnFree.setChecked(False)
                    screen.calendar.month_panel.setSelectionMode(QTableWidget.MultiSelection)
                else:
                    if (not screen.btnJob.isChecked() and
                            not screen.btnFree.isChecked() and
                            not screen.btnStudy.isChecked()):
                        screen.calendar.month_panel.setSelectionMode(QTableWidget.NoSelection)

            elif element_id == "titles_list":
                curr_name = screen.titles_list.currentItem().text()
                materials = self.dataProcessor.materials
                description = screen.description
                description.clear()
                for material in materials:
                    if material.properties['NAME'] == curr_name:
                        for key in material.properties:
                            description.append(key)
                            description.append(material.properties[key] + '\n')
                description.scroll(0, 0)
                return
        except (RuntimeError, NameError, AttributeError, IndexError):
            stack = traceback.extract_stack()
            print('Что-то пошло не так в методе: {}'.format(stack[-1][2]))  # [-1][2] Это просто магические числа

    """
    --------||--------
    Обработчики сигналов по типу нажатие на клавишу, но они не обязательны, просто хотел
    попробовать добавить функционал управления с клавиатруы
    --------||--------
    """
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        if event.key() == Qt.Key_Right:
            self.start_scr_index += 1
            self.set_screen()
        if event.key() == Qt.Key_Left:
            self.start_scr_index -= 1
            self.set_screen()

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = event.pos()
        self.update()

        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.end = event.pos()
        self.update()

        super().mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

        super().mouseMoveEvent(event)
