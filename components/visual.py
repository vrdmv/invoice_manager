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
        self.create_piechart()

    def create_piechart(self):
        """Create a pie chart that lays out all of the invoices' current status"""
        series = QPieSeries()
        val_dispatched = get_dispatched()
        val_paid = get_paid()
        val_overdue = get_overdue()
        series.append("Dispatched", val_dispatched)
        series.append("Overdue", val_overdue)
        series.append("Paid", val_paid)

        pie_slice = QPieSlice()
        pie_slice.setExploded(True)
        pie_slice.setLabelVisible(True)
        pie_slice.setPen(QPen(Qt.darkGreen, 2))
        pie_slice.setBrush(Qt.green)

        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Invoice status summary: ")

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)
        self.layout.addWidget(chartview)