import sys
from pprint import pprint

from PySide6.QtWidgets import QApplication

from model.race import Race
import os

from ui.main_window import MainWindow


def main():
    # tdf_list = Race.load_races_from_file(os.path.join(os.getcwd(), 'data', 'TDF.csv'))
    # pprint(tdf_list)
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()

if __name__ == '__main__':
    main()