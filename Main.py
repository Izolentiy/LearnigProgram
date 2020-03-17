from PyQt5.QtWidgets import QApplication

import sys
import ScreenOperator

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ScreenOperator.ScreenController()

    sys.exit(app.exec_())
