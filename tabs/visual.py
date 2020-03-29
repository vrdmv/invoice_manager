from PyQt5 import QtWidgets
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QFont
from PyQt5.QtCore import Qt
from components import database


class Visual(QtWidgets.QWidget):
    """A class to visualize and summarize the status of all invoices"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QtWidgets.QHBoxLayout()
        self.setLayout(self.layout)
        self.series = QPieSeries()
        self.pie_slice = QPieSlice()
        self.chart = QChart()
        self.chartview = QChartView(self.chart)
        self.create_piechart()

    def update_piechart(self):
        """Update pie chart with most recent status summary """
        self.series.clear()
        self.num_dispatched = database.get_dispatched()
        self.num_overdue = database.get_overdue()
        self.num_paid = database.get_paid()
        self.series.append("Dispatched", self.num_dispatched)
        self.series.append("Overdue", self.num_overdue)
        self.series.append("Paid", self.num_paid)

    def create_piechart(self):
        """Create a pie chart that lays out all of the invoices'
        current status"""
        self.chart.addSeries(self.series)
        self.chart.createDefaultAxes()
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        self.chart.setTitle("Invoice status summary: ")
        self.chart.setTitleFont(font)
        self.chart.setTheme(QChart.ChartThemeBlueIcy)
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)
        self.chartview.setRenderHint(QPainter.Antialiasing)
        self.layout.addWidget(self.chartview)
