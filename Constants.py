# There will be constant values for this program
from PyQt5 import QtGui, QtWidgets

# """ Train types, where 1 it's time for learning. (READ/WATCH, PRACTICE, REPEAT) """
# PIP (Practice in priority), AE (All equally)
train_types = {'PIP': (0.25, 0.5, 0.25), 'AE': (0.33, 0.33, 0.34)}

# Learning speed
read_speed = None  # measured in PAGE per HOUR
watch_speed = None  # measured in RANGE(0.75 - 2) video speed
learn_speeds = {'reading': read_speed, 'watching': watch_speed}

# Learning intensity
learn_intensity = None

# Screen Operator modes
START_MODE = 0
LEARN_VARIABLES_MODE = 1
CREATE_SCHEDULE_MODE = 2
SHOW_UTIL_MODE = 3


class Assets:
    
    def __init__(self):
        # Icons
        nextIcon = QtGui.QIcon()
        nextIcon.addPixmap(QtGui.QPixmap("icons/angle-right-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        backIcon = QtGui.QIcon()
        backIcon.addPixmap(QtGui.QPixmap("icons/angle-left-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        settingsIcon = QtGui.QIcon()
        settingsIcon.addPixmap(QtGui.QPixmap("icons/cog-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        createIcon = QtGui.QIcon()
        createIcon.addPixmap(QtGui.QPixmap("icons/plus-stick.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        angleDownIcon = QtGui.QIcon()
        angleDownIcon.addPixmap(QtGui.QPixmap("icons/angle-down-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # Fonts
        btnFont = QtGui.QFont()
        btnFont.setPointSize(12)
        headerFont = QtGui.QFont()
        headerFont.setPointSize(12)
        tipFont = QtGui.QFont()
        tipFont.setPointSize(8)
        listFont = QtGui.QFont()
        listFont.setPointSize(8)
        nameFont = QtGui.QFont()
        nameFont.setPointSize(25)
        # Size Policies
        descriptionPolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        descriptionPolicy.setHorizontalStretch(12)
        titlesPolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        titlesPolicy.setHorizontalStretch(5)
        sortPolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sortPolicy.setHorizontalStretch(1)
        calendarPolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        calendarPolicy.setVerticalStretch(3)
        fieldPolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        pageBarPolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        btnPolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        btnPolicy.setHorizontalStretch(1)
        # fieldPolicy.setHorizontalStretch(1)

        self.NEXT_ICON = nextIcon
        self.BACK_ICON = backIcon
        self.SETTINGS_ICON = settingsIcon
        self.CREATE_ICON = createIcon
        self.ANGLE_DONW_ICON = angleDownIcon

        self.NAME_FONT = nameFont
        self.HEADER_FONT = headerFont
        self.TIP_FONT = tipFont
        self.LIST_FONT = listFont
        self.BTN_FONT = btnFont

        self.PAGE_BAR_POLICY = pageBarPolicy
        self.DESCRIPTION_POLICY = descriptionPolicy
        self.TITLES_POLICY = titlesPolicy
        self.SORT_POLICY = sortPolicy
        self.CALENDAR_POLICY = calendarPolicy
        self.FIELD_POLICY = fieldPolicy
        self.BTN_POLICY = btnPolicy

