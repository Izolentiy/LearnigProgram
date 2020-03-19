import os.path

import Material
import ProgramLogic
from screens.create import ChooseSubjectScreen, LifeFactorsScreen, ChooseMaterialScreen, IndicateLevelScreen
from screens.util import MaterialExplorerScreen


# Этот класс надо будет передлать
class UserData:
    def __init__(self):
        self.subject = ''
        self.start_level = ''
        self.finish_level = ''

        self.start_levels = []
        self.finish_levels = []
        self.levels = {self.start_level: '', self.finish_level: ''}


# Этот класс надо будет переделать и вообще по красоте было бы реализовать здесь
# работу с.xml файлами, а не с ссаными .txt
class DataProcessor:

    # Конструктор
    def __init__(self):
        # Initializing source files
        self.subjects_list = os.path.join(os.path.dirname(__file__), 'data/SubjectsList.txt')
        self.levels_list = os.path.join(os.path.dirname(__file__), 'data/LevelsList.txt')
        self.materials_list = os.path.join(os.path.dirname(__file__), 'data/MaterialsList.txt')

        self.programLogic = ProgramLogic.ProgramLogic()

        # Declaration logic variables
        self.time_bounds = None  # Current date - Finish date (deadline)
        self.learn_speed = 0  # Speed measured in PAGE per HOUR (for books) | and in range(0.75 - 2) (for videos)
        self.learn_intensity = None  # Intensity measured in hour count per day
        self.train_type = None  # Training type defined in proportion of types of learning(READ/WATCH, PRACTICE, REPEAT)

        self.subject = ''
        self.levels = {'START LEVEL': '', 'FINISH LEVEL': ''}
        self.materials = []

        self.free_days = []
        self.job_days = []
        self.study_days = []

    # Получение данных для экранов (текст, значения и прочее)
    def get_data(self, screen):
        # Get data for the Subject choose screen
        if isinstance(screen, ChooseSubjectScreen.SubjectScreen):
            file = open(self.subjects_list, "r", encoding="utf-8")
            lines = file.readlines()  # Read lines from file
            lines = [line.rstrip() for line in lines]  # Remove new line symbols: '\n'

            # Filling subject list
            for line in lines:
                if line != '':
                    screen.subject_list.addItem(line.lstrip())
            file.close()
            if self.subject != '':
                screen.subject_list.setCurrentText(self.subject)

        # Get data for the Level indicate screen
        elif isinstance(screen, IndicateLevelScreen.LevelsScreens):
            file = open(self.levels_list, "r", encoding="utf-8")
            lines = file.readlines()  # Read lines from file
            lines = [line.rstrip() for line in lines]  # Remove new line symbols: '\n'

            # Filling level lists
            nls = 0  # NLS - "New Line Symbol" count ('\n')
            for line in lines:
                if line == '':
                    nls += 1
                else:
                    if nls == 1:
                        screen.start_list.addItem(line.lstrip())
                    elif nls == 2:
                        screen.finish_list.addItem(line.lstrip())
            file.close()

            if self.levels.keys() != '':
                screen.start_list.setCurrentText(self.levels['START LEVEL'])
                screen.finish_list.setCurrentText(self.levels['FINISH LEVEL'])

        # Get data for the Material choose screen
        elif isinstance(screen, ChooseMaterialScreen.MaterialsScreen):
            screen.btnBooks.setText("BOOKS")
            screen.btnLectures.setText("LECTURES")
            screen.btnWebRes.setText("WEB RESOURCES")

        # Get data for the Material explorer screen
        elif isinstance(screen, MaterialExplorerScreen.MaterialExplorer):
            # Filling materials list
            subject = self.subject
            material_type = screen.header.text()
            screen.description.clear()
            # Define materials
            self.define_material(subject, material_type, screen)

        # Get data for Life factors screen
        elif isinstance(screen, LifeFactorsScreen.Ui_main_window):
            # Fill time lists
            for hour in range(1, 25):
                screen.sleepTime_list.addItem(str(hour))  # Fill sleep time list
                screen.studyTime_list.addItem(str(hour))  # Fill study time list
                screen.jobTime_list.addItem(str(hour))  # Fill job time list

    # Отправка данных с экранов обрабочик данных (этот метод потом надо будет переделать)
    def set_data(self, screen):
        # Set data for the Subject choose screen
        if isinstance(screen, ChooseSubjectScreen.SubjectScreen):
            self.subject = screen.subject_list.currentText()

        # Set data for the Level indicate screen
        elif isinstance(screen, IndicateLevelScreen.LevelsScreens):
            self.levels['START LEVEL'] = screen.start_list.currentText()
            self.levels['FINISH LEVEL'] = screen.finish_list.currentText()

        # Set data for the Material choose screen
        elif isinstance(screen, ChooseMaterialScreen.MaterialsScreen):
            screen.btnBooks.setText("BOOKS")
            screen.btnLectures.setText("LECTURES")
            screen.btnWebRes.setText("WEB RESOURCES")

        # Set data for the Material explorer screen
        elif isinstance(screen, MaterialExplorerScreen.MaterialExplorer):
            # Filling up materials list
            subject_name = self.subject
            material_type = screen.header.text()
            screen.description.clear()
            # Define materials
            self.define_material(subject_name, material_type, screen)

        # Set data for Life factors screen
        elif isinstance(screen, LifeFactorsScreen.Ui_main_window):
            # Fill time lists
            for hour in range(1, 25):
                screen.sleepTime_list.addItem(str(hour))  # Fill sleep time list
                screen.studyTime_list.addItem(str(hour))  # Fill study time list
                screen.jobTime_list.addItem(str(hour))  # Fill job time list

    # Сохранение данных в файл
    def save_data(self, path=None):
        if path is not None:
            pass

    # Инициализация материалов обучения из файла
    def define_material(self, subject, material_type, screen):
        file = open(self.materials_list, "r", encoding="utf-8")
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

        subject_index = None
        type_index = None
        separator = '------'
        materials_list = []

        # Searching for subject in file
        for line in lines:
            if subject in line:
                subject_index = lines.index(line)  # Define index of subject(number of line in file)

                # Searching for material type
                for line in lines[subject_index:]:
                    if material_type in line:
                        type_index = lines.index(line)  # Define index of material type

                        # Creating materials list, and filling it
                        material_index = 0
                        materials_list.append(Material.create_material(material_type))

                        for line in lines[type_index:]:
                            curr_material = materials_list[material_index]
                            # Ends searching if separator found
                            if separator in line:
                                break
                            # Create new material
                            if '' is line.lstrip() and materials_list:
                                materials_list.append(Material.create_material(material_type))
                                material_index += 1
                                continue
                            # Filling up material properties
                            string = line.lstrip()[:line.index(':') - 2]  # Removing '\t' symbols
                            keys = curr_material.keys  # Get keys from certain material type (BOOK for example)
                            if string in keys:  # Searching for keys
                                # Defining values of fields
                                data = line.lstrip()
                                data = line[line.index(':') + 2:]

                                curr_material.properties[string] = data
                                # screen.description.append(string + '\n' + data + '\n')
                                if string == "NAME":  # Adding to list of titles
                                    screen.titles_list.addItem(curr_material.properties[string])

                        break
                break
        self.materials = materials_list
        file.close()
