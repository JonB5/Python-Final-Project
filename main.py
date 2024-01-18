import sys
from PyQt5 import QtWidgets

from new_gui.GUI_mainbox import UiMainWindow
#from GUI_mainbox import UiMainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setup_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


main()
