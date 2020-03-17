from PyQt5 import QtWidgets
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from database import *


class Visual(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)
        # self.i = 0
       #  self.timer = QTimer()
        # self.timer.setInterval(3000)
        # self.timer.timeout.connect(self.update_piechart)
        # self.timer.start()
        self.series = QPieSeries()
        self.pie_slice = QPieSlice()
        self.chart = QChart()
        self.chartview = QChartView(self.chart)
        self.create_piechart()

    def update_piechart(self):
        # self.i += 1
        self.series.clear()
        self.num_disp = get_dispatched()
        self.num_ovrd = get_overdue()
        self.num_paid = get_paid()
        self.series.append("Dispatched", self.num_disp)
        self.series.append("Overdue", self.num_ovrd)
        self.series.append("Paid", self.num_paid)


    def create_piechart(self):
        """Create a pie chart that lays out all of the invoices' current status"""
        self.pie_slice.setExploded(True)
        self.pie_slice.setLabelVisible(True)
        self.pie_slice.setPen(QPen(Qt.darkGreen, 2))
        self.pie_slice.setBrush(Qt.green)

        self.chart.legend().hide()
        self.chart.addSeries(self.series)
        self.chart.createDefaultAxes()
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.setTitle("Invoice status summary: ")

        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)

        self.chartview.setRenderHint(QPainter.Antialiasing)
        self.layout.addWidget(self.chartview)



