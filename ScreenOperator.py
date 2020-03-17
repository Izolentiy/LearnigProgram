import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QTableWidget

import Constants
from DataProccesor import DataProcessor
from screens.create import ChooseSubjectScreen, LifeFactorsScreen, YourFullJourneyScreen, ChooseMaterialScreen, \
    IndicateLevelScreen, YourScheduleScreen, CongratulationsScreen
from screens.base import StartScreen, OutputTypeScreen
from screens.util import MaterialExplorerScreen
from screens.variable import LearnAbilityScreen, EnvironmentScreen

style = os.path.join(os.path.dirname(__file__), 'screens/base/style.css')


class ScreenController(QMainWindow):

    # Constructor
    def __init__(self):


        # Init screen operator (main window)
        super().__init__()
        # self.setWindowIcon(icon)s
        self.setMinimumSize(500, 600)
        self.resize(1100, 650)
        self.setWindowTitle("Learning program")
        # Init util python scripts
        self.dataProcessor = DataProcessor()
        self.assets = Constants.Assets()

        # Init operation mode and start screen
        self.operate_mode = Constants.START_MODE
        self.startScreen = StartScreen.StartScreen()
        self.fileTypeScreen = OutputTypeScreen.CreateType()

        # Init "create-mode" screens
        self.chooseSubjectScreen = ChooseSubjectScreen.SubjectScreen()
        self.indicateLevelScreen = IndicateLevelScreen.LevelsScreens()
        self.chooseMaterialScreen = ChooseMaterialScreen.MaterialsScreen()
        self.lifeFactorScreen = LifeFactorsScreen.Ui_main_window()
        self.yourScheduleScreen = YourScheduleScreen.ScheduleScreen()
        self.yourFullJourneyScreen = YourFullJourneyScreen.Ui_main_window()
        self.congratulationsScreen = CongratulationsScreen.Ui_main_window()
        # Init "variables-mode" screens
        self.abilitiesScreen = LearnAbilityScreen.AbilitiesScreen()
        self.environmentScreen = EnvironmentScreen.EnvironmentScreen()
        # Init "util_mode" screens
        self.materialExplorerScreen = MaterialExplorerScreen.MaterialExplorer()
        self.settingsScreen = None
        self.informationScreen = None

        # "start-mode" screens
        self.start_screen = [self.startScreen, self.fileTypeScreen]
        self.start_scr_index = 0
        # "create-schedule" screens
        self.create_screen = [self.chooseSubjectScreen, self.indicateLevelScreen, self.chooseMaterialScreen,
                              self.lifeFactorScreen, self.yourScheduleScreen, self.yourFullJourneyScreen,
                              self.congratulationsScreen]
        self.create_scr_index = 0
        # "learn variables" screens
        self.vars_screen = [self.abilitiesScreen, self.environmentScreen]
        self.vars_scr_index = 0
        # Util screens
        self.util_screen = [self.materialExplorerScreen, self.informationScreen, self.settingsScreen]
        self.util_scr_index = 0
        # self.set_page_bars(self.util_screens)
        self.util_showed = False

        # Window settings
        flags = self.windowFlags() | Qt.WindowStaysOnTopHint
        self.setWindowFlags(flags)
        # Style initialization
        self.calendarStyleOn = False
        self.update_style()

        # Show window
        self.set_screen()
        self.show()

    # Util methods
    def update_style(self):
        self.calendarStyleOn = True
        try:
            self.setStyleSheet(open(style).read())
        except FileNotFoundError:
            print('style not found')

    def update_page_bar(self, screens, curr_scr_index):
        screens[curr_scr_index].page_bar.setRange(0, len(screens))
        screens[curr_scr_index].page_bar.setValue(curr_scr_index + 1)
        self.assets = self.assets

    # Screen update methods
    def set_screen(self):
        # Start screens
        if self.operate_mode == Constants.START_MODE:
            # Setting up central widget
            self.start_screen[self.start_scr_index].setupUi(self, self.assets)
            if isinstance(self.start_screen[self.start_scr_index], StartScreen.StartScreen):
                self.startScreen.btnCreate.clicked.connect(self.button_processor)
            elif isinstance(self.start_screen[self.start_scr_index], OutputTypeScreen.CreateType):
                self.fileTypeScreen.btnBack.clicked.connect(self.button_processor)
                self.fileTypeScreen.btnSchedule.clicked.connect(self.button_processor)
                self.fileTypeScreen.btnVars.clicked.connect(self.button_processor)
            else:
                print('something went wrong')

        elif self.operate_mode == Constants.CREATE_SCHEDULE_MODE:
            # Setting up central widget
            self.create_screen[self.create_scr_index].setupUi(self, self.assets)
            self.update_page_bar(self.create_screen, self.create_scr_index)
            # Connect buttons
            self.create_screen[self.create_scr_index].btnNext.clicked.connect(self.button_processor)
            self.create_screen[self.create_scr_index].btnBack.clicked.connect(self.button_processor)
            # Loading screen data
            self.dataProcessor.get_data(self.create_screen[self.create_scr_index])
            if self.operate_mode == 23423:
                pass
            # Choose material screen
            elif isinstance(self.create_screen[self.create_scr_index], ChooseMaterialScreen.MaterialsScreen):
                # Connect buttons
                self.chooseMaterialScreen.btnBooks.clicked.connect(self.button_processor)
                self.chooseMaterialScreen.btnLectures.clicked.connect(self.button_processor)
                self.chooseMaterialScreen.btnWebRes.clicked.connect(self.button_processor)
            # Life factors screen
            elif isinstance(self.create_screen[self.create_scr_index], LifeFactorsScreen.Ui_main_window):
                # Setting up calendar style
                if self.calendarStyleOn:
                    self.lifeFactorScreen.calendar.set_style()
                # Connect buttons
                self.lifeFactorScreen.btnFree.toggled.connect(self.button_processor)
                self.lifeFactorScreen.btnJob.toggled.connect(self.button_processor)
                self.lifeFactorScreen.btnStudy.toggled.connect(self.button_processor)
                # Connect to calendar
                self.lifeFactorScreen.calendar.connect_external(self.lifeFactorScreen)
            # Other statements
            else:
                pass

        elif self.operate_mode == Constants.LEARN_VARIABLES_MODE:
            # Setting up central widget
            self.vars_screen[self.vars_scr_index].setupUi(self, self.assets)
            self.update_page_bar(self.vars_screen, self.vars_scr_index)
            # Connect buttons
            self.vars_screen[self.vars_scr_index].btnNext.clicked.connect(self.button_processor)
            self.vars_screen[self.vars_scr_index].btnBack.clicked.connect(self.button_processor)

        elif self.operate_mode == Constants.SHOW_UTIL_MODE:
            button = self.sender()
            self.util_screen[self.util_scr_index].setupUi(self, self.assets)
            self.materialExplorerScreen.header.setText(button.text())  # Setting up window content
            self.dataProcessor.get_data(self.materialExplorerScreen)  # Loading screen data
            # Connect buttons
            self.materialExplorerScreen.btnBack.clicked.connect(self.button_processor)
            self.materialExplorerScreen.titles_list.clicked.connect(self.button_processor)
            pass

        else:
            print('something went wrong')

    def button_processor(self):
        if self.sender().objectName() == "btnCreate":
            self.start_scr_index += 1
            self.set_screen()
        elif self.sender().objectName() == "btnNext":
            if self.operate_mode == Constants.CREATE_SCHEDULE_MODE:
                self.dataProcessor.set_data(self.create_screen[self.create_scr_index])
                self.create_scr_index += 1
            elif self.operate_mode == Constants.LEARN_VARIABLES_MODE:
                # self.dataProcessor.set_data(self.create_screen[self.create_scr_index])
                self.vars_scr_index += 1
            self.set_screen()

        elif self.sender().objectName() == "btnBack":
            if self.operate_mode == Constants.START_MODE:
                self.start_scr_index -= 1
            elif self.operate_mode == Constants.CREATE_SCHEDULE_MODE:
                if self.create_scr_index == 0:
                    self.operate_mode = Constants.START_MODE
                else:
                    self.create_scr_index -= 1
            elif self.operate_mode == Constants.SHOW_UTIL_MODE:
                self.operate_mode = Constants.CREATE_SCHEDULE_MODE
                if self.util_showed:
                    self.util_showed = False
            elif self.operate_mode == Constants.LEARN_VARIABLES_MODE:
                if self.vars_scr_index == 0:
                    self.operate_mode = Constants.START_MODE
                else:
                    self.vars_scr_index -= 1
                # self.dataProcessor.set_data(self.create_screen[self.create_scr_index])
            else:
                print('btnBack works uncorrect')
            self.set_screen()

        elif self.sender().objectName() == "btnSchedule":
            self.operate_mode = Constants.CREATE_SCHEDULE_MODE
            self.set_screen()
        elif self.sender().objectName() == "btnVars":
            print('btnVars clicked')
            self.operate_mode = Constants.LEARN_VARIABLES_MODE
            self.set_screen()

        elif (self.sender().objectName() == "btnBooks" or
              self.sender().objectName() == "btnLectures" or
              self.sender().objectName() == "btnWebRes"):
            self.show_material_explorer()
            self.util_showed = True
            self.operate_mode = Constants.SHOW_UTIL_MODE
            return

        elif self.sender().objectName() == "btnFree":
            if self.sender().isChecked():
                self.lifeFactorScreen.btnJob.setChecked(False)
                self.lifeFactorScreen.btnStudy.setChecked(False)
                self.lifeFactorScreen.calendar.month_panel.setSelectionMode(QTableWidget.MultiSelection)
            else:
                if (not self.lifeFactorScreen.btnJob.isChecked() and
                        not self.lifeFactorScreen.btnFree.isChecked() and
                        not self.lifeFactorScreen.btnStudy.isChecked()):
                    print('selection mode: no selection')
                    self.lifeFactorScreen.calendar.month_panel.setSelectionMode(QTableWidget.NoSelection)
        elif self.sender().objectName() == "btnJob":
            if self.sender().isChecked():
                self.lifeFactorScreen.btnFree.setChecked(False)
                self.lifeFactorScreen.btnStudy.setChecked(False)
                self.lifeFactorScreen.calendar.month_panel.setSelectionMode(QTableWidget.MultiSelection)
            else:
                if (not self.lifeFactorScreen.btnJob.isChecked() and
                        not self.lifeFactorScreen.btnFree.isChecked() and
                        not self.lifeFactorScreen.btnStudy.isChecked()):
                    print('selection mode: no selection')
                    self.lifeFactorScreen.calendar.month_panel.setSelectionMode(QTableWidget.NoSelection)
        elif self.sender().objectName() == "btnStudy":
            if self.sender().isChecked():
                self.lifeFactorScreen.btnJob.setChecked(False)
                self.lifeFactorScreen.btnFree.setChecked(False)
                self.lifeFactorScreen.calendar.month_panel.setSelectionMode(QTableWidget.MultiSelection)
            else:
                if (not self.lifeFactorScreen.btnJob.isChecked() and
                        not self.lifeFactorScreen.btnFree.isChecked() and
                        not self.lifeFactorScreen.btnStudy.isChecked()):
                    print('selection mode: no selection')
                    self.lifeFactorScreen.calendar.month_panel.setSelectionMode(QTableWidget.NoSelection)
            # self.lifeFactorScreen.btnStudy.setChecked(True)

        elif self.sender().objectName() == "titles_list":
            curr_name = self.materialExplorerScreen.titles_list.currentItem().text()
            materials = self.dataProcessor.materials
            description = self.materialExplorerScreen.description
            description.clear()
            for material in materials:
                if material.properties['NAME'] == curr_name:
                    for key in material.properties:
                        description.append(key)
                        description.append(material.properties[key] + '\n')
            description.scroll(0, 0)
            return

    def show_material_explorer(self):
        button = self.sender()
        print('hello')
        self.materialExplorerScreen.setupUi(self, self.assets)
        print('saldkfjal;skdf')
        self.materialExplorerScreen.header.setText(button.text())  # Setting up window content
        self.dataProcessor.get_data(self.materialExplorerScreen)  # Loading screen data
        # Connect buttons
        self.materialExplorerScreen.btnBack.clicked.connect(self.button_processor)
        self.materialExplorerScreen.titles_list.clicked.connect(self.button_processor)

    # Signals processors
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        if event.key() == Qt.Key_Right:
            self.dataProcessor.set_data(self.create_screen[self.create_scr_index])
            self.create_scr_index += 1
            self.set_screen()
        if event.key() == Qt.Key_Left:
            self.create_scr_index -= 1
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
