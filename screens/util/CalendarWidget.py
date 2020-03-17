# Version 2
# Implemented using layouts
import calendar
import datetime
import os

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QWidget, QPushButton, \
    QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QSizePolicy, QHeaderView

style = os.path.join(os.path.dirname(__file__), 'style_calendar.css')


class Date:
    def __init__(self):
        self.year = None
        self.month = None
        self.day = None
        self.month_list = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE',
                           'JULE', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']


class CalendarWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.show_months = True  # Show month table
        self.show_years = False  # Show year table
        self.isExternalConnected = False  # Connection status to external widget

        self.init_date()
        self.init_main_panel()

    # Methods for working with date
    def init_date(self):
        self.date = Date()
        self.cur_date = Date()

        current_date = datetime.date.today()
        self.date.year = current_date.year
        self.date.month = current_date.month
        self.date.day = current_date.day

        self.cur_date.year = current_date.year
        self.cur_date.month = current_date.month
        self.cur_date.day = current_date.day

        self.month_list = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE',
                           'JULE', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']

    def update_date(self):

        pass

    # Init panels
    def init_main_panel(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Init all child panels
        self.init_navigation_panel(main_layout)
        self.init_weekday_panel(main_layout)
        self.init_month_panel(main_layout)

        self.setLayout(main_layout)

    def init_navigation_panel(self, main_layout):
        navigation_panel = QWidget()
        wrap_widget = QWidget()
        navigation_layout = QHBoxLayout()
        wrap_layout = QVBoxLayout()
        navigation_layout.setContentsMargins(0, 0, 0, 0)
        navigation_layout.setSpacing(0)
        wrap_layout.setContentsMargins(0, 0, 0, 0)
        wrap_layout.setSpacing(0)

        # Create buttons and it's configuration
        btnPrevious = QPushButton()
        btnFollowing = QPushButton()
        btnMonth = QPushButton()
        btnYear = QPushButton()
        btnPrevious.setObjectName("btnPrevious")
        btnFollowing.setObjectName("btnFollowing")
        btnMonth.setObjectName("btnMonth")
        btnYear.setObjectName("btnYear")

        # Connect buttons
        btnPrevious.clicked.connect(self.button_controller)
        btnFollowing.clicked.connect(self.button_controller)
        btnMonth.clicked.connect(self.button_controller)
        btnYear.clicked.connect(self.button_controller)

        # Set panel's size
        wrap_button = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        wrap_button.setVerticalStretch(1)
        wrap_button.setHorizontalStretch(3)
        navigate_button = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        navigate_button.setHorizontalStretch(2)
        panel_policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        panel_policy.setVerticalStretch(3)

        btnPrevious.setSizePolicy(navigate_button)
        btnFollowing.setSizePolicy(navigate_button)
        btnYear.setSizePolicy(wrap_button)
        btnMonth.setSizePolicy(wrap_button)
        wrap_widget.setSizePolicy(wrap_button)
        navigation_panel.setSizePolicy(panel_policy)

        # Set buttons' access
        self.btnPrevious = btnPrevious
        self.btnFollowing = btnFollowing
        self.btnMonth = btnMonth
        self.btnYear = btnYear

        # Adding buttons in to the layouts
        navigation_layout.addWidget(self.btnPrevious)
        wrap_layout.addWidget(self.btnMonth)
        wrap_layout.addWidget(self.btnYear)
        wrap_widget.setLayout(wrap_layout)
        navigation_layout.addWidget(wrap_widget)
        navigation_layout.addWidget(self.btnFollowing)

        navigation_panel.setLayout(navigation_layout)
        main_layout.addWidget(navigation_panel)

        self.btnMonth.setText(self.month_list[self.date.month - 1])
        self.btnYear.setText(str(self.date.year))

    def init_weekday_panel(self, main_layout):
        weekday_panel = QWidget()
        weekday_layout = QHBoxLayout()
        weekday_layout.setContentsMargins(0, 0, 0, 0)
        weekday_layout.setSpacing(0)

        # Create buttons and its configuration
        btnMonday = QPushButton()
        btnTuesday = QPushButton()
        btnWednesday = QPushButton()
        btnThursday = QPushButton()
        btnFriday = QPushButton()
        btnSaturday = QPushButton()
        btnSunday = QPushButton()

        btnMonday.setEnabled(False)
        btnTuesday.setEnabled(False)
        btnWednesday.setEnabled(False)
        btnThursday.setEnabled(False)
        btnFriday.setEnabled(False)
        btnSaturday.setEnabled(False)
        btnSunday.setEnabled(False)

        btnMonday.setText('M')
        btnTuesday.setText('T')
        btnWednesday.setText('W')
        btnThursday.setText('T')
        btnFriday.setText('F')
        btnSaturday.setText('S')
        btnSunday.setText('S')

        # Set panel's size
        week_button = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        week_button.setHorizontalStretch(1)
        panel_policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        panel_policy.setVerticalStretch(2)

        btnMonday.setSizePolicy(week_button)
        btnTuesday.setSizePolicy(week_button)
        btnWednesday.setSizePolicy(week_button)
        btnThursday.setSizePolicy(week_button)
        btnFriday.setSizePolicy(week_button)
        btnSaturday.setSizePolicy(week_button)
        btnSunday.setSizePolicy(week_button)
        weekday_panel.setSizePolicy(panel_policy)

        # Set buttons' access
        self.btnMonday = btnMonday
        self.btnTuesday = btnTuesday
        self.btnWednesday = btnWednesday
        self.btnThursday = btnThursday
        self.btnFriday = btnFriday
        self.btnSaturday = btnSaturday
        self.btnSunday = btnSunday

        # Adding buttons in to the layout
        weekday_layout.addWidget(self.btnMonday)
        weekday_layout.addWidget(self.btnTuesday)
        weekday_layout.addWidget(self.btnWednesday)
        weekday_layout.addWidget(self.btnThursday)
        weekday_layout.addWidget(self.btnFriday)
        weekday_layout.addWidget(self.btnSaturday)
        weekday_layout.addWidget(self.btnSunday)

        weekday_panel.setLayout(weekday_layout)
        main_layout.addWidget(weekday_panel)

    def init_month_panel(self, main_layout):
        # Create table
        month_table = QWidget()
        month_layout = QVBoxLayout()
        month_layout.setContentsMargins(0, 0, 0, 0)
        month_layout.setSpacing(0)
        month_panel = QTableWidget()
        month_panel.setObjectName("month_panel")
        month_panel.setEditTriggers(QTableWidget.NoEditTriggers)
        month_panel.setSelectionMode(QTableWidget.NoSelection)

        # Connect buttons
        month_panel.clicked.connect(self.button_controller)

        # Other
        month_panel.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        month_panel.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        month_panel.setAutoScroll(False)

        # Set panel's size
        panel_policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        panel_policy.setVerticalStretch(12)
        month_table.setSizePolicy(panel_policy)

        self.month_panel = month_panel
        self.update_panel()
        # Add table in to the layout
        month_layout.addWidget(self.month_panel)
        month_table.setLayout(month_layout)
        main_layout.addWidget(month_table)

    def update_panel(self):
        # Date
        year = self.date.year
        month = self.date.month

        self.btnMonth.setText(self.month_list[month - 1])
        self.btnYear.setText(str(year))

        if self.show_months:

            self.btnMonday.setText('M')
            self.btnTuesday.setText('T')
            self.btnWednesday.setText('W')
            self.btnThursday.setText('T')
            self.btnFriday.setText('F')
            self.btnSaturday.setText('S')
            self.btnSunday.setText('S')

            # Month table size
            self.month_panel.setColumnCount(7)
            self.month_panel.setRowCount(len(calendar.monthcalendar(year, month)))
            # Filling up the month table
            for i in range(self.month_panel.rowCount()):
                self.month_panel.verticalHeader().setSectionResizeMode(i, QHeaderView.Stretch)
                for j in range(self.month_panel.columnCount()):
                    self.month_panel.horizontalHeader().setSectionResizeMode(j, QHeaderView.Stretch)
                    item = QTableWidgetItem()
                    font = QFont()
                    font.setPointSize(8)
                    item.setFont(font)
                    item.setTextAlignment(Qt.AlignCenter)
                    item.setText(str(calendar.monthcalendar(year, month)[i][j]))
                    if item.text() == '0':
                        item.setText('')
                    # Highlight current date
                    if str(self.cur_date.year) == self.btnYear.text() \
                            and self.month_list[self.cur_date.month - 1] == self.btnMonth.text() \
                            and item.text() == str(self.cur_date.day):
                        item.setForeground(Qt.black)
                        self.month_panel.setItem(i, j, item)
                    else:
                        self.month_panel.setItem(i, j, item)
            # Cell size
            self.month_panel.horizontalHeader().setVisible(False)
            # self.month_panel.horizontalHeader().setMinimumSectionSize(self.cell_width)
            # self.month_panel.horizontalHeader().setDefaultSectionSize(self.cell_width)
            self.month_panel.verticalHeader().setVisible(False)
            # self.month_panel.verticalHeader().setMinimumSectionSize(self.cell_height)
            # self.month_panel.verticalHeader().setDefaultSectionSize(self.cell_height)
        if self.show_years:
            self.btnMonth.setText('MONTHS')

            # Year table size
            self.month_panel.setColumnCount(3)
            self.month_panel.setRowCount(4)

            self.btnMonday.setText('')
            self.btnTuesday.setText('')
            self.btnWednesday.setText('')
            self.btnThursday.setText('')
            self.btnFriday.setText('')
            self.btnSaturday.setText('')
            self.btnSunday.setText('')

            # Filling up the year table
            cur_month = 0
            for i in range(self.month_panel.rowCount()):
                self.month_panel.verticalHeader().setSectionResizeMode(i, QHeaderView.Stretch)
                for j in range(self.month_panel.columnCount()):
                    self.month_panel.horizontalHeader().setSectionResizeMode(j, QHeaderView.Stretch)
                    item = QTableWidgetItem()
                    font = QFont()
                    font.setPointSize(8)
                    item.setFont(font)
                    item.setTextAlignment(Qt.AlignCenter)
                    item.setText(self.month_list[cur_month])
                    cur_month += 1
                    if item.text() == '0':
                        item.setText('')
                    # Highlight current month
                    if str(self.cur_date.year) == self.btnYear.text() \
                            and self.month_list[self.cur_date.month - 1] == item.text():
                        item.setForeground(Qt.black)
                        self.month_panel.setItem(i, j, item)
                    else:
                        self.month_panel.setItem(i, j, item)
            # Cell size
            self.month_panel.horizontalHeader().setVisible(False)
            # self.month_panel.horizontalHeader().setMinimumSectionSize(self.month_panel_width / 3)
            # self.month_panel.horizontalHeader().setDefaultSectionSize(self.month_panel_width / 3)
            self.month_panel.verticalHeader().setVisible(False)
            # self.month_panel.verticalHeader().setMinimumSectionSize(self.navigation_panel_height)
            # self.month_panel.verticalHeader().setDefaultSectionSize(self.navigation_panel_height)
            pass

    # Setting up style
    def set_style(self):
        try:
            icon_prev = QIcon()
            icon_prev.addPixmap(QPixmap("icons/angle-left-solid.svg"), QIcon.Normal, QIcon.Off)
            icon_next = QIcon()
            icon_next.addPixmap(QPixmap("icons/angle-right-solid.svg"), QIcon.Normal, QIcon.Off)
            self.btnPrevious.setIcon(icon_prev)
            self.btnFollowing.setIcon(icon_next)
            self.btnPrevious.setIconSize(QSize(14, 14))
            self.btnFollowing.setIconSize(QSize(14, 14))
            self.setStyleSheet(open(style).read())
        except FileNotFoundError:
            print('style file not found')

    # Buttons controller
    def button_controller(self):
        sender = self.sender()

        if sender.objectName() == 'btnPrevious':
            if self.show_years:
                self.date.year -= 1
            else:
                if self.date.month == 1:
                    self.date.year -= 1
                    self.date.month = 12
                else:
                    self.date.month -= 1
        elif sender.objectName() == 'btnFollowing':
            if self.show_years:
                self.date.year += 1
            else:
                if self.date.month == 12:
                    self.date.year += 1
                    self.date.month = 1
                else:
                    self.date.month += 1

        elif sender.objectName() == 'btnMonth':
            cur_date = datetime.date.today()
            if self.show_months:
                self.date.year = cur_date.year
                self.date.month = cur_date.month
                self.date.day = cur_date.day
            else:
                self.month_panel.clearSelection()
                self.show_months = True
                self.show_years = False
        elif sender.objectName() == 'btnYear':
            cur_date = datetime.date.today()
            if self.show_years:
                self.date.year = cur_date.year
                self.date.month = cur_date.month
                self.date.day = cur_date.day
            else:
                self.month_panel.clearSelection()
                self.show_years = True
                self.show_months = False
            pass

        elif sender.objectName() == 'month_panel':
            if self.show_years:
                self.show_years = False
                self.show_months = True
                self.date.year = int(self.btnYear.text())
                self.date.month = self.month_list.index(self.month_panel.currentItem().text()) + 1
            else:
                try:
                    if self.external.btnFree.isChecked():
                        pass
                    if self.external.btnJob.isChecked():
                        pass
                    if self.external.btnStudy.isChecked():
                        pass
                except AttributeError:
                    print('external is not connected')

        self.update_panel()

    def select_days(self, day_type):
        pass

    def connect_external(self, external):
        if self.isExternalConnected:
            return
        else:
            self.external = external
            print('external connected')
        pass