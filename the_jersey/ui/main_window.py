import os

from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QLineEdit

from model.model import Model
from model.race import Race
from ui.generated.ui_mainwindow import Ui_MainWindow


class RacesTableModel(QtCore.QAbstractTableModel):
    def __init__(self, model: Model):
        super().__init__()
        self.model = model

    def columnCount(self, index):
        return len(self.model.displayed_races[0]) if self.model.races else None

    def rowCount(self, index):
        return len(self.model.displayed_races)

    def data(self, index, role):
        race = self.model.displayed_races[index.row()]
        value = tuple(vars(race).values())[index.column()]
        if role == Qt.DisplayRole:
            return value
        elif role == Qt.BackgroundRole:
            if not self.model.search_text:
                return QtGui.QColor("white")
            if self.model.search_text in str(value).lower():
                return QtGui.QColor("#54b7ec")

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self.model.header[section])
            if orientation == Qt.Vertical:
                return str(section + 1)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.showMaximized()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        header, races = Race.load_races_from_file(os.path.join(os.getcwd(), 'data', 'TDF.csv'))
        self.model = Model(self.ui.le_search.text(), header, races)
        # self.original_races = self.races
        self.races_table_model = RacesTableModel(self.model)
        self.ui.tv_races.setModel(self.races_table_model)
        self.ui.tv_races.resizeColumnsToContents()
        self.ui.le_search.textChanged.connect(self.filter_racestable)

    def filter_racestable(self):
        self.model.search_text = self.ui.le_search.text()
        # self.model.races = [race for race in self.races if self.ui.le_search.text().lower() in race.values_to_str()]
        self.races_table_model.layoutChanged.emit()
        self.ui.tv_races.resizeColumnsToContents()
        # pprint(self.races)
