import sys

from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow


def main():
    # tdf_list = Race.load_races_from_file(os.path.join(os.getcwd(), 'data', 'TDF.csv'))
    # pprint(tdf_list)
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
